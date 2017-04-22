import numpy as np
import cv2

def readImage(dir):
    img = cv2.imread(dir)
    img = np.float32(img)
    return img;