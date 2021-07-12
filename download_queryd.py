import argparse
import json
import logging
import multiprocessing as mp
import os
from datetime import datetime
from pathlib import Path

import pytube
import requests
import tqdm
from pytube.exceptions import RegexMatchError, VideoRegionBlocked, VideoUnavailable, VideoPrivate
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from zsvision.zs_multiproc import starmap_with_kwargs

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def download_one_video(tries: int,
                       url: str,
                       video_dir: Path,
                       video_id: str,
                       failed_folder: Path):
    """
    Try downloading one video repeatedly.
    Inputs:
        tries: number of attempted downloads before giving up
        url: url of video to be downloaded
        video_dir: location where video is stored
        video_id: unique video id corresponding to YouTube id
        logging: logger saving printed info into files named according
                 to creation time
    """
    no_tries = 0
    while no_tries <= tries:
        try:
            print(f"Downloading video {video_id}")
            video_name = f"video-{video_id}"
            youtube = pytube.YouTube(url)
            video = youtube.streams.first()
            no_tries += 1
            video.download(video_dir, filename=video_name)
            no_tries = tries + 1
            print(f"Finished downloading video {video_id}")
        except RegexMatchError:
            if no_tries == tries:
                print(f"Video {video_id} unavailable")
                with open(failed_folder / f'{video_id}_region.txt', 'w') as f:
                    pass
            no_tries += 1
            continue
        # except KeyError:
        #     #Windows error
        #     print(f"Video {video_id} unavailable")
        #     no_tries = tries + 1
        #     with open(failed_folder / f'{video_id}_unavailable.txt', 'w') as f:
        #         pass
        # except VideoRegionBlocked:
        #     print(f"Video {video_id} unavailable in your region")
        #     with open(failed_folder / f'{video_id}_region.txt', 'w') as f:
        #         pass
        #     break
        # except VideoUnavailable:
        #     print(f"Video {video_id} unavailable")
        #     with open(failed_folder / f'{video_id}_unavailable.txt', 'w') as f:
        #         pass
        #     break
        # except VideoPrivate:
        #     print(f"Video {video_id} private")
        #     with open(failed_folder / f'{video_id}_private.txt', 'w') as f:
        #         pass
        #     break
        except Exception as e:
            print(f"Video {video_id} encountered error {e}")
            with open(failed_folder / f'{video_id}.txt', 'w') as f:
                f.write(f"Video {video_id} encountered error {e}")
                f.write('\n')
            break

def download_videos(video_dir: Path,
                    txt_file: Path,
                    tries: int,
                    refresh: bool,
                    processes: int,
                    logging: logging.basicConfig):
    """File goes through list of existent videos in QuerYD dataset and
    attempts to download them. Videos are saved with the name "video-{video_id}".
    Inputs:
        video_dir: location where videos are saved
        tries: how many times to attempt downloading a video
        refresh: flag to restart the downloading process
        logging: logging module for saving information about progress of script
    """
    with open(txt_file, 'r') as f:
        video_links = f.read().splitlines()
    os.makedirs(video_dir, exist_ok=True)
    failed_folder = 'failed_folder'
    os.makedirs(failed_folder, exist_ok=True)
    existent_videos = os.listdir(video_dir)
    existent_ids = [video.split('video-')[1].split('.')[0] for video in existent_videos]
    total_number_videos = len(video_links)
    logging.info("Downloading videos")
    kwarg_list = []
    for idx, url in enumerate(video_links):
        video_id = url.split('https://www.youtube.com/watch?v=')[1]
        if video_id not in existent_ids or refresh is True:
            kwarg_list.append({
            "tries": tries,
            "url": url,
            "video_dir": video_dir,
            "video_id": video_id,
            "failed_folder": Path(failed_folder),
            })               
        else:
            logging.info(f"Already downloaded video {video_id}")     

    pool_func = download_one_video
    if processes > 1:
        # The definition of the pool func must precede the creation of the pool
        # to ensure its pickleable.  We force the definition to occur by reassigning
        # the function.
        with mp.Pool(processes=processes) as pool:
            starmap_with_kwargs(pool=pool, func=pool_func, kwargs_iter=kwarg_list)
    else:
        for idx, kwarg in enumerate(kwarg_list):
            print(f"{idx}/{len(kwarg_list)} processing kwargs ")
            pool_func(**kwarg)

