import cv2
import numpy as np
##############
widthImg,heightImg=640,480 #target image size
############
frameWidth=widthImg
frameHeight=heightImg
cap=cv2.VideoCapture(0) #0 means default webcam
cap.set(3,640) #camera width
cap.set(4,480)  #camera height
cap.set(10,150)  #brightness

def preProcessing(img):
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #imgBlur = cv2.GaussianBlur(imgGray,(5,5),1) #1 is sigma
    imgCanny=cv2.Canny(imgGray,200,200)
    kernel=np.ones((5,5))
    imgDial=cv2.dilate(imgCanny,kernel,iterations=2)
    imgThres=cv2.erode(imgDial,kernel,iterations=1)
    return imgThres

def getContours(img):
    biggest=np.array([])
    maxArea = 0
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>5000: #only draw contours if the area is larger than 500 pixls
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri=cv2.arcLength(cnt,True) #perimeter
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)  #get corner points

            if area>maxArea and len(approx)==4:
                biggest=approx
                maxArea=area
    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)
    return biggest #biggest contour

def reorder(myPoints):
    myPointsNew = np.zeros((4, 1, 2), np.int32)
    if myPoints!=[]:  # if the biggest contour exist
        myPoints=myPoints.reshape((4,2)) #convert 4*1*2 np array to 4*2 np array
        add=myPoints.sum(1)
        myPointsNew[0] = myPoints[np.argmin(add)]
        myPointsNew[3] = myPoints[np.argmax(add)]
        diff=np.diff(myPoints,axis=1)
        myPointsNew[1] = myPoints[np.argmin(diff)]
        myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew

def getWarp(img,biggest):
    biggest=reorder(biggest)
    pts1 = np.float32(biggest)  #the biggest may not follow the order as top left, top right, bottom left, bottom right
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

    imgCropped=imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20] #crop 20 pixels on each side
    imgCropped=cv2.resize(imgCropped,(widthImg, heightImg)) #resize back to original size before cropping

    return imgOutput


while True:
    success,img = cap.read()
    img=cv2.resize(img,(widthImg,heightImg))
    imgContour=img.copy()
    imgThres=preProcessing(img)
    biggest=getContours(imgThres)
    print(biggest)
    imgWarped=getWarp(img,biggest)

    cv2.imshow("video", imgContour)
    cv2.imshow("scanner", imgWarped)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break