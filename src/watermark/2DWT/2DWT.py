import pywt

def dwt(imArray, mode='haar', level=1):
    coeffs=pywt.wavedec2(imArray, mode, level=level)
    coeffs_H=list(coeffs)
    coeffs_H[0] *= 0;
    return coeffs_H;

