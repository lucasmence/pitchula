#!/usr/bin/env python
# coding: utf-8

from PIL import Image 
import pytesseract 
import os 
import codecs   
import jsonLib 

def readPhoto(filename, pathVariables):
    fileInput = filename

    ocrText = pytesseract.image_to_string(Image.open(fileInput))  

    fileOutput = jsonLib.getValue(pathVariables,"textPath")+"/"+jsonLib.getValue(pathVariables,"textFilename")+"."+jsonLib.getValue(pathVariables,"textExtension")
    if (os.path.isfile(fileOutput)):
        os.remove(fileOutput)
    
    os.system("touch "+fileOutput)  
    fileOutputText = codecs.open(fileOutput,"w","utf-8")
    fileOutputText.write(u"\ufeff"+ocrText.lower())
    fileOutputText.close()  
    
