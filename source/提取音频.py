from moviepy.editor import *

vedio = VideoFileClip('1.flv')

audio = vedio.audio

audio.write_audiofile('阿婆说.mp3')
