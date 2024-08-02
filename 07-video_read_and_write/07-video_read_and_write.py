import cv2 as cv
import numpy as np

capture=cv.VideoCapture("necmi.mp4")

height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
count = int(capture.get(cv.CAP_PROP_FRAME_COUNT))
fps = capture.get(cv.CAP_PROP_FPS)

print("Height:", height, "Width:", width, "Frame Count:", count, "FPS:", fps)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter("necmi.avi", fourcc, fps, (width, height))

while True:

    ret,frame=capture.read()

    if ret is True:
        cv.imshow("video-input",frame)
        out.write(frame)

        cv.imshow('video-input', frame)
        if cv.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
            break

capture.release()
out.release()
cv.destroyAllWindows()
