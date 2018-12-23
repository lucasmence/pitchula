#!/usr/bin/env python
# coding: utf-8

import os
import jsonLib
        
def clearAll(pathVariables):
    imagePath = jsonLib.getValue(pathVariables,"imagePath")+"/"+jsonLib.getValue(pathVariables,"imageFilename")+"."+jsonLib.getValue(pathVariables,"imageExtensionDefault")
    textPath = jsonLib.getValue(pathVariables,"textPath")+"/"+jsonLib.getValue(pathVariables,"textFilename")+"."+jsonLib.getValue(pathVariables,"textExtension")

    if (os.path.isfile(imagePath)):
        os.remove(imagePath)

    if (os.path.isfile(textPath)):
        os.remove(textPath)
    
    return 0
