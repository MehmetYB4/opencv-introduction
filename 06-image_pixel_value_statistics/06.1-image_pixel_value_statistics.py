import cv2 as cv
import numpy as np

src=cv.imread("opencv.png",cv.IMREAD_GRAYSCALE)

#minMaxloc

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(src)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))
print("min_loc:",min_loc,"," , "max_loc:" , max_loc)

#meanStdDev
means,stddev=cv.meanStdDev(src)
print("mean: %.2f, stddev: %.2f" % (means,stddev))

src[np.where(src < means)]= 0
src[np.where(src > means)]= 255

cv.imshow("binary",src)
cv.waitKey()