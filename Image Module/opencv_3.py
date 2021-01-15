"""
使用opencv操作影像

三、在圖像上繪製和寫字
原文網址：https://kknews.cc/code/gg2bej8.html
"""

import numpy as np
import cv2

img = cv2.imread('lena.png', cv2.IMREAD_COLOR)
"""
draw line, rectangle
cv2.rectangle(img, start point, end point, color, width)
"""
# cv2.line(img, (0, 0), (150, 150), (255, 255, 255), 15)
# cv2.rectangle(img, (200, 200), (300, 300), (255, 255, 255), 15)

"""
circle
"""
cv2.circle(img, (100, 64), 55, (255, 255, 255), -1) # -1 means full-fill the shape

"""
polylines 折線
"""
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# pts = pts.reshape((-1, 1, 2)) # 不知道目的是什麼
cv2.polylines(img, [pts], True, (255, 255, 255), 1)

"""
write words
"""
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Hello image', (200, 200), font, 1, (255, 255, 255), 2, cv2.LINE_AA)


cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

