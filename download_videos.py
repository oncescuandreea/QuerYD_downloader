import argparse
import os
from pathlib import Path

import pytube
from pytube.exceptions import RegexMatchError
import logging
from datetime import datetime

def download_one_video(tries: int,
                       url: str,
                       video_dir: Path,
                       video_id: str,
                       logging):
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
            logging.info(f"Downloading video {video_id}")
            video_name = f"video-{video_id}"
            youtube = pytube.YouTube(url)
            video = youtube.streams.first()
            no_tries += 1
            video.download(video_dir, filename=video_name)
            no_tries = tries + 1
        except RegexMatchError:
            if no_tries == tries:
                logging.info(f"Video {video_id} unavailable")
            no_tries += 1
            continue
        except KeyError:
            "Windows error"
            logging.info(f"Video {video_id} unavailable")
            no_tries = tries + 1

def download_videos(video_dir: Path,
                    tries: int,
                    refresh: bool,
                    logging):
    """File goes through list of existent videos in QuerYD dataset and
    attempts to download them. Videos are saved with the name "video-{video_id}".
    Inputs:
        video_dir: location where videos are saved
        tries: how many times to attempt downloading a video
        refresh: flag to restart the downloading process
        logging: logging module for saving information about progress of script
    """
    with open('relevant-video-links.txt', 'r') as f:
        video_links = f.read().splitlines()
    os.makedirs(video_dir, exist_ok=True)
    existent_videos = os.listdir(video_dir)
    existent_ids = [video.split('video-')[1].split('.')[0] for video in existent_videos]
    total_number_videos = len(video_links)
    logging.info("Downloading videos")
    for idx, url in enumerate(video_links):
        video_id = url.split('https://www.youtube.com/watch?v=')[1]
        if video_id not in existent_ids or refresh is True:
            download_one_video(tries, url, video_dir, video_id, logging)                 
        else:
            logging.info(f"Already downloaded video {video_id}")
        if idx % 10 == 0 and idx != 0:
            logging.info(f"Reached {idx}/{total_number_videos}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--video_dir",
        type=Path,
        default="videos",
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
    args = parser.parse_args()
    os.makedirs('logs', exist_ok=True)
    logging.basicConfig(filename=f"logs/{datetime.now().strftime(r'%m%d_%H%M%S')}.log",
                        level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())
    download_videos(args.video_dir, args.tries, args.refresh, logging)
if __name__ == "__main__":
    main()
