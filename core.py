#coding: utf-8

import audio
import config
import funct
import image
import jsonLib
import ocr
import os
import spellcheck
import sys
import time
import tts

reload(sys)   
                
def systemStart():

    VARIABLES = 'data/strings/variables.json'

    sys.setdefaultencoding(jsonLib.getValue(VARIABLES,'textType'))

    language = jsonLib.getValue(VARIABLES,'languageCurrent')

    funct.clearAll()

    image.fixImage(imagePath)

    ocr.readPhoto()

    spellcheck.verifyFile()

    audioExists = tts.convertText()

    if (audioExists == True):
        audio.speech()
    
    return 0
            
systemStart()
            
    


    
