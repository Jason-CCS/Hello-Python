import cv2
from matplotlib import pyplot as plt

"""
use cv2 to show image
"""
img = cv2.imread('lena.png')
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""
use matplotlib to show image
"""
plt.imshow(img, cmap='gray')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
# plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()

