import os
import itertools
from datetime import datetime
from serpapi import GoogleSearch
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import PIL

import text_to_speach as t2s
import img_to_video as im2v
import youtube.simple_youtube as yt

dname = "F:/certifications/IIITH-AIML/research/imagen/banner/"
folder = os.path.join(dname, datetime.now().strftime('%Y-%m-%d'))

ai_mask_img = dname + "/youtube/ai_mask.png"
fonts_path = dname + "/fonts"
w_trends_folder = folder + "/wtrends/"
w_trends_wc_fname = w_trends_folder + "w_trends_wc.png"
w_trends_fname = w_trends_folder + "w_trends.png"

#world headlines paths
w_hl_folder = folder + "/wheadlines/"
w_hl_img_path = w_hl_folder + "/img/"
w_hl_fname = w_hl_folder + "w_headlines.png"
w_hl_wc_fname = w_hl_folder + "w_headlines_wc.png"
w_hl_aud_fname = w_hl_folder + "w_headlines.mp3"
bg_audio_fname = dname+"/news-audio.mp3"
video_fname = w_hl_folder+"/todays-headlines.mp4"

youtube_dir = dname + "/youtube/"
headlines_bg_img = youtube_dir + "/top_headlines_bg.png"
news_files = dname + "/news/"
 

def get_world_trends_headlines():

    params = {
      "q": "top trending international news today",
      "location": "India",
      "hl": "en",
      "gl": "in",
      "api_key": "d1ddc1303a097bb484d60afa6778b5f1fb965ce7f0b78e7037ccce56122c112c"
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    titles = ['World', 'WORLD NEWS', 'TOP Headlines', 'World News', 'Top News', 'World', "International News"]
    trends = []
    headlines = []
    for result in results['related_questions']:
      #print("question: "+result['question'] + " title:" +result['title'])
      title = result['title']
      if title == 'top trends':
        trends = result['list']
      elif title in titles:
        headlines.append(result['list'])
        
    return trends, headlines


#To create wordcloud
def create_wordcloud(list, mask_fname, fname):
    comment_words = ''
    stopwords = set(STOPWORDS)

    # iterate through the list
    for val in list:
        # typecaste each val to string
        val = str(val)

        # split the value
        tokens = val.split()

        # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        comment_words += " ".join(tokens)+" "

    #load mask image to create wordcloud in a specific shape. Image should be white BgColor and black FgColor
    maskable_image = np.array(Image.open(mask_fname))

    #create wordcloud with all props
    wc = WordCloud(background_color = 'black', mask = maskable_image, contour_width = 2, stopwords = stopwords,
         contour_color = 'black', colormap = 'cool', width = 1280, height = 720).generate(comment_words)
         
    #Save wordcloud image to a file
    wc.to_file(fname)
         
    #plt.figure(figsize = (8, 8), facecolor = None)
    #plt.axis("off")
    #plt.tight_layout(pad = 0)
    #plt.title("Today Top Trends")
    #plt.imshow(wc)


    #Add header to the image

    # Open an Image
    img = Image.open(fname)

    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)

    # Custom font style and font size
    #myFont = ImageFont.truetype('FreeMono.ttf', 65)
    font = ImageFont.load_default()
    myFont = ImageFont.truetype(fonts_path+'/atop-font/Atop-R99O3.ttf', 80)

    # Add Text to an image
    I1.text((200, 35), "WORLD HEADLINES", font=myFont, fill =(255, 0, 0))

    # Save the edited image
    img.save(fname)


#To create an image for trends content
def create_trends_image(fname, fonts_path, trends):
	
    # creating a image object (new image object)
    image = PIL.Image.new(mode="RGB", size=(1280, 720))

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    #load font file
    hfont = ImageFont.truetype(fonts_path+'/atop-font/Atop-R99O3.ttf', 80)
    draw.text((200, 35), "TODAY TOP TRENDS", font=hfont, fill =(255, 255, 255))

    myFont = ImageFont.truetype(fonts_path+'/malache_crunch/tt/malache crunch.ttf', 60)

    text_color = (255, 255, 255)
    x = 100
    y = 150

    # Add Text to an image
    for trend in trends:
        text = "*  " + trend
        draw.text((x, y), text, font=myFont, fill =(255, 255, 255))
        x = 100
        y = y + 65

    # Call draw Method to add 2D graphics in an image
    #I1 = ImageDraw.Draw(img)

    # Save the edited image
    image.save(fname)


