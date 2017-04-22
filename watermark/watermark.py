import readImage, cv2, os, equalizeImageSpect, numpy, QR, DWT
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))

# open image
img = readImage.readImage(dir_path + '/../tests/samples/xperiax.jpg');
# plt.imshow(img)
# plt.show()

# resize image
shape = [4096, 4096, 3]
img = equalizeImageSpect.fixShape(img, shape)
# plt.imshow(img)
# plt.show()

# split image
blue, green, red = cv2.split(img)
img = cv2.merge((blue, green, red))
# plt.subplot(131),plt.imshow(blue,'gray'),plt.title('blue')
# plt.subplot(132),plt.imshow(green,'gray'),plt.title('green')
# plt.subplot(133),plt.imshow(red,'gray'),plt.title('red')
# plt.show()

# QR code generate
qrImg = QR.generate("adnan", 128, 128)
# plt.imshow(qrImg)
# plt.show()

# DWT
blue = DWT.dwt(blue, "haar", 5)
blue[0] =blue[0] + 0.05 * qrImg[:, : ,1]
# DWT.coeffs_visualization(blue)
result = DWT.diwt(blue, "haar")
result = DWT.image_normalization(result)
img = cv2.merge((result, green, red))

plt.imshow(img)
plt.show()
