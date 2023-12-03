from pytube import YouTube
from moviepy.editor import AudioFileClip


def get_sound(url, source_to_save=None):
    video_yt = YouTube(url)
    title = video_yt.title
    video_yt.streams.get_highest_resolution().download(output_path=f'sound/')


if __name__ == '__main__':
    get_sound(url='https://dzen.ru/video/watch/5d9329d4f73d9d00b05cced8')
