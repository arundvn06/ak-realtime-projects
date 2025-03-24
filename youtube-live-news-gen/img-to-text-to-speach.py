import os
from datetime import datetime
import cv2  
import pytesseract
from PIL import Image
from gtts import gTTS

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

dname = "F:/certifications/IIITH-AIML/research/imagen/banner/"
folder = os.path.join(dname, datetime.now().strftime('%Y-%m-%d')) 

def img_to_text():
    print('Extractign text from images in the folder: ', folder)
    news = ''
    for filename in os.listdir(folder):
        if filename != 'dup':
            img = cv2.imread(os.path.join(folder,filename))
            if img is not None:
                org_img_path = folder+"/"+filename
                
                # Load the image 
                image = cv2.imread(org_img_path)  
                text = pytesseract.image_to_string(image)
                news = news + text.strip() + "....."
                #news = news + " ".join(text.split()) + "....."
                #print(text)
    print('Image-to-text extraction completed')
    return news

def text_to_speach(news):
    print('Text-to-speach convertion started')
    # The text that you want to convert to audio
    mytext = news

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    # myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj = gTTS(text=mytext, lang=language, tld='co.in', slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save(folder+"/text-speach.mp3")

    # Playing the converted file
    #os.system("start welcome.mp3")
    print('Text-to-speach convertion completed')



news = img_to_text()

#f = open(folder+"/img_to_text.txt", "a")
#f.write(news)
#f.close()
#print(news)
text_to_speach(news)
