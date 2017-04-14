import cv
import numpy as np


def equalizeImage(img):
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])

    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    return cdf_normalized


def fixShape(img, shape):
    width, height, channel = shape
    res = cv.resize(img, (width, height), interpolation=cv2.INTER_CUBIC) #todo: nearest interpolation
    return res;