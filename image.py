#!/usr/bin/env python
# coding: utf-8

import cv2
import os
import numpy

class Image():
    def __init__(self, constants):
        self._constants = constants

    def fixImage(self, filename,internalImage):

        image = cv2.imread(filename)
        originalGamma = numpy.double(image)
        newGamma = originalGamma + self._constants._VALUE_IMAGE_PERCENT_GAMMA_CORRECTION
        image = numpy.uint8(newGamma)
        
        imageGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        
        (thresh, im_bw) = cv2.threshold(imageGray, self._constants._VALUE_IMAGE_BLACK_WHITE_DIVISION, self._constants._VALUE_IMAGE_COLORS, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        thresh = self._constants._VALUE_IMAGE_BLACK_WHITE_UPDATE
        im_bw = cv2.threshold(imageGray, thresh, self._constants._VALUE_IMAGE_COLORS, cv2.THRESH_BINARY)[self._constants._VALUE_IMAGE_BINARY_GET]
        
        if (os.path.isfile(internalImage)):
            os.remove(internalImage)
            
        cv2.imwrite(internalImage,im_bw)
        return self._constants._INDEX_RETURN_OK
    
    
    
