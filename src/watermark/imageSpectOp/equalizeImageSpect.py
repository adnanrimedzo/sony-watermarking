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

def otsuThreshold(img):
    (thresh, im_bw) = cv.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #todo: check parameters one more time
    return im_bw