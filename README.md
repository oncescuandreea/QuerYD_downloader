# QuerYD_download

This is a tool to allow for easy download of the videos forming the QuerYD dataset.

**Installing necessary libraries:**
* argparse
* pytube ```python -m pip install git+https://github.com/nficano/pytube```
* pathlib
* logging
* multiprocessing
* requests
* tqdm
* json
* zsvision

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
wget http://www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/QuerYD/json_metadata.zip
unzip json_metadata.zip
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

**Downloading transcribed descriptions and corresponding time-stamps**\
The transcribed version of the audio descriptions can be downloaded as a pickle file by accessing the following link:
```
http://www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/QuerYD/raw_captions_combined_filtered.pkl
```
The corresponding time-stamps in the same order are provided in this pickle file:
```
http://www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/QuerYD/times_captions_combined_filtered.pkl
```
The confidence of the transcriptions in the same order as transcriptions are found here:
```
http://www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/QuerYD/confidence_captions_combined_filtered.pkl
```

**Downloading video features, descriptions and train/val/test splits**\
To download QuerYD data:
```
wget http://www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/features-v2/QuerYD-experts.tar.gz
```
To download QuerYDSegments data (localised clips and their descriptions):
```
wget http://www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/features-v2/QuerYDSegments-experts.tar.gz
```

More info and scripts used can be found at https://github.com/albanie/collaborative-experts#queryd and training and test steps can be followed from https://github.com/albanie/collaborative-experts#evaluating-a-pretrained-model where MSVD should be replaced by QuerYD or QuerYDSegments. Model names should be taken from retrieval results tables at https://github.com/albanie/collaborative-experts#queryd or https://github.com/albanie/collaborative-experts#querydsegments .

### References
[1] If you find this code useful, please consider citing:
```
@misc{oncescu2021queryd,
      title={QuerYD: A video dataset with high-quality text and audio narrations}, 
      author={Andreea-Maria Oncescu and João F. Henriques and Yang Liu and Andrew Zisserman and Samuel Albanie},
      year={2021},
      eprint={2011.11071},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

[2] If you find this code useful or use the extracted features, please consider citing:

```
@inproceedings{Liu2019a,
  author    = {Liu, Y. and Albanie, S. and Nagrani, A. and Zisserman, A.},
  booktitle = {arXiv preprint arxiv:1907.13487},
  title     = {Use What You Have: Video retrieval using representations from collaborative experts},
  date      = {2019},
}
```




### Acknowledgements

This work is supported by the EP-SRC (VisualAI EP/T028572/1 and DTA Studentship), and theRoyal Academy of Engineering (DFR05420). We are gratefulto Sophia Koepke for her helpful comments and suggestions.

