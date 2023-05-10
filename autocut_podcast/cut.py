import sys
import subprocess


def cut(input_file: str, max_chunk_duration: int = 59 * 60) -> None:
    """
    Cuts an audio file into smaller chunks of a specified maximum duration.

    Args:
        input_file (str): The input audio file to be cut.
        max_chunk_duration (int, optional): The maximum duration of each chunk, in seconds. Defaults to 59 minutes.

    Returns:
        None, Files are saved to disk as chunk_0.mp3, chunk_1.mp3, etc.

    Raises:
        subprocess.CalledProcessError: If an error occurs during the ffmpeg or ffprobe subprocess calls.
    """
    duration = float(
        subprocess.check_output(
            f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {input_file}",
            shell=True,
        )
    )

    num_chunks = int(duration // max_chunk_duration) + 1

    for i in range(num_chunks):
        start_time = i * max_chunk_duration
        output_file = f"chunk_{i}.mp3"
        command = f"ffmpeg -ss {start_time} -t {max_chunk_duration} -i {input_file} -acodec libmp3lame -ar 44100 -ab 128k {output_file}"
        subprocess.call(command, shell=True)

if __name__ == "__main__":
    input_file = sys.argv[1]
    cut(input_file)
