import cv2 as cv
import numpy as np

image_path= "opencv.png"
image=cv.imread(image_path)

h, w, ch=image.shape
print("h, w, ch", h, w, ch)

for row in range(h):
    for col in range(w):
        b, g, r = image[row,col]
        b= 255 - b
        g= 255 - g
        r= 255 - r
        image[row,col]=[b,g,r]

cv.imshow("output",image)
cv.waitKey(1)
cv.destroyAllWindows()
