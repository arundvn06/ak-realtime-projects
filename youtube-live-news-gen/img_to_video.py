from mutagen.mp3 import MP3
import mutagen
from mutagen.wave import WAVE
from PIL import Image
from pathlib import Path
from moviepy import editor
from moviepy.editor import *
import os
from datetime import datetime


def create_video(images_path, audio_fname, bg_audio_fname, video_fname):
    
    # Reading in the mp3 that we got from gTTS
    song = MP3(audio_fname)
    
    audio_length = round(song.info.length)
    #audio_length = 26
    print('audio length: ', audio_length)

    print('Creating a video from images in the folder: ', images_path)

    # Globbing the images and Stitching it to for the gif
    path_images = Path(images_path)

    images = list(path_images.glob('*.png'))
    #print(images[0])

    image_list = list()

    for image_name in images:
        image = Image.open(image_name).resize((1280, 800), Image.LANCZOS)
        image_list.append(image)

    #Checking Audio length

    length_audio = audio_length
    duration = int(length_audio / len(image_list)) * 1000
    print(duration)

    #Creating Gif
    image_list[0].save(os.path.join(images_path,"temp.gif"),
                       save_all=True,
                       append_images=image_list[1:],
                       duration=duration)

    # Creating the video using the gif and the audio file
    video = editor.VideoFileClip(os.path.join(images_path,"temp.gif"))
    print('done video')

    audio = editor.AudioFileClip(audio_fname)
    back_music = editor.AudioFileClip(bg_audio_fname)
    #back_music = back_music.subclip(0, int(audio.duration)) 
    newclip = back_music.volumex(0.4)
    composit_audioclip = CompositeAudioClip([audio, newclip])
    print('done audio')

    final_video = video.set_audio(composit_audioclip)
    print('Set Audio and writing')

    final_video.set_fps(30)
    final_video.write_videofile(video_fname)
    #final_video.close()
    

def create_short_video(images_path, audio_fname, bg_audio_fname, video_fname):
    
    # Reading in the mp3 that we got from gTTS
    song = MP3(audio_fname)
    
    audio_length = round(song.info.length)
    #audio_length = 26
    print('audio length: ', audio_length)

    print('Creating a video from images in the folder: ', images_path)

    # Globbing the images and Stitching it to for the gif
    path_images = Path(images_path)

    images = list(path_images.glob('*.png'))
    images.sort(key=os.path.getmtime)
    #print(images[0])

    image_list = list()

    for image_name in images:
        image = Image.open(image_name).resize((800, 1200), Image.LANCZOS)
        image_list.append(image)

    #Checking Audio length

    length_audio = audio_length
    duration = int(length_audio / len(image_list)) * 1000
    print(duration)

    #Creating Gif
    image_list[0].save(os.path.join(images_path,"temp.gif"),
                       save_all=True,
                       append_images=image_list[1:],
                       duration=duration)

    # Creating the video using the gif and the audio file
    video = editor.VideoFileClip(os.path.join(images_path,"temp.gif"))
    print('done video')

    audio = editor.AudioFileClip(audio_fname)
    back_music = editor.AudioFileClip(bg_audio_fname)
    #back_music = back_music.subclip(0, int(audio.duration)) 
    newclip = back_music.volumex(0.4)
    composit_audioclip = CompositeAudioClip([audio, newclip])
    print('done audio')

    final_video = video.set_audio(composit_audioclip)
    print('Set Audio and writing')

    final_video.set_fps(30)
    final_video.write_videofile(video_fname)
    #final_video.close()
