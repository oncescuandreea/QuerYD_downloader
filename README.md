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
python download_queryd.py --txt_file relevant-video-links-test.txt --task download_videos
```
This will create a folder called videos in your current folder and videos will be saved there.
To fully run the download_videos script run:
```
python download_queryd.py --txt_file relevant-video-links.txt --task download_videos
```
To attempt downloading videos multiple times, set the --tries flag to the desired value. By default the value is 2. Eg:
```
python download_queryd.py --txt_file relevant-video-links.txt --tries 3 --task download_videos
```
To re-download all files use the --refresh flag. Eg:
```
python download_queryd.py --txt_file relevant-video-links.txt --refresh --task download_videos
```

**Downloading json metadata** \
To download the .json file containing information about the described videos run:
```
python download_queryd.py --txt_file relevant-video-links.txt --task annotations
```

**Downloading audio description files** \
Audio files can be downloaded only after downloading the .json metadata using the previous step.\
To download the audio description files corresponding to each video, run:
```
python download_queryd.py --txt_file relevant-video-links.txt --task download_wavs
```
To use more processes add the --processes flag with the number of CPUs available. eg:
```
python download_queryd.py --txt_file relevant-video-links.txt --task download_wavs --processes 2
```
