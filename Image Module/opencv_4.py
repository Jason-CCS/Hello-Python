"""
使用opencv操作影像

四、圖像操作
原文網址：https://kknews.cc/code/gg2bej8.html
"""
import cv2

img = cv2.imread('lena.png', cv2.IMREAD_COLOR)

px = img[180, 220] # get pixel
print(px)

face = img[180:390, 220:370] # get ROI
print(face.shape)
# print(face.size)
# print(face.dtype)

cv2.imshow('lena_face', face)
img[180:390, 220:370] = [255, 255, 255] # 改變某區域像素
cv2.imshow('lena_filled', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
