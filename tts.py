#!/usr/bin/env python
# coding: utf-8

import constants
from gtts import gTTS
import os

def convertText(filename, output, language):
    
    fileInput = filename
    fileText = constants.FIELD_EMPTY_STRING

    for listItem in open(fileInput,constants.COMMAND_READ_MODE).read().splitlines():   
        fileText = fileText+constants.FIELD_SPACE+listItem
        
    if ((fileText == None) or (len(fileText.strip()) < constants.MINIMUM_TEXT_SIZE)):
        return constants.INDEX_RETURN_ERROR

    fileOutput = output
    tts = gTTS(text=fileText, lang=language) 
    tts.save(fileOutput)

    return constants.INDEX_RETURN_OK

