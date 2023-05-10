This repo provides python code for automatic cutting of podcast episodes.
The code assumes that the podcast is recorded using zoom and that the audio is saved separately as a m4a file.
The cut.py script takes the m4a file and cuts it into chunks of less than 60 minutes each (mp3).
These chunks should then be audio enhanced, e. g. using https://podcast.adobe.com/Enhance.
Then, the combine.py script recombines the chunks into a single mp3 file, which is then layed over the video recording.
Finally, using the episodes.py script and a list of start and end times, the video is cut into episodes and overlayed with a jingle and logo at the beginning and end of each episode.

## Requirements
### ffmpeg
The scripts use ffmpeg to cut and combine the audio and video files.