def download_wavs(txt_file: Path,
                  refresh: bool,
                  api_wav_endpoint: str,
                  data_dir: Path,
                  processes: int,
                  legacy_only: bool):
    wav_dir = data_dir / "wav-files"
    wav_dir.mkdir(parents=True, exist_ok=True)
    triplets = []
    with open(txt_file, 'r') as f:
        video_links = f.read().splitlines()
    annotation_folder = data_dir / 'describe-api-results'
    for url in tqdm.tqdm(video_links):
        video_id = url.split('https://www.youtube.com/watch?v=')[1]
        src_path = annotation_folder / f"assets-{video_id}.json"
        with open(src_path, "r") as f:
            info = json.load(f)
        for desc in info["result"]["audio_descriptions"]:
            for clip in desc["audio_clips"]:
                wav_file = clip["file_name"]
                if Path(clip["file_path"]).name == "legacy":
                    wav_parent = Path(clip["file_path"]).name
                else:
                    wav_parent = Path(clip["file_path"]).parent.name
                if wav_file:
                    triplets.append((video_id, wav_file, wav_parent))
    print(f"Parsed {len(triplets)} in total")

    if legacy_only:
        prev = len(triplets)
        triplets = [x for x in triplets if x[2] == "legacy"]
        print(f"Filtered to legacy only wavs ({prev} -> {len(triplets)}")

    kwarg_list = []
    for url, wav_file, wav_parent in triplets:
        kwarg_list.append({
            "url": url,
            "wav_dir": wav_dir,
            "wav_file": wav_file,
            "wav_parent": wav_parent,
            "refresh": refresh,
            "api_wav_endpoint": api_wav_endpoint,
        })

    pool_func = fetch_wav_worker
    if processes > 1:
        # The definition of the pool func must precede the creation of the pool
        # to ensure its pickleable.  We force the definition to occur by reassigning
        # the function.
        with mp.Pool(processes=processes) as pool:
            starmap_with_kwargs(pool=pool, func=pool_func, kwargs_iter=kwarg_list)
    else:
        for idx, kwarg in enumerate(kwarg_list):
            print(f"{idx}/{len(kwarg_list)} processing kwargs ")
            pool_func(**kwarg)

def fetch_wav_worker(
    url: str,
    wav_file: str,
    wav_dir: Path,
    wav_parent: str,
    api_wav_endpoint: str,
    refresh: bool,
):
    if wav_parent == "legacy":
        full_url = f"{api_wav_endpoint}/{wav_parent}/{wav_file}"
    else:
        full_url = f"{api_wav_endpoint}/{wav_parent}/{url}/{wav_file}"
    dest_path = wav_dir / f"video-{url}" / f"audio-{wav_file}"
    dest_path.parent.mkdir(exist_ok=True, parents=True)
    if dest_path.exists() and not refresh:
        print(f"Found existing result at {dest_path}, skipping...")
        return
    resp = requests.get(full_url, verify=False)
    print(f"Fetching {full_url} -> {dest_path} [{resp.status_code}]")
    if resp.status_code == 200 and "not found" not in resp.text:
        with open(dest_path, "wb") as f:
            f.write(resp.content)
    else:
        print(f"Skipping due to failed request {resp.text}")
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--video_dir",
        type=Path,
        default="videos",
    )
    parser.add_argument(
        "--data_dir",
        type=Path,
        default=".",
    )
    parser.add_argument(
        "--tries",
        type=int,
        default=2,
        help="how many times to attempt downloading a video"
    )
    parser.add_argument(
        "--refresh",
        action="store_true"
    )
    parser.add_argument(
        "--txt_file",
        type=Path,
        default='relevant-video-links.txt'
    )
    parser.add_argument("--legacy_only", action="store_true")
    parser.add_argument("--processes", type=int, default=1)
    parser.add_argument(
        "--api_wav_endpoint",
        default="https://api.youdescribe.org/audio-descriptions-files",
    )
    parser.add_argument("--task", default="download_videos",
                        choices=["download_videos", "download_wavs"])
    args = parser.parse_args()
    os.makedirs('logs', exist_ok=True)
    logging.basicConfig(filename=f"logs/{datetime.now().strftime(r'%m%d_%H%M%S')}.log",
                        level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())
    if args.task in "download_videos":
        download_videos(args.video_dir, args.txt_file,
                        args.tries, args.refresh,
                        args.processes, logging)
    elif args.task in "download_wavs":
        download_wavs(args.txt_file,
                      args.refresh,
                      args.api_wav_endpoint,
                      args.data_dir,
                      args.processes,
                      args.legacy_only)
    
if __name__ == "__main__":
    main()
