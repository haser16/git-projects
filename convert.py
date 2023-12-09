import moviepy.editor as mp


clip = mp.VideoFileClip('video.avi')
clip.write_videofile('video.mp4')


# Supported video formats (.mp4, .avi, .webm, .gif)
