#!/usr/bin/env python
# coding: utf-8

from gtts import gTTS
import os

class Tts():

    def __init__(self, constants):
        self._constants = constants

    def convertText(self, filename, output, language):
        
        fileInput = filename
        fileText = self._constants._FIELD_EMPTY_STRING

        for listItem in open(fileInput,self._constants._COMMAND_READ_MODE).read().splitlines():   
            fileText = fileText+self._constants._FIELD_SPACE+listItem
            
        if ((fileText == None) or (len(fileText.strip()) < self._constants._MINIMUM_TEXT_SIZE)):
            return self._constants._INDEX_RETURN_ERROR

        fileOutput = output
        tts = gTTS(text=fileText, lang=language) 
        tts.save(fileOutput)

        return self._constants._INDEX_RETURN_OK

