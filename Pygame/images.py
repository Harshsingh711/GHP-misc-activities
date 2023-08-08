import cv2 as cv

img1 = cv.imread("avocado.png")
img2 = cv.imread("fire.png")
height_im1 = img1.shape[0]
width_im1 = img1.shape[1]

height_im2 = img2.shape[0]
width_im2 = img2.shape[1]

minHeight = min(height_im1, height_im2)
minWidth = min(width_im1, width_im2)

cropped_im1 = img1[0:minHeight, 0:minWidth]
cropped_im2 = img2[0:minHeight, 0:minWidth]

img3 = cv.add(cropped_im1, cropped_im2),

secondWeight = .1
firstWeight = .9

cv.imshow("start", img1)
key = cv.waitKey(0)
if key == 100:
    while (secondWeight < 1):
        weightedImage = cv.addWeighted(cropped_im1, firstWeight, cropped_im2, secondWeight, 0)
        cv.imshow("gradient", weightedImage)
        secondWeight += .002
        firstWeight -= .002
        key = cv.waitKey(15)
        if key == 27:
            cv.destroyAllWindows()
            exit()
exit()
    



# while True:
#     cv.imshow("apple.png", img1)
#     key = cv.waitKey(0)
#     cv.destroyAllWindows()
#     if key == int(100):
#         cv.imshow("combined", weightedImage)
#         key = cv.waitKey(0)
#         cv.destroyAllWindows()

#     if key == 27: # Esc
#         cv.destroyAllWindows()
#         break
