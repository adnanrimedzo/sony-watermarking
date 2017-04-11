import numpy as np
import cv

def readImage(dir):
    imArray = cv.imread(dir)
    imArray = cv.cvtColor(imArray, cv.COLOR_RGB2GRAY)
    imArray = np.float32(imArray)
    imArray /= 255;
    return imArray;