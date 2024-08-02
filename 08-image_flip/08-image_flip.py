import cv2 as cv
import numpy as np

src=cv.imread("opencv.png")

#x flip
dst1=cv.flip(src,0)
cv.imshow("x_flip",dst1)
cv.waitKey(1)

#y flip
dst2=cv.flip(src,1)
cv.imshow("y_flip",dst2)
cv.waitKey(1)

#xy flip
dst3=cv.flip(src,-1)
cv.imshow("xy_flip",dst3)
cv.waitKey(0)
