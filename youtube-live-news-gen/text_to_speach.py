import os
from datetime import datetime
import pytesseract
from gtts import gTTS

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def text_to_speach(news, aud_fname):
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
    myobj.save(aud_fname)

    # Playing the converted file
    #os.system("start welcome.mp3")
    print('Text-to-speach convertion completed')