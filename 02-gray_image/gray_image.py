import cv2 as cv

image_path = "yusufdikec.jpg"
image = cv.imread(image_path)

if image is None:
    print("Resim yüklenemedi. Dosya yolunu ve dosya bütünlüğünü kontrol edin.")
else:
    print("Resim başarıyla yüklendi.")

cv.namedWindow("colored",cv.WINDOW_AUTOSIZE)
cv.imshow("colored",image)
cv.waitKey(1)

#cvtColor

gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

cv.imshow("gray", gray)
cv.waitKey(0)

#imwrite
cv.imwrite("gray_yusufdikec.png", gray)
cv.destroyAllWindows()

image = cv.imread(image_path,cv.IMREAD_GRAYSCALE)
cv.namedWindow("gray",cv.WINDOW_AUTOSIZE)
cv.imshow("gray",image)
cv.waitKey(0)

