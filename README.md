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
wget http://www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/QuerYD/json_metadata-{version either v1 or v2}.zip
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

This work is supported by the EP-SRC (VisualAI EP/T028572/1 and DTA Studentship), and the Royal Academy of Engineering (DFR05420). We are gratefulto Sophia Koepke for her helpful comments and suggestions.


### 2nd Version of QuerYD retrieval results:

### QuerYD

### MODEL study on QUERYD

**Importance of the model**:

| Model | Task | R@1 | R@5 | R@10 | R@50 | MdR | MnR | Geom | params | Links |
| ----- | ---- | --- | --- | ---- | ---- | --- | --- | ----- | -- | -- |
| HowTo100m S3D | t2v  | <sub><sup>10.7<sub>(0.0)</sub></sup></sub> | <sub><sup>23.2<sub>(0.0)</sub></sup></sub> | <sub><sup>27.7<sub>(0.0)</sub></sup></sub> | <sub><sup>52.5<sub>(0.0)</sub></sup></sub> | <sub><sup>44.0<sub>(0.0)</sub></sup></sub> | <sub><sup>82.6<sub>(0.0)</sub></sup></sub> | <sub><sup>19.0<sub>(0.0)</sub></sup></sub> | 1 | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-mnnet/c3991baf/seed-0/2021-03-17_09-32-21/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-mnnet/c3991baf/seed-0/2021-03-17_09-32-21/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-mnnet/c3991baf/seed-0/2021-03-17_09-32-21/summary-seed-0_seed-1_seed-2.json) |
| CE - P,CG | t2v  | <sub><sup>10.5<sub>(0.3)</sub></sup></sub> | <sub><sup>31.7<sub>(0.2)</sub></sup></sub> | <sub><sup>45.1<sub>(0.2)</sub></sup></sub> | <sub><sup>73.9<sub>(1.0)</sub></sup></sub> | <sub><sup>14.5<sub>(0.7)</sub></sup></sub> | <sub><sup>43.1<sub>(1.9)</sub></sup></sub> | <sub><sup>24.6<sub>(0.2)</sub></sup></sub> | 57.75M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-moee/c3008757/seed-0/2021-03-17_09-32-21/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-moee/c3008757/seed-0/2021-03-17_09-32-21/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-moee/c3008757/seed-0/2021-03-17_09-32-21/summary-seed-0_seed-1_seed-2.json) |
| CE    | t2v  | <sub><sup>15.5<sub>(1.6)</sub></sup></sub> | <sub><sup>38.4<sub>(1.6)</sub></sup></sub> | <sub><sup>49.8<sub>(1.0)</sub></sup></sub> | <sub><sup>80.6<sub>(0.5)</sub></sup></sub> | <sub><sup>10.5<sub>(0.7)</sub></sup></sub> | <sub><sup>30.5<sub>(1.3)</sub></sup></sub> | <sub><sup>30.9<sub>(0.3)</sub></sup></sub> | 30.82M |[config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce/76fa1a77/seed-0/2021-03-17_09-32-21/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce/76fa1a77/seed-0/2021-03-17_09-32-21/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce/76fa1a77/seed-0/2021-03-17_09-32-21/summary-seed-0_seed-1_seed-2.json) |
| HowTo100m S3D | v2t  | <sub><sup>10.0<sub>(0.0)</sub></sup></sub> | <sub><sup>21.4<sub>(0.0)</sub></sup></sub> | <sub><sup>29.1<sub>(0.0)</sub></sup></sub> | <sub><sup>53.6<sub>(0.0)</sub></sup></sub> | <sub><sup>41.0<sub>(0.0)</sub></sup></sub> | <sub><sup>81.1<sub>(0.0)</sub></sup></sub> | <sub><sup>18.4<sub>(0.0)</sub></sup></sub> | 1 | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-mnnet/c3991baf/seed-0/2021-03-17_09-32-21/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-mnnet/c3991baf/seed-0/2021-03-17_09-32-21/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-mnnet/c3991baf/seed-0/2021-03-17_09-32-21/summary-seed-0_seed-1_seed-2.json) |
| CE - P,CG | v2t  | <sub><sup>11.5<sub>(1.1)</sub></sup></sub> | <sub><sup>31.9<sub>(1.4)</sub></sup></sub> | <sub><sup>46.0<sub>(0.2)</sub></sup></sub> | <sub><sup>74.4<sub>(2.4)</sub></sup></sub> | <sub><sup>13.5<sub>(0.7)</sub></sup></sub> | <sub><sup>41.8<sub>(1.8)</sub></sup></sub> | <sub><sup>25.6<sub>(0.8)</sub></sup></sub> | 57.75M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-moee/c3008757/seed-0/2021-03-17_09-32-21/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-moee/c3008757/seed-0/2021-03-17_09-32-21/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-moee/c3008757/seed-0/2021-03-17_09-32-21/summary-seed-0_seed-1_seed-2.json) |
| CE    | v2t  | <sub><sup>16.0<sub>(0.8)</sub></sup></sub> | <sub><sup>39.0<sub>(1.4)</sub></sup></sub> | <sub><sup>52.5<sub>(0.3)</sub></sup></sub> | <sub><sup>81.9<sub>(1.4)</sub></sup></sub> | <sub><sup>9.5<sub>(0.7)</sub></sup></sub> | <sub><sup>28.9<sub>(0.8)</sub></sup></sub> | <sub><sup>32.0<sub>(0.1)</sub></sup></sub> | 30.82M |[config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce/76fa1a77/seed-0/2021-03-17_09-32-21/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce/76fa1a77/seed-0/2021-03-17_09-32-21/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce/76fa1a77/seed-0/2021-03-17_09-32-21/summary-seed-0_seed-1_seed-2.json) |

