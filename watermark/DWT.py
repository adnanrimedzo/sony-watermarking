import numpy as np
import pywt
import matplotlib.pyplot as plt


def dwt(img, kernel='haar', level=1, mode="sym"):
    data = img.astype(np.float64)
    coeffs = pywt.wavedec2(data, kernel, level=level, mode=mode)
    return coeffs


def diwt(coeffs, kernel='haar', mode="sym"):
    data = pywt.waverec2(coeffs, kernel, mode);
    return data;

def image_normalization(src_img):
    norm_img = (src_img - np.min(src_img)) / (np.max(src_img) - np.min(src_img))
    return norm_img

def merge_images(cA, cH_V_D):
    cH, cV, cD = cH_V_D
    cH = image_normalization(cH)
    cV = image_normalization(cV)
    cD = image_normalization(cD)
    cA = cA[0:cH.shape[0], 0:cV.shape[1]]
    return np.vstack((np.hstack((cA,cH)), np.hstack((cV, cD))))

def coeffs_visualization(cof):
    norm_cof0 = cof[0]
    norm_cof0 = image_normalization(norm_cof0)
    merge = norm_cof0
    for i in range(1, len(cof)):
        merge = merge_images(merge, cof[i])
    plt.imshow(merge, cmap="gray")
    plt.show()