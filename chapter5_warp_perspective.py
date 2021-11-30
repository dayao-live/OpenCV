import cv2
import numpy as np

img = cv2.imread("Resources/card.webp")
print(img.shape)


cv2.line(img,(80,241),(204,228),(0,0,255),3)
cv2.line(img,(204,228),(232,400),(0,0,255),3)
cv2.line(img,(232,400),(91,423),(0,0,255),3)
cv2.line(img,(91,423),(80,241),(0,0,255),3)
pts1=np.float32([[80,241],[204,228],[91,423],[232,400]]) #top left, top right, bottom left, bottom right
width,height=250,350 #because playing is 2.5*3.5 inches, so keep the same ratio
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("card image",img)
cv2.imshow('Output',imgOutput)
cv2.waitKey(0)
