from mutagen.mp3 import MP3
import mutagen
from mutagen.wave import WAVE
from PIL import Image
from pathlib import Path
from moviepy import editor
from moviepy.editor import *
import os
from datetime import datetime

#Pre requisites
dname = "F:/certifications/IIITH-AIML/research/imagen/banner/"
folder = os.path.join(dname, datetime.now().strftime('%Y-%m-%d'))

#audio_path = dname+"news-audio.mp3"
audio_path = folder+"/text-speach.mp3"
audio2_path = dname+"/news-audio.mp3"
video_path = folder+"/todays-headlines.mp4"
folder_path = folder
full_audio_path = os.path.join(audio_path)
full_video_path = os.path.join(video_path)

# Reading in the mp3 that we got from gTTS

song = MP3(audio_path)
audio_length = round(song.info.length)
#audio_length = 26
print('audio length: ', audio_length)

print('Creating a video from images in the folder: ', folder)

# Globbing the images and Stitching it to for the gif
path_images = Path(folder+"/dup/")

images = list(path_images.glob('*.png'))
#print(images[0])

image_list = list()

for image_name in images:
    #image = Image.open(image_name).resize((1080, 1920), Image.LANCZOS)
    image = Image.open(image_name).resize((1280, 800), Image.LANCZOS)
    image_list.append(image)

#Checking Audio length

length_audio = audio_length
duration = int(length_audio / len(image_list)) * 1000
print(duration)

#Creating Gif
image_list[0].save(os.path.join(folder_path,"temp.gif"),
                   save_all=True,
                   append_images=image_list[1:],
                   duration=duration)

# Creating the video using the gif and the audio file
video = editor.VideoFileClip(os.path.join(folder_path,"temp.gif"))
print('done video')

audio = editor.AudioFileClip(audio_path)
back_music = editor.AudioFileClip(audio2_path)
#back_music = back_music.subclip(0, int(audio.duration)) 
newclip = back_music.volumex(0.4)
composit_audioclip = CompositeAudioClip([audio, newclip])
print('done audio')

final_video = video.set_audio(composit_audioclip)
print('Set Audio and writing')

final_video.set_fps(30)
final_video.write_videofile(full_video_path)
#final_video.close()