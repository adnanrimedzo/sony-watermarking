import cv
import numpy as np


def equalizeImage(img):
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])

    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    return cdf_normalized


def fixShape(img, shape):
    width, height, channel = shape
    res = cv.resize(img, (width, height), interpolation=cv.INTER_NEAREST)
    return res;

def otsuThreshold(img):
    (thresh, im_bw) = cv.threshold(img, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU) #todo: check parameters one more time
    return im_bw