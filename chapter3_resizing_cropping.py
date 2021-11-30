import cv2
import numpy as np

img = cv2.imread("Resources/lambo.png")
print(img.shape)
print(type(img))
imgResized=cv2.resize(img,(400,200))

imgCropped=img[:200,:500]

cv2.imshow("output",img)
cv2.imshow("resized image",imgResized)
print(imgResized.shape)
cv2.imshow("cropped image",imgCropped)

cv2.waitKey(0)
