# QuerYD_download

This is a tool to allow for easy download of the videos forming the QuerYD dataset.

**Installing necessary libraries:**
* argparse
* pytube
* pathlib
* logging

**Downloading videos** \
To test the download videos script for the QuerYD dataset simply run:
```
python download_videos.py --txt_file relevant-video-links-test.txt
```
This will create a folder called videos in your current folder and videos will be saved there.
To fully run the download_videos script run:
```
python download_videos.py --txt_file relevant-video-links.txt
```
To attempt downloading videos multiple times, set the --tries flag to the desired value. By default the value is 2. Eg:
```
python download_videos.py --txt_file relevant-video-links.txt --tries 3
```
To re-download all files use the --refresh flag. Eg:
```
python download_videos.py --txt_file relevant-video-links.txt --refresh
```
