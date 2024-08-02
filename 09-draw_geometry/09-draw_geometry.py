import numpy as np
import cv2 as cv

image = np.zeros((512,512,3),dtype=np.uint8)

cv.rectangle(image, (100, 100), (300, 300), (255, 0, 0), 2, cv.LINE_8, 0)

cv.circle(image, (256, 256), 50, (0, 255, 0), 2, cv.LINE_8, 0)

cv.ellipse(image, (256, 256), (150, 50), 360, 0, 360, (0, 0, 255), 2, cv.LINE_8, 0)

cv.imshow("Shapes", image)
cv.waitKey(1)

image = np.zeros((512, 512, 3), dtype=np.uint8)

for i in range(100000):
    # (siyah)
    image[:, :, :] = 0

    # Rastgele koordinatlar
    x1 = np.random.rand() * 512
    y1 = np.random.rand() * 512
    x2 = np.random.rand() * 512
    y2 = np.random.rand() * 512
    # Rastgele renkler
    b = np.random.randint(0, 256)
    g = np.random.randint(0, 256)
    r = np.random.randint(0, 256)
    color = (b, g, r)

    # Rastgele çizgi
    cv.line(image, (int(x1), int(y1)), (int(x2), int(y2)), color, 4, cv.LINE_8, 0)

    # Rastgele kare
    top_left = (np.random.randint(0, 512), np.random.randint(0, 512))
    bottom_right = (np.random.randint(top_left[0], 512), np.random.randint(top_left[1], 512))
    cv.rectangle(image, top_left, bottom_right, color, 1, cv.LINE_8, 0)

    # Rastgele daire
    center = (np.random.randint(0, 512), np.random.randint(0, 512))
    radius = np.random.randint(10, 100)
    cv.circle(image, center, radius, color, 2, cv.LINE_8, 0)

    # Rastgele elips
    center = (np.random.randint(0, 512), np.random.randint(0, 512))
    axes = (np.random.randint(20, 100), np.random.randint(20, 100))
    angle = np.random.randint(0, 360)
    start_angle = 0
    end_angle = 360
    cv.ellipse(image, center, axes, angle, start_angle, end_angle, color, 2, cv.LINE_8, 0)

    cv.imshow("image", image)
    c = cv.waitKey(20)
    if c == 27:  # ESC
        break

cv.destroyAllWindows()