The influence of different pretrained experts for the performance of the CE model trained on QuerYD is studied. The value and cumulative effect of different experts for scene clas-sification (SCENE), ambient sound classification (AUDIO),image classification (OBJECT), and action recognition (ACTION) are presented. PREV. denotes the experts used in the previous row.

| Experts | Task | R@1 | R@5 | R@10 | R@50 | MdR | MnR | Geom | params | Links |
| ----- | ---- | --- | --- | ---- | ---- | --- | --- | ----- | -- | -- |
| Scene    | t2v  | <sub><sup>10.9<sub>(nan)</sub></sup></sub> | <sub><sup>30.0<sub>(nan)</sub></sup></sub> | <sub><sup>41.8<sub>(nan)</sub></sup></sub> | <sub><sup>69.5<sub>(nan)</sub></sup></sub> | <sub><sup>18.0<sub>(nan)</sub></sup></sub> | <sub><sup>52.8<sub>(nan)</sub></sup></sub> | <sub><sup>23.9<sub>(nan)</sub></sup></sub> | 7.51M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene/c6290e2d/seed-0/2021-03-17_09-32-35/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene/c6290e2d/seed-0/2021-03-17_09-32-35/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce-only-scene/c6290e2d/seed-0/2021-03-17_09-32-35/summary-seed-0_seed-1_seed-2.json) |
| Prev. + Audio    | t2v  | <sub><sup>11.4<sub>(0.7)</sub></sup></sub> | <sub><sup>31.1<sub>(1.2)</sub></sup></sub> | <sub><sup>42.5<sub>(1.6)</sub></sup></sub> | <sub><sup>72.4<sub>(1.3)</sub></sup></sub> | <sub><sup>15.5<sub>(1.5)</sub></sup></sub> | <sub><sup>44.7<sub>(1.0)</sub></sup></sub> | <sub><sup>24.7<sub>(0.3)</sub></sup></sub> | 17.25M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio/cc96d84e/seed-0/2021-03-17_09-32-36/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio/cc96d84e/seed-0/2021-03-17_09-32-36/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce-only-scene-audio/cc96d84e/seed-0/2021-03-17_09-32-36/summary-seed-0_seed-1_seed-2.json) |
| Prev. + Inst    | t2v  | <sub><sup>15.2<sub>(2.6)</sub></sup></sub> | <sub><sup>38.1<sub>(0.5)</sub></sup></sub> | <sub><sup>50.9<sub>(0.6)</sub></sup></sub> | <sub><sup>81.5<sub>(1.1)</sub></sup></sub> | <sub><sup>10.0<sub>(0.0)</sub></sup></sub> | <sub><sup>30.5<sub>(0.4)</sub></sup></sub> | <sub><sup>30.9<sub>(1.4)</sub></sup></sub> | 24.63M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio-inst/d17959ed/seed-0/2021-03-17_09-32-40/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio-inst/d17959ed/seed-0/2021-03-17_09-32-40/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce-only-scene-audio-inst/d17959ed/seed-0/2021-03-17_09-32-40/summary-seed-0_seed-1_seed-2.json) |
| Prev. + R2P1D    | t2v  | <sub><sup>16.1<sub>(1.6)</sub></sup></sub> | <sub><sup>39.3<sub>(1.9)</sub></sup></sub> | <sub><sup>50.2<sub>(0.9)</sub></sup></sub> | <sub><sup>81.0<sub>(0.8)</sub></sup></sub> | <sub><sup>10.0<sub>(1.0)</sub></sup></sub> | <sub><sup>30.1<sub>(1.2)</sub></sup></sub> | <sub><sup>31.7<sub>(1.1)</sub></sup></sub> | 30.82M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio-inst-r2p1d/4bd85c1c/seed-0/2021-03-17_09-47-18/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio-inst-r2p1d/4bd85c1c/seed-0/2021-03-17_09-47-18/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce-only-scene-audio-inst-r2p1d/4bd85c1c/seed-0/2021-03-17_09-47-18/summary-seed-0_seed-1_seed-2.json) |
| Scene    | v2t  | <sub><sup>9.8<sub>(nan)</sub></sup></sub> | <sub><sup>29.5<sub>(nan)</sub></sup></sub> | <sub><sup>41.6<sub>(nan)</sub></sup></sub> | <sub><sup>70.9<sub>(nan)</sub></sup></sub> | <sub><sup>16.0<sub>(nan)</sub></sup></sub> | <sub><sup>51.4<sub>(nan)</sub></sup></sub> | <sub><sup>22.9<sub>(nan)</sub></sup></sub> | 7.51M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene/c6290e2d/seed-0/2021-03-17_09-32-35/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene/c6290e2d/seed-0/2021-03-17_09-32-35/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce-only-scene/c6290e2d/seed-0/2021-03-17_09-32-35/summary-seed-0_seed-1_seed-2.json) |
| Prev. + Audio    | v2t  | <sub><sup>11.3<sub>(0.5)</sub></sup></sub> | <sub><sup>30.3<sub>(0.9)</sub></sup></sub> | <sub><sup>42.2<sub>(1.3)</sub></sup></sub> | <sub><sup>73.7<sub>(1.5)</sub></sup></sub> | <sub><sup>16.0<sub>(1.0)</sub></sup></sub> | <sub><sup>42.9<sub>(0.8)</sub></sup></sub> | <sub><sup>24.3<sub>(0.1)</sub></sup></sub> | 17.25M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio/cc96d84e/seed-0/2021-03-17_09-32-36/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio/cc96d84e/seed-0/2021-03-17_09-32-36/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce-only-scene-audio/cc96d84e/seed-0/2021-03-17_09-32-36/summary-seed-0_seed-1_seed-2.json) |
| Prev. + Inst.    | v2t  | <sub><sup>15.6<sub>(0.2)</sub></sup></sub> | <sub><sup>37.7<sub>(0.0)</sub></sup></sub> | <sub><sup>52.8<sub>(0.2)</sub></sup></sub> | <sub><sup>82.4<sub>(0.8)</sub></sup></sub> | <sub><sup>9.0<sub>(0.0)</sub></sup></sub> | <sub><sup>29.0<sub>(0.5)</sub></sup></sub> | <sub><sup>31.4<sub>(0.1)</sub></sup></sub> | 24.63M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio-inst/d17959ed/seed-0/2021-03-17_09-32-40/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio-inst/d17959ed/seed-0/2021-03-17_09-32-40/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce-only-scene-audio-inst/d17959ed/seed-0/2021-03-17_09-32-40/summary-seed-0_seed-1_seed-2.json) |
| Prev. + R2P1D    | v2t  | <sub><sup>15.8<sub>(0.7)</sub></sup></sub> | <sub><sup>39.7<sub>(1.6)</sub></sup></sub> | <sub><sup>52.5<sub>(0.2)</sub></sup></sub> | <sub><sup>82.2<sub>(1.1)</sub></sup></sub> | <sub><sup>9.3<sub>(0.6)</sub></sup></sub> | <sub><sup>28.6<sub>(0.8)</sub></sup></sub> | <sub><sup>32.0<sub>(0.0)</sub></sup></sub> | 30.82M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio-inst-r2p1d/4bd85c1c/seed-0/2021-03-17_09-47-18/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/queryd-train-full-ce-only-scene-audio-inst-r2p1d/4bd85c1c/seed-0/2021-03-17_09-47-18/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/queryd-train-full-ce-only-scene-audio-inst-r2p1d/4bd85c1c/seed-0/2021-03-17_09-47-18/summary-seed-0_seed-1_seed-2.json) |


