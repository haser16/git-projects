from pytube import YouTube

video = YouTube("https://youtu.be/QNdYybI3Pgs")

video.streams.get_by_itag(itag=248).download(filename='video.mp4')
