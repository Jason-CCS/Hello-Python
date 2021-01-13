"""
使用opencv操作影像

六、閾值
原文網址：https://kknews.cc/code/gg2bej8.html
"""
import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
cv2.imshow('1', img)
cv2.imshow('threshold', threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()


