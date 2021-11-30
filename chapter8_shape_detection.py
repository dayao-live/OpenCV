import cv2
import numpy as np

def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        if area>500: #only draw contours if the area is larger than 500 pixls
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri=cv2.arcLength(cnt,True) #perimeter
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)  #get corner points
            print(len(approx)) # print number of corners of each contour
            objCor=len(approx)
            x,y,w,h=cv2.boundingRect(approx)

            if objCor==3:
                object_type='tri'
            elif objCor==4:
                aspRatio=w/h
                if aspRatio>0.9 and aspRatio<1.1: object_type='square'
                else: object_type='rectangle'
            elif objCor>4: object_type='circle'

            else:
                object_type='None'

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,222,0),2)
            cv2.putText(imgContour, object_type, (x + (w // 2), y + (h // 2)), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                        (0, 255, 255), 2)

path='Resources/shapes.png'
img=cv2.imread(path)
imgContour=img.copy()

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny=cv2.Canny(imgBlur,50,50)
getContours(imgCanny)


cv2.imshow('original',img)
cv2.imshow('Gray',imgGray)
cv2.imshow('Blur',imgBlur)
cv2.imshow('Canny',imgCanny)
cv2.imshow('Contour',imgContour)

cv2.waitKey(0)