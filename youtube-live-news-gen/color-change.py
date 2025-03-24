#Import the necessary libraries 
import cv2 
import numpy as np 
import os
from datetime import datetime
from PIL import Image

dname = "F:/certifications/IIITH-AIML/research/imagen/banner/"
folder = os.path.join(dname, datetime.now().strftime('%Y-%m-%d'))
print('Updating images in the folder: ', folder)

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

def add_mask(dname, image):

    # Convert to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define lower and uppper limits of what we call "white-ish"
    sensitivity = 19
    lower_white = np.array([0, 0, 255 - sensitivity])
    upper_white = np.array([255, sensitivity, 255])

    # Create mask to only select white
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # Change image to grey where we found white
    image2 = image.copy()
    image2[mask > 0] = (170, 170, 170)

    # Create new rectangular mask that is white on black background
    x,y,w,h = 33,100,1400,1000
    x,y,w,h = 33,100,1000,1700
    mask2 = np.zeros_like(image)
    cv2.rectangle(mask2, (x,y), (x+w,y+h), (255, 255, 255), -1)

    # invert mask
    mask2_inv = 255 - mask2

    # apply mask to image
    image_masked = cv2.bitwise_and(image, mask2)

    # apply inverted mask to image2
    image2_masked = cv2.bitwise_and(image2, mask2_inv)

    # add together
    result = cv2.add(image_masked, image2_masked)

    # save results
    #cv2.imwrite(dname+'result.jpg', result)

    #cv2.imshow('result', result)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return result

def change_image_color(org_img_path, dup_img_path): 
    img = Image.open(org_img_path)
    img = img.convert("RGB")
     
    d = img.getdata()
     
    new_image = []
    for item in d:
     
        # change all white (also shades of whites)
        # pixels to yellow
        if item[0] in list(range(0, 100)):
            new_image.append((255, 245, 255))
        elif item[0] in list(range(250, 256)):
            new_image.append((0, 0, 0))
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
        dup_img_path = folder+"/dup/"+filename
        # Load the image 
        image = cv2.imread(org_img_path)  
        
        # Resize the image with an aspect ratio; 
        # this is not needed as we doing it as part of creating video
        #resized_image = resize_with_aspect_ratio(image, width=1080)
        #resized_image = resize_with_aspect_ratio(image, height=1920)
        #resized_image = resize_img(image, 1080, 1920)

        # Sharpen the image using the Laplacian operator 
        #sharpened_image = cv2.Laplacian(resized_image, cv2.CV_64F)
        
        #masked
        #final_image = add_mask(folder+"/dup/", image)
        
        #Save the image 
        #cv2.imwrite(dup_img_path, image)
        
        change_image_color(org_img_path, dup_img_path)
print('Update completed')