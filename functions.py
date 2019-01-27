#!/usr/bin/env python
# coding: utf-8

import os

class Functions():

    def __init__(self, constants):
        self._constants = constants

    def clearAll(self, imagePath, textPath):
        if (os.path.isfile(imagePath)):
            os.remove(imagePath)

        if (os.path.isfile(textPath)):
            os.remove(textPath)
        
        return self._constants._INDEX_RETURN_OK
