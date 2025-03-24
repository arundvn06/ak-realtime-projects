#Import the necessary libraries 
import cv2 
import numpy as np 
import os
from datetime import datetime
from PIL import Image

def resize_img(image, width, height):
    resized_image = cv2.resize(image, (width, height))
    return resized_image
    
def resize_with_aspect_ratio(image, width=None, height=None):
    # Get the original image dimensions
    h, w = image.shape[:2]

    # Calculate the aspect ratio
    aspect_ratio = w / h

    if width is None:
        # Calculate height based on the specified width
        new_height = int(height / aspect_ratio)
        resized_image = cv2.resize(image, (height, new_height))
    else:
        # Calculate width based on the specified height
        new_width = int(width * aspect_ratio)
        resized_image = cv2.resize(image, (new_width, width))

    return resized_image

dname = "F:/certifications/IIITH-AIML/research/imagen/banner/"
#folder = "2024-09-08"
folder = os.path.join(dname, datetime.now().strftime('%Y-%m-%d'))
print('Resizing images in the folder: ', folder)    

def change_image_color(dup_img_path, org_img_path): 
    img = Image.open(org_img_path)
    img = img.convert("RGB")
     
    d = img.getdata()
     
    new_image = []
    for item in d:
     
        # change all white (also shades of whites)
        # pixels to yellow
        if item[0] in list(range(200, 256)):
            new_image.append((255, 224, 100))
        else:
            new_image.append(item)
     
    # update image data
    img.putdata(new_image)
     
    # save new image
    img.save(dup_img_path)

for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder,filename))
    if img is not None:
        org_img_path = folder+"/"+filename
        dup_img_path = folder+"/dup/resize_"+filename
        # Load the image 
        image = cv2.imread(org_img_path)  

        # Sharpen the image using the Laplacian operator 
        #sharpened_image2 = cv2.Laplacian(image, cv2.CV_64FC4) 
        
        # Save the image 
        #cv2.imwrite(dup_img_path, sharpened_image2)
        
        # Resize the image with an aspect ratio
        resized_image = resize_img(image, 1080, 1920)
        
        image_gray=cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY) 
        image_rgb=cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB) 
        hsv = cv2.cvtColor(resized_image, cv2.COLOR_BGR2HSV)
        
        # Save the resized image
        cv2.imwrite(dup_img_path, image_gray)
        cv2.imwrite(folder+"/dup/rgb_"+filename, image_rgb)
        cv2.imwrite(folder+"/dup/hsv_"+filename, hsv)
        
        change_image_color(folder+"/dup/color_changed_"+filename, org_img_path)
        
        break

print('Resize completed')
