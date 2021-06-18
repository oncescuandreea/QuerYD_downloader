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

## Version 2 of the dataset has been added on 8th of April

**Downloading videos** \
To test the download videos script for the QuerYD dataset simply run:
```
python download_queryd.py --txt_file relevant-video-links-test.txt --task download_videos
```
This will create a folder called videos in your current folder and videos will be saved there.
To fully run the download_videos script run:
```
python download_queryd.py --txt_file relevant-video-links-{version either v1 or v2}.txt --task download_videos
```
To attempt downloading videos multiple times, set the --tries flag to the desired value. By default the value is 2. Eg:
```
python download_queryd.py --txt_file relevant-video-links-{version either v1 or v2}.txt --tries 3 --task download_videos
```
To re-download all files use the --refresh flag. Eg:
```
python download_queryd.py --txt_file relevant-video-links-{version either v1 or v2}.txt --refresh --task download_videos
```

**Downloading json metadata** \
To download the .json file containing information about the described videos run:
```
wget http://www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/QuerYD/json_metadata-{version either v1 or v2}.zip
mv json_metadata-{version either v1 or v2}.zip json_metadata.zip
unzip json_metadata.zip
```

**Downloading audio description files** \
Audio files can be downloaded only after downloading the .json metadata using the previous step.\
To download the audio description files corresponding to each video, run:
```
python download_queryd.py --txt_file relevant-video-links-{version either v1 or v2}.txt --task download_wavs
```
To use more processes add the --processes flag with the number of CPUs available. eg:
```
python download_queryd.py --txt_file relevant-video-links-{version either v1 or v2}.txt --task download_wavs --processes 2
```

**Downloading transcribed descriptions and corresponding time-stamps**\
The transcribed version of the audio descriptions can be downloaded as a pickle file by accessing the following link:
```
http://www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/QuerYD/raw_captions_combined_filtered-{version either v1 or v2}.pkl
mv raw_captions_combined_filtered-{version either v1 or v2}.pkl raw_captions_combined_filtered.pkl
```
The corresponding time-stamps in the same order are provided in this pickle file:
```
http://www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/QuerYD/times_captions_combined_filtered-{version either v1 or v2}.pkl
mv times_captions_combined_filtered-{version either v1 or v2}.pkl times_captions_combined_filtered.pkl
```
The confidence of the transcriptions in the same order as transcriptions are found here:
```
http://www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/QuerYD/confidence_captions_combined_filtered-{version either v1 or v2}.pkl
mv confidence_captions_combined_filtered-{version either v1 or v2}.pkl confidence_captions_combined_filtered.pkl
```

