import readImage, cv2, os
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))


#open image
img = readImage.readImage(dir_path + '/../tests/samples/xperiax.jpg');
# plt.imshow(img)
# plt.show()

#split image
blue,green,red = cv2.split(img)
img = cv2.merge((blue,green,red))
# plt.subplot(131),plt.imshow(blue,'gray'),plt.title('blue')
# plt.subplot(132),plt.imshow(green,'gray'),plt.title('green')
# plt.subplot(133),plt.imshow(red,'gray'),plt.title('red')
# plt.show()




