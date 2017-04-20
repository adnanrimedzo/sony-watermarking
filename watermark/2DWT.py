import numpy as np
import pywt


def dwt(imArray, mode='haar', level=1):
    coeffs = pywt.wavedec2(imArray, mode, level=level)
    coeffs_H = list(coeffs)
    coeffs_H[0] *= 0;
    return coeffs_H;


def diwt(coeffs_H, mode='haar'):
    imArray_H = pywt.waverec2(coeffs_H, mode);
    imArray_H *= 255;
    imArray_H = np.uint8(imArray_H);
    return imArray_H;
