#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gtts import gTTS
import os

def convertText(filename, output, language):
    
    fileInput = filename
    fileText = ""

    for listItem in open(fileInput,"r").read().splitlines():   
        fileText = fileText+" "+listItem
    if ((fileText == None) or (len(fileText.strip()) < 4)):
        return 1

    fileOutput = output
    tts = gTTS(text=fileText, lang=language) 
    tts.save(fileOutput)

    return 0

