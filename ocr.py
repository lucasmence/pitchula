#!/usr/bin/env python
# coding: utf-8

from PIL import Image 
import pytesseract 
import os 
import codecs   
import jsonLib 

def readPhoto(filename, filetext):
    fileInput = filename

    ocrText = pytesseract.image_to_string(Image.open(fileInput))  

    fileOutput = filetext
    if (os.path.isfile(fileOutput)):
        os.remove(fileOutput)
    
    os.system("touch "+fileOutput)  
    fileOutputText = codecs.open(fileOutput,"w","utf-8")
    fileOutputText.write(u"\ufeff"+ocrText.lower())
    fileOutputText.close()  
    
