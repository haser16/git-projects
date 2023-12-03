import os

from moviepy.editor import AudioFileClip
from pytube import YouTube

list_music = (
    'https://youtu.be/bvGNTCfEV7o',
)

path = 'D:/sound'


def get_sound(urls, source_to_save):
    for url in urls:
        video_yt = YouTube(url, use_oauth=True)
        title = video_yt.title
        video_yt.streams.get_highest_resolution().download(output_path='sound/', filename=f'{title}.mp4')
        audio = AudioFileClip(f'sound/{title}.mp4', buffersize=20000)
        audio.write_audiofile(f'sound/{title}.mp3')
        os.remove(f'sound/{title}.mp4')
        os.replace(src=f'sound/{title}.mp3', dst=f'{source_to_save}/{title}.mp3')
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


if __name__ == '__main__':
    get_sound(urls=list_music, source_to_save=path)