**Downloading video features, descriptions and train/val/test splits**\
To download QuerYD data:
```
wget http://www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/features-v2/QuerYD-experts-{version either v1 or v2}.tar.gz
mv QuerYD-experts-{version either v1 or v2}.tar.gz QuerYD-experts.tar.gz
```
To download QuerYDSegments data (localised clips and their descriptions):
```
wget http://www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/features-v2/QuerYDSegments-experts-{version either v1 or v2}.tar.gz
mv QuerYDSegments-experts-{version either v1 or v2}.tar.gz QuerYDSegments-experts.tar.gz
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

This work is supported by the EP-SRC (VisualAI EP/T028572/1 and DTA Studentship), and the Royal Academy of Engineering (DFR05420). We are gratefulto Sophia Koepke for her helpful comments and suggestions.


### 2nd Version of QuerYD retrieval results:

### QuerYD

### MODEL study on QUERYD

**Importance of the model**:

| Model | Task | R@1 | R@5 | R@10 | R@50 | MdR | MnR | Geom | params | Links |
| ----- | ---- | --- | --- | ---- | ---- | --- | --- | ----- | -- | -- |
| HowTo100m S3D | t2v  | <sub><sup>10.2<sub>(0.0)</sub></sup></sub> | <sub><sup>24.5<sub>(0.0)</sub></sup></sub> | <sub><sup>32.7<sub>(0.0)</sub></sup></sub> | <sub><sup>54.3<sub>(0.0)</sub></sup></sub> | <sub><sup>38.0<sub>(0.0)</sub></sup></sub> | <sub><sup>82.1<sub>(0.0)</sub></sup></sub> | <sub><sup>20.2<sub>(0.0)</sub></sup></sub> | 1 | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-mnnet/7e1a7420/seed-0/2021-05-28_16-38-33/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-mnnet/7e1a7420/seed-0/2021-05-28_16-38-33/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-mnnet/7e1a7420/seed-0/2021-05-28_16-38-33/summary-seed-0_seed-1_seed-2.json) |
| CE - P,CG | t2v  | <sub><sup>29.8<sub>(0.3)</sub></sup></sub> | <sub><sup>63.8<sub>(0.5)</sub></sup></sub> | <sub><sup>74.9<sub>(0.3)</sub></sup></sub> | <sub><sup>93.0<sub>(0.1)</sub></sup></sub> | <sub><sup>3.0<sub>(0.0)</sub></sup></sub> | <sub><sup>15.1<sub>(0.4)</sub></sup></sub> | <sub><sup>52.3<sub>(0.3)</sub></sup></sub> | 57.75M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-moee/ab5db961/seed-0/2021-05-28_15-32-38/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-moee/ab5db961/seed-0/2021-05-28_15-32-38/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-moee/ab5db961/seed-0/2021-05-28_15-32-38/summary-seed-0_seed-1_seed-2.json) |
| CE    | t2v  | <sub><sup>31.9<sub>(1.5)</sub></sup></sub> | <sub><sup>64.5<sub>(1.4)</sub></sup></sub> | <sub><sup>76.1<sub>(0.8)</sub></sup></sub> | <sub><sup>93.8<sub>(0.9)</sub></sup></sub> | <sub><sup>3.0<sub>(0.0)</sub></sup></sub> | <sub><sup>13.1<sub>(0.8)</sub></sup></sub> | <sub><sup>53.9<sub>(0.7)</sub></sup></sub> | 30.82M |[config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce/c50d3616/seed-0/2021-05-28_15-24-39/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce/c50d3616/seed-0/2021-05-28_15-24-39/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce/c50d3616/seed-0/2021-05-28_15-24-39/summary-seed-0_seed-1_seed-2.json) |
| HowTo100m S3D | v2t  | <sub><sup>10.0<sub>(0.0)</sub></sup></sub> | <sub><sup>25.7<sub>(0.0)</sub></sup></sub> | <sub><sup>32.3<sub>(0.0)</sub></sup></sub> | <sub><sup>53.2<sub>(0.0)</sub></sup></sub> | <sub><sup>42.0<sub>(0.0)</sub></sup></sub> | <sub><sup>81.7<sub>(0.0)</sub></sup></sub> | <sub><sup>20.2<sub>(0.0)</sub></sup></sub> | 1 | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-mnnet/7e1a7420/seed-0/2021-05-28_16-38-33/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-mnnet/7e1a7420/seed-0/2021-05-28_16-38-33/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-mnnet/7e1a7420/seed-0/2021-05-28_16-38-33/summary-seed-0_seed-1_seed-2.json) |
| CE - P,CG | v2t  | <sub><sup>28.6<sub>(1.1)</sub></sup></sub> | <sub><sup>62.4<sub>(0.5)</sub></sup></sub> | <sub><sup>73.6<sub>(0.8)</sub></sup></sub> | <sub><sup>92.9<sub>(0.1)</sub></sup></sub> | <sub><sup>3.0<sub>(0.0)</sub></sup></sub> | <sub><sup>14.7<sub>(0.4)</sub></sup></sub> | <sub><sup>50.8<sub>(0.7)</sub></sup></sub> | 57.75M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-moee/ab5db961/seed-0/2021-05-28_15-32-38/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-moee/ab5db961/seed-0/2021-05-28_15-32-38/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-moee/ab5db961/seed-0/2021-05-28_15-32-38/summary-seed-0_seed-1_seed-2.json) |
| CE    | v2t  | <sub><sup>32.9<sub>(1.7)</sub></sup></sub> | <sub><sup>64.9<sub>(1.1)</sub></sup></sub> | <sub><sup>76.7<sub>(1.1)</sub></sup></sub> | <sub><sup>93.6<sub>(0.6)</sub></sup></sub> | <sub><sup>3.0<sub>(0.0)</sub></sup></sub> | <sub><sup>12.8<sub>(0.6)</sub></sup></sub> | <sub><sup>54.7<sub>(1.1)</sub></sup></sub> | 30.82M |[config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce/c50d3616/seed-0/2021-05-28_15-24-39/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce/c50d3616/seed-0/2021-05-28_15-24-39/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce/c50d3616/seed-0/2021-05-28_15-24-39/summary-seed-0_seed-1_seed-2.json) |

The influence of different pretrained experts for the performance of the CE model trained on QuerYD is studied. The value and cumulative effect of different experts for scene clas-sification (SCENE), ambient sound classification (AUDIO),image classification (OBJECT), and action recognition (ACTION) are presented. PREV. denotes the experts used in the previous row.

| Experts | Task | R@1 | R@5 | R@10 | R@50 | MdR | MnR | Geom | params | Links |
| ----- | ---- | --- | --- | ---- | ---- | --- | --- | ----- | -- | -- |
| Scene    | t2v  | <sub><sup>17.0<sub>(0.7)</sub></sup></sub> | <sub><sup>47.0<sub>(2.4)</sub></sup></sub> | <sub><sup>60.8<sub>(1.1)</sub></sup></sub> | <sub><sup>85.4<sub>(1.6)</sub></sup></sub> | <sub><sup>6.3<sub>(0.6)</sub></sup></sub> | <sub><sup>27.2<sub>(1.1)</sub></sup></sub> | <sub><sup>36.5<sub>(1.0)</sub></sup></sub> | 7.51M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene/766c0b81/seed-0/2021-05-28_15-39-29/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene/766c0b81/seed-0/2021-05-28_15-39-29/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce-only-scene/766c0b81/seed-0/2021-05-28_15-39-29/summary-seed-0_seed-1_seed-2.json) |
| Prev. + Audio    | t2v  | <sub><sup>21.4<sub>(0.2)</sub></sup></sub> | <sub><sup>53.0<sub>(1.3)</sub></sup></sub> | <sub><sup>63.9<sub>(0.4)</sub></sup></sub> | <sub><sup>88.6<sub>(0.3)</sub></sup></sub> | <sub><sup>5.0<sub>(0.0)</sub></sup></sub> | <sub><sup>22.2<sub>(0.7)</sub></sup></sub> | <sub><sup>41.7<sub>(0.4)</sub></sup></sub> | 17.25M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio/e576753f/seed-0/2021-05-28_16-20-15/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio/e576753f/seed-0/2021-05-28_16-20-15/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce-only-scene-audio/e576753f/seed-0/2021-05-28_16-20-15/summary-seed-0_seed-1_seed-2.json) |
| Prev. + Inst    | t2v  | <sub><sup>32.3<sub>(1.6)</sub></sup></sub> | <sub><sup>65.5<sub>(1.0)</sub></sup></sub> | <sub><sup>76.7<sub>(0.9)</sub></sup></sub> | <sub><sup>93.6<sub>(0.2)</sub></sup></sub> | <sub><sup>3.0<sub>(0.0)</sub></sup></sub> | <sub><sup>13.0<sub>(0.3)</sub></sup></sub> | <sub><sup>54.5<sub>(0.3)</sub></sup></sub> | 24.63M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio-inst/e40f68bf/seed-0/2021-05-28_16-21-50/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio-inst/e40f68bf/seed-0/2021-05-28_16-21-50/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce-only-scene-audio-inst/e40f68bf/seed-0/2021-05-28_16-21-50/summary-seed-0_seed-1_seed-2.json) |
| Prev. + R2P1D    | t2v  | <sub><sup>31.9<sub>(1.5)</sub></sup></sub> | <sub><sup>64.2<sub>(1.4)</sub></sup></sub> | <sub><sup>76.1<sub>(0.7)</sub></sup></sub> | <sub><sup>93.8<sub>(0.9)</sub></sup></sub> | <sub><sup>3.0<sub>(0.0)</sub></sup></sub> | <sub><sup>13.1<sub>(0.8)</sub></sup></sub> | <sub><sup>53.8<sub>(0.7)</sub></sup></sub> | 30.82M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio-inst-r2p1d/54ca249c/seed-0/2021-05-28_16-24-04/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio-inst-r2p1d/54ca249c/seed-0/2021-05-28_16-24-04/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce-only-scene-audio-inst-r2p1d/54ca249c/seed-0/2021-05-28_16-24-04/summary-seed-0_seed-1_seed-2.json) |
| Scene    | v2t  | <sub><sup>20.3<sub>(0.5)</sub></sup></sub> | <sub><sup>47.4<sub>(0.8)</sub></sup></sub> | <sub><sup>60.0<sub>(0.4)</sub></sup></sub> | <sub><sup>85.5<sub>(1.6)</sub></sup></sub> | <sub><sup>6.0<sub>(0.0)</sub></sup></sub> | <sub><sup>27.0<sub>(0.7)</sub></sup></sub> | <sub><sup>38.7<sub>(0.3)</sub></sup></sub> | 7.51M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene/766c0b81/seed-0/2021-05-28_15-39-29/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene/766c0b81/seed-0/2021-05-28_15-39-29/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce-only-scene/766c0b81/seed-0/2021-05-28_15-39-29/summary-seed-0_seed-1_seed-2.json) |
| Prev. + Audio    | v2t  | <sub><sup>23.6<sub>(0.9)</sub></sup></sub> | <sub><sup>52.2<sub>(1.1)</sub></sup></sub> | <sub><sup>63.9<sub>(1.3)</sub></sup></sub> | <sub><sup>89.2<sub>(0.3)</sub></sup></sub> | <sub><sup>5.0<sub>(0.0)</sub></sup></sub> | <sub><sup>21.6<sub>(0.8)</sub></sup></sub> | <sub><sup>42.8<sub>(0.5)</sub></sup></sub> | 17.25M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio/e576753f/seed-0/2021-05-28_16-20-15/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio/e576753f/seed-0/2021-05-28_16-20-15/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce-only-scene-audio/e576753f/seed-0/2021-05-28_16-20-15/summary-seed-0_seed-1_seed-2.json) |
| Prev. + Inst.    | v2t  | <sub><sup>32.6<sub>(1.3)</sub></sup></sub> | <sub><sup>65.6<sub>(0.3)</sub></sup></sub> | <sub><sup>77.2<sub>(0.3)</sub></sup></sub> | <sub><sup>93.7<sub>(0.9)</sub></sup></sub> | <sub><sup>3.0<sub>(0.0)</sub></sup></sub> | <sub><sup>12.5<sub>(0.1)</sub></sup></sub> | <sub><sup>54.8<sub>(0.6)</sub></sup></sub> | 24.63M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio-inst/e40f68bf/seed-0/2021-05-28_16-21-50/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio-inst/e40f68bf/seed-0/2021-05-28_16-21-50/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce-only-scene-audio-inst/e40f68bf/seed-0/2021-05-28_16-21-50/summary-seed-0_seed-1_seed-2.json) |
| Prev. + R2P1D    | v2t  | <sub><sup>32.9<sub>(1.7)</sub></sup></sub> | <sub><sup>65.0<sub>(1.0)</sub></sup></sub> | <sub><sup>76.7<sub>(1.0)</sub></sup></sub> | <sub><sup>93.6<sub>(0.6)</sub></sup></sub> | <sub><sup>3.0<sub>(0.0)</sub></sup></sub> | <sub><sup>12.8<sub>(0.6)</sub></sup></sub> | <sub><sup>54.7<sub>(1.1)</sub></sup></sub> | 30.82M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio-inst-r2p1d/54ca249c/seed-0/2021-05-28_16-24-04/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio-inst-r2p1d/54ca249c/seed-0/2021-05-28_16-24-04/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce-only-scene-audio-inst-r2p1d/54ca249c/seed-0/2021-05-28_16-24-04/summary-seed-0_seed-1_seed-2.json) |


### For QuerYDSegments updated results are

### MODEL study on QUERYDSEGMENTS

**Importance of the model**:

| Model | Task | R@1 | R@5 | R@10 | R@50 | MdR | MnR | Geom | params | Links |
| ----- | ---- | --- | --- | ---- | ---- | --- | --- | ----- | -- | -- |
| HowTo100m S3D | t2v  | <sub><sup>6.4<sub>(0.0)</sub></sup></sub> | <sub><sup>13.8<sub>(0.0)</sub></sup></sub> | <sub><sup>19.9<sub>(0.0)</sub></sup></sub> | <sub><sup>36.3<sub>(0.0)</sub></sup></sub> | <sub><sup>131.0<sub>(0.0)</sub></sup></sub> | <sub><sup>340.0<sub>(0.0)</sub></sup></sub> | <sub><sup>12.1<sub>(0.0)</sub></sup></sub> | 1 | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-mnnet/1404fc28/seed-0/2021-05-28_16-38-32/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-mnnet/1404fc28/seed-0/2021-05-28_16-38-32/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/querydsegments-train-full-mnnet/1404fc28/seed-0/2021-05-28_16-38-32/summary-seed-0_seed-1_seed-2.json) |
| CE - P,CG | t2v  | <sub><sup>21.9<sub>(0.5)</sub></sup></sub> | <sub><sup>44.5<sub>(0.9)</sub></sup></sub> | <sub><sup>53.5<sub>(0.0)</sub></sup></sub> | <sub><sup>72.0<sub>(0.8)</sub></sup></sub> | <sub><sup>8.3<sub>(0.6)</sub></sup></sub> | <sub><sup>107.7<sub>(2.6)</sub></sup></sub> | <sub><sup>37.4<sub>(0.4)</sub></sup></sub> | 57.75M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-moee/7b3b466e/seed-0/2021-05-28_15-32-44/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-moee/7b3b466e/seed-0/2021-05-28_15-32-44/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/querydsegments-train-full-moee/7b3b466e/seed-0/2021-05-28_15-32-44/summary-seed-0_seed-1_seed-2.json) |
| CE    | t2v  | <sub><sup>19.2<sub>(0.1)</sub></sup></sub> | <sub><sup>40.8<sub>(1.6)</sub></sup></sub> | <sub><sup>49.4<sub>(1.0)</sub></sup></sub> | <sub><sup>68.7<sub>(0.5)</sub></sup></sub> | <sub><sup>11.0<sub>(1.0)</sub></sup></sub> | <sub><sup>125.0<sub>(4.7)</sub></sup></sub> | <sub><sup>33.8<sub>(0.6)</sub></sup></sub> | 30.82M |[config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-ce/0d1b703c/seed-0/2021-05-28_15-26-57/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-ce/0d1b703c/seed-0/2021-05-28_15-26-57/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/querydsegments-train-full-ce/0d1b703c/seed-0/2021-05-28_15-26-57/summary-seed-0_seed-1_seed-2.json) |
| HowTo100m S3D | v2t  | <sub><sup>7.2<sub>(0.0)</sub></sup></sub> | <sub><sup>15.1<sub>(0.0)</sub></sup></sub> | <sub><sup>19.5<sub>(0.0)</sub></sup></sub> | <sub><sup>34.3<sub>(0.0)</sub></sup></sub> | <sub><sup>160.0<sub>(0.0)</sub></sup></sub> | <sub><sup>361.4<sub>(0.0)</sub></sup></sub> | <sub><sup>12.9<sub>(0.0)</sub></sup></sub> | 1 | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-mnnet/1404fc28/seed-0/2021-05-28_16-38-32/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-mnnet/1404fc28/seed-0/2021-05-28_16-38-32/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/querydsegments-train-full-mnnet/1404fc28/seed-0/2021-05-28_16-38-32/summary-seed-0_seed-1_seed-2.json) |
| CE - P,CG | v2t  | <sub><sup>20.8<sub>(0.7)</sub></sup></sub> | <sub><sup>43.8<sub>(1.2)</sub></sup></sub> | <sub><sup>53.2<sub>(0.8)</sub></sup></sub> | <sub><sup>72.6<sub>(1.1)</sub></sup></sub> | <sub><sup>8.3<sub>(0.6)</sub></sup></sub> | <sub><sup>102.6<sub>(2.9)</sub></sup></sub> | <sub><sup>36.5<sub>(0.7)</sub></sup></sub> | 57.75M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-moee/7b3b466e/seed-0/2021-05-28_15-32-44/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-moee/7b3b466e/seed-0/2021-05-28_15-32-44/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/querydsegments-train-full-moee/7b3b466e/seed-0/2021-05-28_15-32-44/summary-seed-0_seed-1_seed-2.json) |
| CE    | v2t  | <sub><sup>18.5<sub>(0.5)</sub></sup></sub> | <sub><sup>40.1<sub>(0.6)</sub></sup></sub> | <sub><sup>49.5<sub>(0.2)</sub></sup></sub> | <sub><sup>69.0<sub>(0.6)</sub></sup></sub> | <sub><sup>11.0<sub>(0.0)</sub></sup></sub> | <sub><sup>112.1<sub>(4.3)</sub></sup></sub> | <sub><sup>33.2<sub>(0.4)</sub></sup></sub> | 30.82M |[config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-ce/0d1b703c/seed-0/2021-05-28_15-26-57/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-ce/0d1b703c/seed-0/2021-05-28_15-26-57/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/querydsegments-train-full-ce/0d1b703c/seed-0/2021-05-28_15-26-57/summary-seed-0_seed-1_seed-2.json) |
