import os
import sys
import subprocess

def create_episodes(video_file: str,
                    episode_intervals: list,
                    intro_file: str = "logo_intro.mov",
                    outro_file: str = "logo_outro.mov") -> None:
    """
    Creates individual episodes from video file by extracting specific time intervals and concatenating them with an intro and outro video.

    Args:
        video_file (str): The input video file from which episodes will be extracted.
        episode_intervals (list): A list of time intervals from the input file, represented as a list of lists of integers where each sublist contains two integers representing the start and end time of an episode, respectively. The times should be in seconds.
        intro_file (str, optional): The intro video file to be concatenated with each episode. Defaults to "logo_intro.mov".
        outro_file (str, optional): The outro video file to be concatenated with each episode. Defaults to "logo_outro.mov".

    Returns:
        None, Files are saved to disk as episode_0.mp4, episode_1.mp4, etc.

    Raises:
        subprocess.CalledProcessError: If an error occurs during the ffmpeg subprocess calls.
    """
    for i, (start_time, end_time) in enumerate(episode_intervals):
        episode_duration = end_time - start_time
        temp_file = f"temp_{i}.mp4"
        episode_file = f"episode_{i}.mp4"

        command = f"ffmpeg -ss {start_time} -t {episode_duration} -i {video_file} -c copy {temp_file}"
        subprocess.call(command, shell=True)

        command = f'ffmpeg -i {intro_file} -i {temp_file} -i {outro_file} -filter_complex "[0:v][0:a][1:v][1:a][2:v][2:a]concat=n=3:v=1:a=1 [v] [a]" -map "[v]" -map "[a]" {episode_file}'

        print("\n", command, "\n")
        subprocess.call(command, shell=True)

        # Remove temporary file
        os.remove(temp_file)

def create_interval_string(intervals: list) -> str:
    """
    transforms a list of time intervals ["hh:mm:ss - hh:mm:ss", ...]
    into a string of intervals "start,end|start,end|...",
    where start and end are in seconds
    """
    interval_string = ""
    for interval in intervals:
        start, end = interval.split(" - ")
        start = start.split(":")
        end = end.split(":")
        start = int(start[0]) * 3600 + int(start[1]) * 60 + int(start[2])
        end = int(end[0]) * 3600 + int(end[1]) * 60 + int(end[2])
        interval_string += f"{start},{end}|"
    return interval_string[:-1]

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python episodes.py /path/to/video_file episode_intervals\n episode_intervals: 'start_time,end_time|start_time,end_time|...'")
        sys.exit(1)

    video_file = sys.argv[1]
    string = sys.argv[2]
    episode_intervals = [[int(num) for num in substr.split(',')]
                                   for substr in string.split('|')]
    create_episodes(video_file, episode_intervals)
