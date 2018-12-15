#!/usr/bin/env python
# coding: utf-8

from PIL import Image 
import pytesseract 
import os 
import cmd
import const
import codecs    

def readPhoto(filePath):
    fileExistsInput = False
    fileInput = ''
    ocrText = ''
    
    if filePath == '':
        for extInput in const.All.EXTENSIONS_IMAGE:
            fileInput = const.All.PATH_IMAGE+const.All.FILENAME_IMAGE+extInput
            fileExistsInput = (os.path.isfile(fileInput))
            if (fileExistsInput):
                break
    else:
        fileInput = filePath
        fileExistsInput = (os.path.isfile(fileInput))    
        
    if (fileExistsInput == False):
        print(colors.bashColors.FAIL+'Arquivo da imagem nao encontrado! Necessario capturar a foto novamente!'+colors.bashColors.ENDC)
        print(colors.bashColors.FAIL+'Digite "'+colors.bashColors.OKBLUE+cmd.All.CAMERA+colors.bashColors.FAIL+'"!')
        return
    
    print('A imagem esta sendo processada, por favor aguarde...')
    print('Caminho: '+fileInput)
    ocrText = pytesseract.image_to_string(Image.open(fileInput))  
    print('Imagem processada, resultado: '+colors.bashColors.WARNING+ocrText+colors.bashColors.ENDC)
    
    fileOutput = const.All.PATH_TEXT+const.All.FILENAME_TEXT+const.All.EXTENSION_TEXT
    if (os.path.isfile(fileOutput)):
        os.remove(fileOutput)
    
    os.system('touch '+fileOutput)
    fileOutputText = codecs.open(fileOutput,'w','utf-8')
    fileOutputText.write(u"\ufeff"+ocrText.lower())
    fileOutputText.close()  
    
    return ocrText
