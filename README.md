# Fake Faces in the Wild (FFW) dataset

This repository contains the download code for the FFW dataset as introduced in the following publication:
A. Khodabakhsh, R. Raghavendra, K. Raja, P. Wasnik, C. Busch, “Fake Face Detection Methods: Can They Be Generalized?”, BIOSIG, 2018.
The videos are >=480p, without audio, 30fps, avi files (matching light compression in FaceForensics dataset [2]) categorized as follows:

* FakeApp: 50 videos, Minimum length = ~3 sec
* Face_Head: 50 videos, Minimum length = ~2.5 sec
  * Head CGI: 15 videos
  * Face replacement: 15 videos
  * Face Only CGI: 7 videos
  * Head Only CGI: 8 videos
  * Part of face: 5 videos
* CGI: 50 videos, Minimum length = ~4 sec

In the `all_videos.csv` file, the first column is the video ID, while the second and the third are the start and end times in seconds, respectively. The fourth column, if not empty, indicates which part of the screen the fake face is on. The last column describes the category.

## Instructions

Drag and drop the list file on download.[bat|sh] for downloading the videos.

Requires the following (in path):
* [python](https://www.python.org/downloads/)
* [ffmpeg](https://ffmpeg.org/download.html)
* [youtube-dl](http://rg3.github.io/youtube-dl/download.html) (.exe provided)

The download and cut process may take many hours to complete. Some of the videos may be unavailable in your country, removed by the owner, or YouTube at the download time.

## contact

Please feel free to contact me if you have any questions or face any issues.

Ali Khodabakhsh, [ali.khodabakhsh@gmail.com](mailto:ali.khodabakhsh@gmail.com)

The code is also available at [http://ali.khodabakhsh.org/ffw/](http://ali.khodabakhsh.org/ffw/) for download

---
```
[1] A. Khodabakhsh, R. Raghavendra, K. Raja, P. Wasnik, C. Busch, “Fake Face Detection Methods: Can They Be Generalized?”, BIOSIG, 2018.

[2] Rössler, Andreas, et al. "FaceForensics: A Large-scale Video Dataset for Forgery Detection in Human Faces." arXiv preprint arXiv:1803.09179, 2018.
```