### For QuerYDSegments updated results are

### MODEL study on QUERYDSEGMENTS

**Importance of the model**:

| Model | Task | R@1 | R@5 | R@10 | R@50 | MdR | MnR | Geom | params | Links |
| ----- | ---- | --- | --- | ---- | ---- | --- | --- | ----- | -- | -- |
| HowTo100m S3D | t2v  | <sub><sup>7.7<sub>(0.0)</sub></sup></sub> | <sub><sup>16.4<sub>(0.0)</sub></sup></sub> | <sub><sup>20.7<sub>(0.0)</sub></sup></sub> | <sub><sup>35.3<sub>(0.0)</sub></sup></sub> | <sub><sup>142.0<sub>(0.0)</sub></sup></sub> | <sub><sup>399.0<sub>(0.0)</sub></sup></sub> | <sub><sup>13.8<sub>(0.0)</sub></sup></sub> | 1 | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-mnnet/f530d25b/seed-0/2021-03-15_16-55-23/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-mnnet/f530d25b/seed-0/2021-03-15_16-55-23/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/querydsegments-train-full-mnnet/f530d25b/seed-0/2021-03-15_16-55-23/summary-seed-0_seed-1_seed-2.json) |
| CE - P,CG | t2v  | <sub><sup>19.0<sub>(0.7)</sub></sup></sub> | <sub><sup>41.1<sub>(0.6)</sub></sup></sub> | <sub><sup>50.7<sub>(0.7)</sub></sup></sub> | <sub><sup>70.8<sub>(0.6)</sub></sup></sub> | <sub><sup>10.3<sub>(0.6)</sub></sup></sub> | <sub><sup>124.6<sub>(3.8)</sub></sup></sub> | <sub><sup>34.1<sub>(0.6)</sub></sup></sub> | 57.75M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-moee/aa409ae1/seed-0/2021-03-15_16-38-13/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-moee/aa409ae1/seed-0/2021-03-15_16-38-13/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/querydsegments-train-full-moee/aa409ae1/seed-0/2021-03-15_16-38-13/summary-seed-0_seed-1_seed-2.json) |
| CE    | t2v  | <sub><sup>18.1<sub>(1.0)</sub></sup></sub> | <sub><sup>39.1<sub>(1.3)</sub></sup></sub> | <sub><sup>48.5<sub>(1.8)</sub></sup></sub> | <sub><sup>69.2<sub>(1.3)</sub></sup></sub> | <sub><sup>11.7<sub>(1.5)</sub></sup></sub> | <sub><sup>130.7<sub>(5.9)</sub></sup></sub> | <sub><sup>32.5<sub>(1.1)</sub></sup></sub> | 30.82M |[config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-ce/90f47d44/seed-0/2021-03-15_16-13-50/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-ce/90f47d44/seed-0/2021-03-15_16-13-50/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/querydsegments-train-full-ce/90f47d44/seed-0/2021-03-15_16-13-50/summary-seed-0_seed-1_seed-2.json) |
| HowTo100m S3D | v2t  | <sub><sup>7.6<sub>(0.0)</sub></sup></sub> | <sub><sup>16.3<sub>(0.0)</sub></sup></sub> | <sub><sup>20.9<sub>(0.0)</sub></sup></sub> | <sub><sup>34.8<sub>(0.0)</sub></sup></sub> | <sub><sup>162.0<sub>(0.0)</sub></sup></sub> | <sub><sup>423.8<sub>(0.0)</sub></sup></sub> | <sub><sup>13.7<sub>(0.0)</sub></sup></sub> | 1 | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-mnnet/f530d25b/seed-0/2021-03-15_16-55-23/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-mnnet/f530d25b/seed-0/2021-03-15_16-55-23/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/querydsegments-train-full-mnnet/f530d25b/seed-0/2021-03-15_16-55-23/summary-seed-0_seed-1_seed-2.json) |
| CE - P,CG | v2t  | <sub><sup>18.7<sub>(0.6)</sub></sup></sub> | <sub><sup>40.4<sub>(1.4)</sub></sup></sub> | <sub><sup>49.8<sub>(0.7)</sub></sup></sub> | <sub><sup>70.7<sub>(0.4)</sub></sup></sub> | <sub><sup>10.3<sub>(0.6)</sub></sup></sub> | <sub><sup>120.2<sub>(2.5)</sub></sup></sub> | <sub><sup>33.5<sub>(0.7)</sub></sup></sub> | 57.75M | [config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-moee/aa409ae1/seed-0/2021-03-15_16-38-13/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-moee/aa409ae1/seed-0/2021-03-15_16-38-13/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/querydsegments-train-full-moee/aa409ae1/seed-0/2021-03-15_16-38-13/summary-seed-0_seed-1_seed-2.json) |
| CE    | v2t  | <sub><sup>18.3<sub>(1.1)</sub></sup></sub> | <sub><sup>38.3<sub>(1.4)</sub></sup></sub> | <sub><sup>48.0<sub>(1.4)</sub></sup></sub> | <sub><sup>69.0<sub>(1.3)</sub></sup></sub> | <sub><sup>12.3<sub>(1.2)</sub></sup></sub> | <sub><sup>125.9<sub>(5.9)</sub></sup></sub> | <sub><sup>32.3<sub>(0.9)</sub></sup></sub> | 30.82M |[config](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-ce/90f47d44/seed-0/2021-03-15_16-13-50/config.json), [model](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/models/querydsegments-train-full-ce/90f47d44/seed-0/2021-03-15_16-13-50/trained_model.pth), [log](http:/www.robots.ox.ac.uk/~vgg/research/collaborative-experts/data/log/querydsegments-train-full-ce/90f47d44/seed-0/2021-03-15_16-13-50/summary-seed-0_seed-1_seed-2.json) |

