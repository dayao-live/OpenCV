import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur= cv2.GaussianBlur(imgGray,(7,7),0,)  #kernal size is 7*7
imgCanny=cv2.Canny(img,100,100) #Canny image detector, 100 and 100 are threshold 1 and threshold 2

kernel=np.ones((5,5),np.uint8)
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded=cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny,)
cv2.imshow("ImgDialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)