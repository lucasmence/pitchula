#!/usr/bin/env python
# coding: utf-8

import constants
import cv2
import os
import numpy

def fixImage(filename,internalImage):

    image = cv2.imread(filename)
    originalGamma = numpy.double(image)
    newGamma = originalGamma + constants.VALUE_IMAGE_PERCENT_GAMMA_CORRECTION
    image = numpy.uint8(newGamma)
    
    imageGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    (thresh, im_bw) = cv2.threshold(imageGray, constants.VALUE_IMAGE_BLACK_WHITE_DIVISION, constants.VALUE_IMAGE_COLORS, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    thresh = constants.VALUE_IMAGE_BLACK_WHITE_UPDATE
    im_bw = cv2.threshold(imageGray, thresh, constants.VALUE_IMAGE_COLORS, cv2.THRESH_BINARY)[constants.VALUE_IMAGE_BINARY_GET]
    
    if (os.path.isfile(internalImage)):
        os.remove(internalImage)
        
    cv2.imwrite(internalImage,im_bw)
    return constants.INDEX_RETURN_OK
    
    
    
