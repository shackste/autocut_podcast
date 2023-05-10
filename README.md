# Automatic Podcast Cutting

This repo provides python code for automatic cutting of podcast episodes.
The code was build for podcasts recorded using zoom with audio saved separately as a m4a file.
The cut.py script takes the m4a file and cuts it into chunks of less than 60 minutes each (mp3).
These chunks should then be audio enhanced, e. g. using https://podcast.adobe.com/Enhance.
Then, the combine.py script recombines the chunks into a single mp3 file, which is then layed over the video recording.
Finally, using the episodes.py script and a list of start and end times, the video is cut into episodes and overlayed with a jingle and logo at the beginning and end of each episode.

## Requirements
### ffmpeg
The scripts uses command line calls of ffmpeg to cut and combine the audio and video files.

## Installation

Simply download and run the scripts

OR

```
pip install git+https://github.com/shackste/autocut_podcast

python
>>> import autocut_podcast as ap
```

## Usage
### 1. Record
Record a podcast using zoom and save the audio_files and video_file separately.

### 2. Cut the audio files into chunks
Required for recordings longer than 60 minutes (maximum file size to Enhance audio).
```
python cut.py <audio_file>

-> chunk_0.mp3, chunk_1.mp3, ...
```
OR
```
ap.cut.cut("audio_file.m4a")
```

Best practice is to cut tracks for different persons individually.
(TODO: autotamize combining the tracks of different persons

### 3. Enhance the audio chunks

Use https://podcast.adobe.com/Enhance to enhance the audio chunks.
```
-> "chunk_0 (enhanced).mp3", "chunk_1 (enhanced).mp3", ...
```
### 4. Combine the audio chunks
```
python combine.py <number of chunks> <video_file>

-> final_output_file.mp4
```
OR
```
ap.combine.combine(<number of chunks>, "video_file.mp4", final_output_file=<enhanced_video_file>)
```

### 5. Cut the video into episodes

Given a list of start and end times in seconds, the enhanced video is cut into episodes, with intro and outro video added at beginning and end of each episode.

```

python episodes.py <enhanced_video_file> <episode_times>

-> episode_0.mp4, episode_1.mp4, ...

episode_times = "start,end|start,end|..."
```


OR

```
ap.episodes.episodes("enhanced_video_file.mp4", [[start,end], [start,end], ...], intro_file=<intro_file>, outro_file=<outro_file>

-> episode_0.mp4, episode_1.mp4, ...
```