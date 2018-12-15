#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gtts import gTTS
import os
import cmd
import const
import funct
import config

def convertText():
    
    fileInput = const.All.PATH_TEXT+const.All.FILENAME_TEXT+const.All.EXTENSION_TEXT
    if (os.path.isfile(fileInput) == False):
        print(colors.bashColors.FAIL+'Arquivo texto nao encontrado, execute o processamento da img novamente digitando "'+colors.bashColors.OKBLUE+cmd.All.OCR+colors.bashColors.FAIL+'"!')
        return
    
    fileText = ''
    for listItem in open(fileInput,'r').read().splitlines():   
        fileText = fileText+' '+listItem
    
    fileText = funct.removeAccents(fileText)
    if ((fileText == None) or (len(fileText.strip()) < 4)):
        print(colors.bashColors.FAIL+'O arquivo texto esta em branco, realize a catura da imagem novamente digitando "'+colors.bashColors.OKBLUE+cmd.All.CAMERA+colors.bashColors.FAIL+'"!')
        return False
    else:
        print('Audio a ser gerado: '+fileText)
        fileOutput = const.All.PATH_AUDIO+const.All.FILENAME_AUDIO+const.All.EXTENSION_AUDIO
        print('Convertendo texto para audio, aguarde pois pode levar alguns segundos...')
        
        language = config.getLanguage()
        if (language == "pt_br"):
            language = "pt"
        elif (language == "en_us"):
            language = "en"
        
        tts = gTTS(text=fileText, lang=language)
        
        tts.save(fileOutput)
        print('Audio gerado com exito!') 
        return True

