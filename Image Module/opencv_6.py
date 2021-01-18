"""
使用opencv操作影像

六、閾值
原文網址：https://kknews.cc/code/gg2bej8.html
"""
import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
"""
自適應閥值法
"""
threshold = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
cv2.imshow('original', img)
cv2.imshow('adaptive threshold', threshold)

"""
大津閥值法
"""
# retval2, threshold2 = cv2.threshold(grayscaled, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# cv2.imshow('Otsu threshold', threshold2)

cv2.waitKey(0)
cv2.destroyAllWindows()
