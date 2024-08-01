import cv2 as cv


# Dosya yolunu kontrol edin
image_path = "yusufdikec.jpg"
image = cv.imread(image_path)

if image is None:
    print("Resim yüklenemedi. Dosya yolunu ve dosya bütünlüğünü kontrol edin.")
else:
    print("Resim başarıyla yüklendi.")

print(type(image))

#namedWindow
cv.namedWindow("opencv_test",cv.WINDOW_AUTOSIZE)

#imshow
cv.imshow("opencv_test",image)
cv.waitKey()

cv.destroyAllWindows()
