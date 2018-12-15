#!/usr/bin/env python
# coding: utf-8

import os
from os import listdir
from os.path import isfile
import const

def listingFiles(path):
    return listdir(path)
    
      
def clearFile(type):
    listFile = []
    fileType = ''
    filePath = ''
    
    if (type == const.All.FILE_TYPE_IMAGE):
        listFile = listingFiles(const.All.PATH_IMAGE)
        fileType = const.All.FILE_TYPE_IMAGE
        filePath = const.All.PATH_IMAGE 
    elif (type == const.All.FILE_TYPE_TEXT):
        listFile = listingFiles(const.All.PATH_TEXT)
        fileType = const.All.FILE_TYPE_TEXT
        filePath = const.All.PATH_TEXT 
    elif (type == const.All.FILE_TYPE_AUDIO):
        listFile = listingFiles(const.All.PATH_AUDIO)
        fileType = const.All.FILE_TYPE_AUDIO
        filePath = const.All.PATH_AUDIO
    elif (type == const.All.FILE_TYPE_IMAGE_CROPPED):
        listFile = listingFiles(const.All.PATH_IMAGE_CROPPED)
        fileType = const.All.FILE_TYPE_IMAGE_CROPPED
        filePath = const.All.PATH_IMAGE_CROPPED
        
    fileCount = 0
    
    for file in listFile:
        print('Removendo '+filePath+file+'...')
        if (os.path.isfile(filePath+file)):
            fileCount = fileCount + 1
            os.remove(filePath+file)
            
    print('Foi removido '+str(fileCount)+' '+fileType+' locais')
        
def clearAll():
    clearFile(const.All.FILE_TYPE_IMAGE)
    clearFile(const.All.FILE_TYPE_TEXT)
    clearFile(const.All.FILE_TYPE_AUDIO)
