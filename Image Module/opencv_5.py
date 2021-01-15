"""
使用opencv操作影像

五、圖像算術和邏輯運算
原文網址：https://kknews.cc/code/gg2bej8.html
"""
import cv2
import numpy as np

"""
相加兩個等大影像
"""
# img1 = cv2.imread('lena.png')
# img2 = cv2.imread('baboon.png')
# # cv2.imshow('lena', img1)
# # cv2.imshow('baboon', img2)
#
# weighted = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)  # combine two images together and use weighted method
# cv2.imshow('add', weighted)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""
將一個影像嵌進另一個影像，不容易啊
"""
lena = cv2.imread('lena.png')
python_logo = cv2.resize(cv2.imread('python.jpg'), (128, 128))
# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = python_logo.shape
roi = lena[0:rows, 0:cols]
# Now create a mask of logo and create its inverse mask
python_log_gray = cv2.cvtColor(python_logo, cv2.COLOR_BGR2GRAY)

# add a threshold
# THRESH_BINARY，將220以上的都變成255
ret, mask = cv2.threshold(python_log_gray, 220, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI, 使用位元操作，將mask與roi做bit-and，例如 11011001 and 11111111 = 11011001
img1_bg = cv2.bitwise_and(roi, roi, mask=mask) # 不知道為什麼這個function有兩個src: src1 and src2
cv2.imshow('1', img1_bg)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(python_logo, python_logo, mask=mask_inv)
cv2.imshow('2', img2_fg)
dst = cv2.add(img1_bg, img2_fg)
lena[0:rows, 0:cols] = dst

cv2.imshow('res', lena)
cv2.waitKey(0)
cv2.destroyAllWindows()
