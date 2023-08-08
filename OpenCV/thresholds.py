import cv2 as cv
import numpy as np

img = cv.imread("apple.png")

converted = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


ret, thresholded = cv.threshold(converted, 127, 255, cv.THRESH_TRUNC)

cv.imshow('thresholded', thresholded)

cv.waitKey(0)
cv.destroyAllWindows()