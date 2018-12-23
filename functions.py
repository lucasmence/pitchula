#!/usr/bin/env python
# coding: utf-8

import constants
import os
        
def clearAll(imagePath, textPath):
    if (os.path.isfile(imagePath)):
        os.remove(imagePath)

    if (os.path.isfile(textPath)):
        os.remove(textPath)
    
    return constants.INDEX_RETURN_OK
