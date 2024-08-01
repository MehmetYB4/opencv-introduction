import cv2 as cv
import numpy as np

image_path= "yusufdikec.jpg"
image=cv.imread(image_path)

cv.namedWindow("image_create",cv.WINDOW_AUTOSIZE)
cv.imshow("image_create",image)
cv.waitKey(1)

m1=np.copy(image)
m2=image

print(image[100:200, 200:300, :])
image[100:200, 200:300, :]=0

cv.imshow("m2",m2)
cv.waitKey(1)

m3=np.zeros(image.shape,image.dtype)
cv.imshow("m3",m3)
cv.waitKey(1)

m4=np.zeros([512,512],image.dtype)
cv.imshow("m4",m4)
cv.waitKey(1)

m5=np.zeros([512,512],np.dtype)
m5[:,:]=127
cv.imshow("m5",m5)
cv.waitKey(1)

cube = np.zeros((500, 500, 3), dtype=np.uint8)
points = np.array([
    [100, 100],  # A
    [200, 100],  # B
    [200, 200],  # C
    [100, 200],  # D
    [150, 150],  # E
    [250, 150],  # F
    [250, 250],  # G
    [150, 250]   # H
])

color = (0, 255, 0)
thickness = 2

# Ön yüz
cv.line(cube, tuple(points[0]), tuple(points[1]), color, thickness)
cv.line(cube, tuple(points[1]), tuple(points[2]), color, thickness)
cv.line(cube, tuple(points[2]), tuple(points[3]), color, thickness)
cv.line(cube, tuple(points[3]), tuple(points[0]), color, thickness)

# Arka yüz
cv.line(cube, tuple(points[4]), tuple(points[5]), color, thickness)
cv.line(cube, tuple(points[5]), tuple(points[6]), color, thickness)
cv.line(cube, tuple(points[6]), tuple(points[7]), color, thickness)
cv.line(cube, tuple(points[7]), tuple(points[4]), color, thickness)

# Bağlantı çizgileri
cv.line(cube, tuple(points[0]), tuple(points[4]), color, thickness)
cv.line(cube, tuple(points[1]), tuple(points[5]), color, thickness)
cv.line(cube, tuple(points[2]), tuple(points[6]), color, thickness)
cv.line(cube, tuple(points[3]), tuple(points[7]), color, thickness)

cv.imshow("Cube", cube)
cv.waitKey(0)
cv.destroyAllWindows()


