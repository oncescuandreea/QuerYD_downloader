import argparse
import os
from pathlib import Path

import pytube


def download_videos(video_dir: Path,
                    refresh: bool):
    with open('relevant-video-links-test.txt', 'r') as f:
        video_links = f.read().splitlines()
    existent_videos = os.listdir(video_dir)
    existent_ids = [video.split('video-')[1].split('.')[0] for video in existent_videos]
    total_number_videos = len(video_links)
    print("Downloading videos")
    for idx, url in enumerate(video_links):
        video_id = url.split('https://www.youtube.com/watch?v=')[1]
        if video_id not in existent_ids or refresh is True:
            video_name = f"video-{video_id}"
            youtube = pytube.YouTube(url)
            video = youtube.streams.first()
            video.download(video_dir, filename=video_name)
        else:
            print(f"Already downloaded video {video_id}")
        if idx % 10 == 0 and idx != 0:
            print(f"Reached {idx}/{total_number_videos}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--video_dir",
        type=Path,
        default="videos",
    )
    parser.add_argument(
        "--refresh",
        action="store_true"
    )
    args = parser.parse_args()
    download_videos(args.video_dir, args.refresh)
if __name__ == "__main__":
    main()
