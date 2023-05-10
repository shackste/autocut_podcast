import sys
import subprocess


def combine(num_chunks: int,
            video_file: str,
            combined_audio_file: str = 'combined.mp3',
            final_output_file: str = 'final_output.mp4') -> None:
    """ # TODO: allow for multiple audio tracks to be combined
    Combines multiple enhanced audio chunks into a single audio file, and then combines that audio file with a video file to create a final output file.

    Args:
        num_chunks (int): The number of audio chunks to be combined.
        video_file (str): The input video file to be combined with the audio.
        combined_audio_file (str, optional): The output audio file containing the combined audio chunks. Defaults to 'combined.mp3'.
        final_output_file (str, optional): The final output file with the combined audio and video. Defaults to 'final_output.mp4'.

    Returns:
        None, Files are saved to disk as combined_audio_file and final_output_file.

    Raises:
        subprocess.CalledProcessError: If an error occurs during the ffmpeg subprocess calls.
    """
    concat_files = " -i ".join([f'"chunk_{i} (enhanced).wav"' for i in range(num_chunks)])
    filter = "".join([f"[{i}:0]" for i in range(num_chunks)])
    filter += f"concat=n={num_chunks}:v=0:a=1[out]"
    command = f'ffmpeg -i {concat_files} -filter_complex "{filter}" -map "[out]" {combined_audio_file}'
    subprocess.call(command, shell=True)

    command = f"ffmpeg -i {video_file} -i {combined_audio_file} -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 {final_output_file}"
    subprocess.call(command, shell=True)

if __name__ == "__main__":
    num_chunks = int(sys.argv[1])
    video_file = sys.argv[2]
    combine(num_chunks, video_file)
