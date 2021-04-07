import cv2 as cv
import numpy as np 

# to use a camera
# camera = cv.VideoCapture(0) 
camera = cv.VideoCapture('IMG_5136.mov')

while True:
    _, frame = camera.read()

    cv.imshow('Camera', frame)

    # laplacian = cv.Laplacian(frame, cv.CV_64F)
    # laplacian = np.uint8(laplacian)
    # cv.imshow('Laplacian', laplacian)

    # adjust the frame
    edges = cv.Canny(frame, 100, 100)
    cv.imshow('Canny', edges)

    if cv.waitKey(5) == ord('x'):
        break

camera.relase()
cv.destroyAllWindows()

