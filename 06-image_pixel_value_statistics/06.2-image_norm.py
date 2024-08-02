import cv2 as cv
import numpy as np

src = cv.imread("opencv.png")
print("Original Image Shape:", src.shape)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)
cv.waitKey(1)

print("Gray Image Shape:", gray.shape)

gray = np.float32(gray)
print("Gray Image as float32:\n", gray)
means, stddev = cv.meanStdDev(gray)
print("Mean: %.2f, StdDev: %.2f" % (means, stddev))

# norm_minmax
dst_minmax = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst_minmax, alpha=0, beta=1.0, norm_type=cv.NORM_MINMAX)
print("Normalized Image (Min-Max):\n", dst_minmax)
print("Normalized Image (Min-Max) as int8:\n", np.int8(dst_minmax * 255))
means, stddev = cv.meanStdDev(np.int8(dst_minmax * 255))
print("Mean (Min-Max): %.2f, StdDev (Min-Max): %.2f" % (means, stddev))
cv.imshow("Normalized Min-Max", dst_minmax)
cv.waitKey(0)

# norm_INF
dst_inf = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst_inf, alpha=0, beta=1.0, norm_type=cv.NORM_INF)
cv.imshow("Normalized INF", dst_inf)
cv.waitKey(0)

# norm_L1
dst_l1 = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst_l1, alpha=0, beta=1.0, norm_type=cv.NORM_L1)
cv.imshow("Normalized L1", dst_l1)
cv.waitKey(0)

# norm_L2
dst_l2 = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst_l2, alpha=0, beta=1.0, norm_type=cv.NORM_L2)
cv.imshow("Normalized L2", dst_l2)
cv.waitKey(0)

cv.destroyAllWindows()
