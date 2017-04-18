import numpy as np
import pywt


def diwt(coeffs_H, mode='haar'):
    imArray_H = pywt.waverec2(coeffs_H, mode);
    imArray_H *= 255;
    imArray_H = np.uint8(imArray_H);
    return imArray_H;
