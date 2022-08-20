# python module to perform operations on YouTube contents
from pytube import YouTube

# prompting user to input required URL
url = input("Enter URL of video: ")

# getting details of required video from youtube and access it using a variable video
video = YouTube(url)

# get maximum resolution available for the selected video
quality = video.streams.get_highest_resolution()

# showing user about video title and highest quality available
print('title: {}, file-size: {}, Resolution: {}'.format(video.captions, quality.filesize, quality.resolution))

# downloads the required video
quality.download()
