import cv2 as cv
import numpy as np

SavedIm = cv.imread('savedIm.png')
savedMask = cv.imread('savedMask.png')
savedMask = cv.cvtColor(savedMask, cv.COLOR_BGR2GRAY)
savedResult = cv.imread('savedResult.png')

contours, heirarchy = cv.findContours(savedMask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(savedResult,contours,-1, (0,255,255), 5)

area = cv.contourArea(contours[0])
i = 0
sortedContours = [None]*100
for x in contours:
    sortedContours[i] = cv.contourArea(contours[i])

sortedContours.sort()

M = cv.moments(sortedContours[1])

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

cv.imshow("contours", savedResult)

cv.waitKey(0)
cv.destroyAllWindows