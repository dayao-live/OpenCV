import cv2
import numpy as np

def empty(self):
    pass

path="Resources/lambo.png"
cv2.namedWindow('sdf')
cv2.resizeWindow('sdf',480,240)

cv2.createTrackbar('hue Min','sdf',0,179,empty)
cv2.createTrackbar('hue Max','sdf',179,179,empty)
cv2.createTrackbar('Sat Min','sdf',58,255,empty)
cv2.createTrackbar('Sat Max','sdf',255,255,empty)
cv2.createTrackbar('Val Min','sdf',128,255,empty)
cv2.createTrackbar('Val Max','sdf',255,255,empty)

# img = cv2.imread(path)
# imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

frameWidth=640
frameHeight=480
cap=cv2.VideoCapture(0) #0 means default webcam
cap.set(3,frameWidth) #width
cap.set(4,frameHeight)  #height
cap.set(10,100)  #brightness
while True:
    success,img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

    h_min=cv2.getTrackbarPos('hue Min','sdf')
    h_max = cv2.getTrackbarPos('hue Max', 'sdf')
    s_min = cv2.getTrackbarPos('Sat Min', 'sdf')
    s_max = cv2.getTrackbarPos('Sat Max', 'sdf')
    v_min = cv2.getTrackbarPos('Val Min', 'sdf')
    v_max = cv2.getTrackbarPos('Val Max', 'sdf')
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    imgResult=cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("original",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("mask",mask)
    cv2.imshow("Result",imgResult)
    cv2.waitKey(1)