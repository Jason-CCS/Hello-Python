"""
使用opencv操作影像

三、圖像操作
原文網址：https://kknews.cc/code/gg2bej8.html
"""
import cv2

img = cv2.imread('lena.png', cv2.IMREAD_COLOR)

"""
填滿ROI
"""
face = img[180:390, 220:370]
img[180:390, 220:370] = [255, 255, 255]
cv2.imshow('lena_face', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
