#!/usr/bin/env python
# coding: utf-8

import constants
import functions
import image
import jsonLib
import ocr
import os
import spellcheck
import sys
import tts

class Reader():
    
    def __init__(self):
        self._constants = constants.Constants()
        self._functions = functions.Functions(self._constants)
        self._image = image.Image(self._constants)
        self._jsonLib = jsonLib.JsonLib(self._constants)
        self._ocr = ocr.Ocr(self._constants)
        self._spellcheck = spellcheck.Spellcheck(self._constants)
        self._tts = tts.Tts(self._constants)

        

    def start(self,inputFile, outputFile):
        
        if (inputFile == self._constants._FIELD_EMPTY_STRING or outputFile == self._constants._FIELD_EMPTY_STRING):
            print(self._jsonLib.getValue(languagePath,self._constants._FIELD_ERROR_PARAMETERS))
            return self._constants._INDEX_RETURN_ERROR    

        pathImage = inputFile
        pathAudio = outputFile

        variables = self._constants._PATH_VARIABLES
        textType = self._jsonLib.getValue(variables,self._constants._FIELD_TEXT_TYPE)
        textTypeCodecs = self._jsonLib.getValue(variables,self._constants._FIELD_TEXT_TYPE_CODECS)
        languageType = self._jsonLib.getValue(variables,self._constants._FIELD_LANGUAGE_CURRENT)
        languagePath = self._jsonLib.getValue(variables,self._constants._PATH_LANGUAGE)+languageType+self._constants._EXTENSION_JSON
    
        extension = os.path.splitext(pathImage)[self._constants._INDEX_POSITION_EXTENSION][self._constants._INDEX_POSITION_SPLIT_ORDER:]

        if not (os.path.isfile(pathImage)):
            print(self._jsonLib.getValue(languagePath,self._constants._FIELD_ERROR_INPUT))
            return self._constants._INDEX_RETURN_ERROR        
        if (not (os.path.dirname(pathAudio))) and (os.path.dirname(pathAudio) != self._constants._FIELD_EMPTY_STRING):
            print(self._jsonLib.getValue(languagePath,self._constants._FIELD_ERROR_OUTPUT))
            return self._constants._INDEX_RETURN_ERROR
        if not (extension in self._jsonLib.getValue(variables,self._constants._FIELD_IMAGE_EXTENSION)):
            print(self._jsonLib.getValue(languagePath,self._constants._FIELD_ERROR_FILE_TYPE))
            return self._constants._INDEX_RETURN_ERROR    

        print(self._jsonLib.getValue(languagePath,self._constants._FIELD_MESSAGE_WELCOME)) 

        internalImage = self._jsonLib.getValue(variables,self._constants._FIELD_IMAGE_FILENAME)
        internalText = self._jsonLib.getValue(variables,self._constants._FIELD_TEXT_FILENAME)
        
        self._image.fixImage(pathImage,internalImage)

        self._ocr.readPhoto(internalImage,internalText,textTypeCodecs)

        self._spellcheck.verifyFile(internalText,languageType,textType,textTypeCodecs)

        ttsLanguage = self._jsonLib.getValue(languagePath,self._constants._FIELD_GTTS_CODE)
        audioExists = self._tts.convertText(internalText,pathAudio,ttsLanguage)

        if (audioExists == self._constants._INDEX_RETURN_OK):
            print(self._jsonLib.getValue(languagePath,self._constants._FIELD_MESSAGE_FINISH))
        
        self._functions.clearAll(internalImage,internalText)
        
        return self._constants._INDEX_RETURN_OK


    def __del__(self):
        del self._constants
        del self._functions
        del self._image
        del self._jsonLib
        del self._ocr
        del self._spellcheck
        del self._tts
                   
            
    


    
