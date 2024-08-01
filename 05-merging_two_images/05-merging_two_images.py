import cv2 as cv
import numpy as np

#başka bir ekleme çeşidi
image1=cv.imread("opencv.png")
image2=cv.imread("opencv.png")

cv.imshow("resim1",image1)
cv.waitKey()

cv.imshow("resim2",image2)
cv.waitKey()

#merge
horizontal=np.hstack((image1,image2))
cv.imshow("merged",horizontal)
cv.waitKey()
cv.destroyAllWindows()