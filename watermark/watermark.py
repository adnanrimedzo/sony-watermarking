import cv2, os, utils, numpy, QR, DWT
# import matplotlib.pyplot as plt

# dir_path = os.path.dirname(os.path.realpath(__file__))

# open image
# img = utils.readImage(dir_path + '/../tests/samples/xperiax.jpg');

def markByteImage(dir, key):
    # dir_path = os.path.dirname(os.path.realpath(__file__))

    # open image
    img = utils.readImage(dir);

    # img = utils.byteArrayToImg(imageByte);
    max = utils.getImageMax(img)
    min = utils.getImageMin(img)

    cv2.normalize(img, img, 0.0, 255.0, cv2.NORM_MINMAX)

    sourceimgShape = utils.getImageShape(img)
    # plt.imshow(img)
    # plt.show()

    # resize imagex
    shape = [4096, 4096, 3]
    img = utils.fixShape(img, shape)
    # plt.imshow(img)
    # plt.show()

    # split image
    blue, green, red = utils.splitBands(img)
    img = utils.mergeBands(blue, green, red)
    # plt.subplot(131),plt.imshow(blue,'gray'),plt.title('blue')
    # plt.subplot(132),plt.imshow(green,'gray'),plt.title('green')
    # plt.subplot(133),plt.imshow(red,'gray'),plt.title('red')
    # plt.show()

    # QR code generate
    qrImg = QR.generate(key, 1024, 1024)
    # plt.imshow(qrImg, cmap="gray")
    # plt.show()

    # DWT
    blueHaar = DWT.dwt(blue, "db1", 7)
    cH, cV, cD = blueHaar[7]
    xxx = DWT.dwt(cD, "db1", 2)
    xH, xV, xD = xxx[2]
    cv2.normalize(qrImg, qrImg, numpy.max(xD), numpy.min(xD), cv2.NORM_MINMAX)
    xD = qrImg
    xxx[2] = xH, xV, xD

    cD = DWT.diwt(xxx, "db1")

    # DWT.coeffs_visualization(blueHaar)
    blueHaar[7] = cH, cV, cD
    result = DWT.diwt(blueHaar, "db1")
    cv2.normalize(result, result, numpy.min(blue), numpy.max(blue), cv2.NORM_MINMAX)
    img = cv2.merge((result, green, red))
    #img = utils.fixShape(img, sourceimgShape)
    cv2.normalize(img, img, min, max, cv2.NORM_MINMAX)
    img = numpy.uint8(img)
    # return img;
    utils.saveImage("output-file.jpg", img);
    return True
# plt.imshow(img)
# plt.show()



# get QR

# open image
# img = utils.readImage(dir_path + '/../tests/samples/out.jpg');

def getKeyFromByteImage(dir):
    # open image
    img = utils.readImage(dir);
    # img = utils.byteArrayToImg(imageByte);
    # resize image
    shape = [4096, 4096, 3]
    img = utils.fixShape(img, shape)

    # split image
    blue, green, red = cv2.split(img)
    img = cv2.merge((blue, green, red))

    # DWT
    blueHaar = DWT.dwt(blue, "db1", 7)
    cH, cV, cD = blueHaar[7]
    xxx = DWT.dwt(cD, "db1", 2)
    xH, xV, xD = xxx[2]
    cv2.normalize(xD, xD, 0, 255, cv2.NORM_MINMAX)
    cv2.normalize(xV, xV, 0, 255, cv2.NORM_MINMAX)
    cv2.normalize(xH, xH, 0, 255, cv2.NORM_MINMAX)
    xD = numpy.uint8(xD)
    xV = numpy.uint8(xV)
    xH = numpy.uint8(xH)
    xD = utils.otsuThreshold(xD)
    xv = utils.otsuThreshold(xV)
    xH = utils.otsuThreshold(xH)

    return QR.readQRMessage(xD);

    # plt.subplot(131), plt.imshow(xH, 'gray'), plt.title('xH')
    # plt.subplot(132), plt.imshow(xV, 'gray'), plt.title('xV')
    # plt.subplot(133), plt.imshow(xD, 'gray'), plt.title('xD')
    # plt.show()
