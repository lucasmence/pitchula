#!/usr/bin/env python
# coding: utf-8

import constants
from PIL import Image 
import pytesseract 
import os 
import codecs   

def readPhoto(filename, filetext, textTypeCodecs):
    fileInput = filename

    ocrText = pytesseract.image_to_string(Image.open(fileInput))  

    fileOutput = filetext
    if (os.path.isfile(fileOutput)):
        os.remove(fileOutput)
    
    os.system(constants.COMMAND_CREATE_FILE+fileOutput)  
    fileOutputText = codecs.open(fileOutput,constants.COMMAND_WRITE_MODE,textTypeCodecs)
    fileOutputText.write(constants.COMMAND_WRITE_FILE+ocrText.lower())
    fileOutputText.close()  
    
