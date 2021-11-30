import cv2
print("Package Imported")

# img = cv2.imread("Resources/lena.png")
#
# cv2.imshow("output",img)
# cv2.waitKey(1000) #1000ms
# cap=cv2.VideoCapture("Resources/test_video.mp4")
cap=cv2.VideoCapture(0) #0 means default webcam
cap.set(3,640) #width
cap.set(4,10)  #height
cap.set(10,100)  #brightness

while True:
    success,img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
