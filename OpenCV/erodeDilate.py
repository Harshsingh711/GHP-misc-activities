import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Turn on camera")
    exit()

def nothing(x):
    pass

img = np.zeros((640, 480, 3), np.uint8)
cv.namedWindow('color')

# create trackbars
cv.createTrackbar('Hue1', 'color',0,179,nothing)
cv.createTrackbar('Sat1', 'color',0,255,nothing)
cv.createTrackbar('Val1', 'color',0,255,nothing)

cv.createTrackbar('Hue2', 'color',0,179,nothing)
cv.createTrackbar('Sat2', 'color',0,255,nothing)
cv.createTrackbar('Val2', 'color',0,255,nothing)

while True:
    # capture a frame
    ret, frame = cap.read()
    if not ret:
        print("couldn't get a frame")
        exit()
    color = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    hueValue = cv.getTrackbarPos('Hue1', 'color')
    satValue = cv.getTrackbarPos('Sat1', 'color')
    value = cv.getTrackbarPos('Val1', 'color')

    hueValue2 = cv.getTrackbarPos('Hue2', 'color')
    satValue2 = cv.getTrackbarPos('Sat2', 'color')
    value2 = cv.getTrackbarPos('Val2', 'color')

    lower = np.array([hueValue,satValue,value])
    upper = np.array([hueValue2,satValue2,value2])

    generatedMask = cv.inRange(color,lower,upper)
    kernel = np.ones((5,5), np.uint8)



    eroded = cv.erode(generatedMask, kernel, iterations = 1)
    dilated = cv.dilate(eroded, kernel, iterations = 1)

    result = cv.bitwise_and(frame,frame,mask=dilated)




    cv.imshow("frame", color)
    cv.imshow("eroded",eroded)
    cv.imshow("result",result)
    if cv.waitKey(1) == 27:
        break
    
cap.release()
cv.destroyAllWindows()