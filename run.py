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
                
def run():

    variables = constants.PATH_VARIABLES
    textType = jsonLib.getValue(variables,constants.FIELD_TEXT_TYPE)
    textTypeCodecs = jsonLib.getValue(variables,constants.FIELD_TEXT_TYPE_CODECS)
    sys.setdefaultencoding(textType)
    languageType = jsonLib.getValue(variables,constants.FIELD_LANGUAGE_CURRENT)
    languagePath = jsonLib.getValue(variables,constants.PATH_LANGUAGE)+languageType+constants.EXTENSION_JSON

    if (len(sys.argv) <= constants.MINIMUM_ARGUMENTS):
        print(jsonLib.getValue(languagePath,constants.FIELD_ERROR_PARAMETERS))
        return constants.INDEX_RETURN_ERROR    

    pathImage = sys.argv[constants.INDEX_ARGUMENT_IMAGE]
    pathAudio = sys.argv[constants.INDEX_ARGUMENT_AUDIO]
    extension = os.path.splitext(pathImage)[constants.INDEX_POSITION_EXTENSION][constants.INDEX_POSITION_SPLIT_ORDER:]

    if not (os.path.isfile(pathImage)):
        print(jsonLib.getValue(languagePath,constants.FIELD_ERROR_INPUT))
        return constants.INDEX_RETURN_ERROR        
    if (not (os.path.dirname(pathAudio))) and (os.path.dirname(pathAudio) != constants.FIELD_EMPTY_STRING):
        print(jsonLib.getValue(languagePath,constants.FIELD_ERROR_OUTPUT))
        return constants.INDEX_RETURN_ERROR
    if not (extension in jsonLib.getValue(variables,constants.FIELD_IMAGE_EXTENSION)):
        print(jsonLib.getValue(languagePath,constants.FIELD_ERROR_FILE_TYPE))
        return constants.INDEX_RETURN_ERROR    

    print(jsonLib.getValue(languagePath,constants.FIELD_MESSAGE_WELCOME)) 

    internalImage = jsonLib.getValue(variables,constants.FIELD_IMAGE_FILENAME)
    internalText = jsonLib.getValue(variables,constants.FIELD_TEXT_FILENAME)
    
    image.fixImage(pathImage,internalImage)

    ocr.readPhoto(internalImage,internalText,textTypeCodecs)

    spellcheck.verifyFile(internalText,languageType,textType,textTypeCodecs)

    ttsLanguage = jsonLib.getValue(languagePath,constants.FIELD_GTTS_CODE)
    audioExists = tts.convertText(internalText,pathAudio,ttsLanguage)

    if (audioExists == constants.INDEX_RETURN_OK):
        print(jsonLib.getValue(languagePath,constants.FIELD_MESSAGE_FINISH))
    
    functions.clearAll(internalImage,internalText)
    
    return constants.INDEX_RETURN_OK
            
run()
            
    


    
