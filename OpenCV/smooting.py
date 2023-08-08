import cv2 as cv
import numpy as np

img = cv.imread("apple.png")

# kernel = np.ones((5,5), np.float32) / 9

kernel = np.array([[0,1,0,1,0],
                  [1,2,1,0,1],
                  [0,1,0,1,0]]) / 9

filtered = cv.medianBlur(img, 5)

cv.imshow("filtered img", filtered)

cv.waitKey(0)
cv.destroyAllWindows    