def create_headline_images(new_images_path, fonts_path, headlines):
    #load font file
    hfont = ImageFont.truetype(fonts_path+'/atop-font/Atop-R99O3.ttf', 80)

    myFont = ImageFont.truetype(fonts_path+'/malache_crunch/tt/malache crunch.ttf', 40)

    text_color = (255, 255, 255)

    count = 0
    for h1 in headlines:
      count = count + 1

      # creating a image object (new image object)
      image = PIL.Image.new(mode="RGB", size=(1280, 720))

      # Create a drawing context
      draw = ImageDraw.Draw(image)

      # Add header to the image
      draw.text((80, 35), "TOP WORLD HEADLINES TODAY", font=hfont, fill =(255, 0, 0))

      x = 80
      y = 150

      for h2 in h1:

        text_len = len(h2)
        max_len = 56


        # Add Text to an image
        draw.text((x, y), "$", font=myFont, fill =(255, 0, 0))

        #when you have long text devide into 2/3 lines then draw image
        if text_len  <= max_len:
          draw.text((x+40, y), h2, font=myFont, fill =(255, 255, 255))
          y = y + 65
        else:
          max_2l_len = max_len*2
          l = max_len
          if text_len <= max_2l_len:
            draw.text((x+40, y), h2[:max_len], font=myFont, fill =(255, 255, 255))
            y = y + 50
          else:
            l = max_2l_len
            draw.text((x+40, y), h2[:max_len], font=myFont, fill =(255, 255, 255))
            y = y + 50

            draw.text((x+40, y), h2[max_len:l], font=myFont, fill =(255, 255, 255))
            y = y + 50

          draw.text((x+40, y), h2[l:], font=myFont, fill =(255, 255, 255))
          y = y + 65


        # Save the edited image
        img_name = new_images_path+"/whl_" + str(count) + ".png"
        image.save(img_name)

def create_headline_images_with_bg_img(new_images_path, bg_img_path, fonts_path, headlines):
    #load font file
    hfont = ImageFont.truetype(fonts_path+'/atop-font/Atop-R99O3.ttf', 80)

    myFont = ImageFont.truetype(fonts_path+'/montserrat-font/MontserratBlack-3zOvZ.ttf', 60)

    text_color = (255, 255, 255)

    count = 64
    for h1 in headlines:

      # creating a image object (new image object)
      #image = PIL.Image.new(mode="RGB", size=(1280, 720))

      # Create a drawing context
      #draw = ImageDraw.Draw(image)

      # Add header to the image
      #draw.text((80, 35), "TOP WORLD HEADLINES TODAY", font=hfont, fill =(255, 0, 0))
     
      for h2 in h1:
         
        count = count + 1
        
        x = 78
        y = 770
        
        image = PIL.Image.open(bg_img_path)
        draw = ImageDraw.Draw(image)
        
        text_len = len(h2)
        max_len = 50


        # Add Text to an image
        draw.text((x, y), "$", font=myFont, fill =(255, 0, 0))

        #when you have long text devide into 2/3 lines then draw image
        if text_len  <= max_len:
          draw.text((x+40, y), h2, font=myFont, fill =(255, 255, 255))
          y = y + 65
        else:
          max_2l_len = max_len*2
          l = max_len
          if text_len <= max_2l_len:
            draw.text((x+40, y), h2[:max_len], font=myFont, fill =(255, 255, 255))
            y = y + 65
          else:
            l = max_2l_len
            draw.text((x+40, y), h2[:max_len], font=myFont, fill =(255, 255, 255))
            y = y + 65

            draw.text((x+40, y), h2[max_len:l], font=myFont, fill =(255, 255, 255))
            y = y + 65

          draw.text((x+40, y), h2[l:], font=myFont, fill =(255, 255, 255))
          y = y + 65
        
        img_name = new_images_path+"/whl_" + chr(count) + ".png"
        image.save(img_name)
        
# create a file with date and write content
def write_headlines_to_file(path, content):
    filename = datetime.now() 
    # %d - date, %B - month, %Y - Year 
    with open(path + filename.strftime("%d %B %Y")+".txt", "w") as file: 
        file.write(content)         

#world_trends, world_headlines = get_world_trends_headlines()
#print("world_trends: ", world_trends)
#print("world_headlines:", world_headlines)
#create_wordcloud(world_trends, ai_mask_img, w_trends_wc_fname)


#Get news / headlines
world_trends, world_headlines = get_world_trends_headlines()
headlines = list(itertools.chain.from_iterable(world_headlines));

#write headlines to the file
content = '\n'.join(headlines)
write_headlines_to_file(news_files, content)

#text-to-images: 1-wordcloud image for thumbnail,    X - headline images
create_wordcloud(headlines, ai_mask_img, w_hl_wc_fname)
#create_headline_images(w_hl_img_path, fonts_path, world_headlines)
create_headline_images_with_bg_img(w_hl_img_path, headlines_bg_img, fonts_path, world_headlines)

#text-to-speach
news = '.......'.join(map(str, headlines))
t2s.text_to_speach(news, w_hl_aud_fname)   

#create video from images and text generated above
im2v.create_video(w_hl_img_path, w_hl_aud_fname, bg_audio_fname, video_fname)

    
#upload video to youtube
yt.upload_world_headlines(youtube_dir, video_fname, w_hl_wc_fname)