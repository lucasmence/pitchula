import cv2
import os
import numpy

def fixImage(filename,internalImage):
    image = cv2.imread(filename)
    originalGamma = numpy.double(image)
    newGamma = originalGamma + 30
    image = numpy.uint8(newGamma)
    
    imageGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    (thresh, im_bw) = cv2.threshold(imageGray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    thresh = 127
    im_bw = cv2.threshold(imageGray, thresh, 255, cv2.THRESH_BINARY)[1]
    
    if (os.path.isfile(internalImage)):
        os.remove(internalImage)
        
    cv2.imwrite(internalImage,im_bw)
    return 0
    
    
    
