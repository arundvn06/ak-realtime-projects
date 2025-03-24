#Import the necessary libraries 
import cv2 
import numpy as np 
import os
from datetime import datetime
from PIL import Image

import img_to_video as im2v
import youtube.simple_youtube as yt

dname = "F:/certifications/IIITH-AIML/research/imagen/banner/"
folder = os.path.join(dname, datetime.now().strftime('%Y-%m-%d'))
org_imgs = folder + "/youtube_trends/original/"
crop_imgs = folder + "/youtube_trends/croped/"

#youtube trends
video_fname = folder + "/youtube_trends/youtube_trends.mp4"
youtube_dir = dname + "/youtube/"
bg1_audio_fname = youtube_dir + "/bg1.mp3"
bg2_audio_fname = youtube_dir + "/bg2.mp3"

def crop_images(org_img_folder, crop_img_folder):
    for filename in os.listdir(org_img_folder):
        img = cv2.imread(os.path.join(org_img_folder, filename))
        if img is not None:
            #org_img_path = org_img_folder+"/"+filename
            crop_img_path = crop_img_folder+"/"+filename
            
            #Save the image 
            crop = img[0:1000, 100:1000]
            cv2.imwrite(crop_img_path, crop)

crop_images(org_imgs, crop_imgs)        
print('Image Cropping completed')

#create video from images and text generated above
im2v.create_short_video(crop_imgs, bg1_audio_fname, bg2_audio_fname, video_fname)

    
#upload video to youtube
yt.upload_youtube_trends(youtube_dir, video_fname, crop_imgs+"/trending.png")