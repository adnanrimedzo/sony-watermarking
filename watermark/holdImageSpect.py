import cv


def getImageHist(img):
    hist = cv.calcHist([img], [0], None, [256], [0, 256])
    return hist


def getImageMax(img):
    max = img[...].max()
    return max


def getImageMin(img):
    max = img[...].max()
    return max


def getImageShape(img):
    return img.shape
