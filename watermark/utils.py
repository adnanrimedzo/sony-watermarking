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
    (thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return im_bw


def saveImage(dir, img):
    cv2.imwrite(dir, img)


def readImage(dir):
    img = cv2.imread(dir)
    img = np.float32(img)
    return img;

def byteArrayToImg(imgByte):
    img = np.float32(imgByte)
    return img;


def getImageHist(img):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    return hist


def getImageMax(img):
    max = img[...].max()
    return max


def getImageMin(img):
    max = img[...].min()
    return max


def getImageShape(img):
    return img.shape


def splitBands(img):
    return cv2.split(img)


def mergeBands(blue, green, red):
    return cv2.merge((blue, green, red))
