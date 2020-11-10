import argparse
import os
from pathlib import Path

import pytube


def download_videos(video_dir: Path,
                    refresh: bool):
    with open('relevant-video-links-test.txt', 'r') as f:
        video_links = f.read().splitlines()
    # existent_videos = os.listdir(video_dir)
    for url in video_links:
        youtube = pytube.YouTube(url)
        video = youtube.streams.first()
        video.download(video_dir)

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
