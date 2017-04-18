import numpy as np
import cv2

def readImage(dir):
    imArray = cv2.imread(dir)
    imArray = np.float32(imArray)
    imArray /= 255;
    return imArray;