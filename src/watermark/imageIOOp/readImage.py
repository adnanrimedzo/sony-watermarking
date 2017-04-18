import numpy as np
import cv2

def readImage(dir):
    imArray = cv2.imread(dir)
    imArray = cv2.cvtColor(imArray, cv2.COLOR_RGB2GRAY)
    imArray = np.float32(imArray)
    imArray /= 255;
    return imArray;