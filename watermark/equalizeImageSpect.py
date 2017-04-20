import cv2
import numpy as np


def equalizeImage(img):
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])

    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    return cdf_normalized


def fixShape(img, shape):
    width, height, channel = shape
    res = cv2.resize(img, (width, height), interpolation=cv2.INTER_NEAREST)
    return res;

def otsuThreshold(img):
    (thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #todo: check parameters one more time
    return im_bw