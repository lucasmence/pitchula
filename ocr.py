#!/usr/bin/env python
# coding: utf-8

from PIL import Image 
import pytesseract 
import os 
import codecs   

class Ocr():

    def __init__(self, constants):
        self._constants = constants

    def readPhoto(self, filename, filetext, textTypeCodecs):
        fileInput = filename

        ocrText = pytesseract.image_to_string(Image.open(fileInput))  

        fileOutput = filetext
        if (os.path.isfile(fileOutput)):
            os.remove(fileOutput)
        
        os.system(self._constants._COMMAND_CREATE_FILE+fileOutput)  
        fileOutputText = codecs.open(fileOutput,self._constants._COMMAND_WRITE_MODE,textTypeCodecs)
        fileOutputText.write(self._constants._COMMAND_WRITE_FILE+ocrText.lower())
        fileOutputText.close()  
    
