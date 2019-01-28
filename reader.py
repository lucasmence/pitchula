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

    def start(self,inputFile, outputFile):

        _jsonLib = jsonLib.JsonLib(self._constants)   

        variables = self._constants._PATH_VARIABLES
        textType = _jsonLib.getValue(variables,self._constants._FIELD_TEXT_TYPE)
        textTypeCodecs = _jsonLib.getValue(variables,self._constants._FIELD_TEXT_TYPE_CODECS)
        languageType = _jsonLib.getValue(variables,self._constants._FIELD_LANGUAGE_CURRENT)
        languagePath = _jsonLib.getValue(variables,self._constants._PATH_LANGUAGE)+languageType+self._constants._EXTENSION_JSON 
        extension = os.path.splitext(inputFile)[self._constants._INDEX_POSITION_EXTENSION][self._constants._INDEX_POSITION_SPLIT_ORDER:]

        if (inputFile == self._constants._FIELD_EMPTY_STRING or outputFile == self._constants._FIELD_EMPTY_STRING):
            print(_jsonLib.getValue(languagePath,self._constants._FIELD_ERROR_PARAMETERS))
            return self._constants._INDEX_RETURN_ERROR 

        if not (os.path.isfile(inputFile)):
            print(_jsonLib.getValue(languagePath,self._constants._FIELD_ERROR_INPUT))
            return self._constants._INDEX_RETURN_ERROR        
        if (not (os.path.dirname(outputFile))) and (os.path.dirname(outputFile) != self._constants._FIELD_EMPTY_STRING):
            print(_jsonLib.getValue(languagePath,self._constants._FIELD_ERROR_OUTPUT))
            return self._constants._INDEX_RETURN_ERROR
        if not (extension in _jsonLib.getValue(variables,self._constants._FIELD_IMAGE_EXTENSION)):
            print(_jsonLib.getValue(languagePath,self._constants._FIELD_ERROR_FILE_TYPE))
            return self._constants._INDEX_RETURN_ERROR    

        print(_jsonLib.getValue(languagePath,self._constants._FIELD_MESSAGE_WELCOME)) 

        internalImage = _jsonLib.getValue(variables,self._constants._FIELD_IMAGE_FILENAME)
        internalText = _jsonLib.getValue(variables,self._constants._FIELD_TEXT_FILENAME)
        
        _image = image.Image(self._constants)
        _image.fixImage(inputFile,internalImage)
        if (_image):
            del _image

        _ocr = ocr.Ocr(self._constants)
        _ocr.readPhoto(internalImage,internalText,textTypeCodecs)
        if (_ocr):
            del _ocr

        _spellcheck = spellcheck.Spellcheck(self._constants)
        _spellcheck.verifyFile(internalText,languageType,textType,textTypeCodecs)
        if (_spellcheck):
            del _spellcheck

        ttsLanguage = _jsonLib.getValue(languagePath,self._constants._FIELD_GTTS_CODE)
        _tts = tts.Tts(self._constants)
        audioExists = _tts.convertText(internalText,outputFile,ttsLanguage)
        if (_tts):
            del _tts

        if (audioExists == self._constants._INDEX_RETURN_OK):
            print(_jsonLib.getValue(languagePath,self._constants._FIELD_MESSAGE_FINISH))
        
        if (_jsonLib):
            del _jsonLib

        _functions = functions.Functions(self._constants)
        _functions.clearAll(internalImage,internalText)
         if (_functions):
            del _functions
  
        return self._constants._INDEX_RETURN_OK


    def __del__(self):
        if (self._constants):
            del self._constants
        
                   
            
    


    
