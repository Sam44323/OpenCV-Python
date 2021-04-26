import cv2 as cv
import numpy as np

# creating a blank image (uint8 means an image)
blank = np.zeros((500, 500, 3), dtype="uint8")

# 1. Paint the image a certain colour
# blank[:] = 0, 255, 0  # painting the entire image green
# cv.imshow("Green", blank)

# 2. Painting a certain portion of the image
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Multi', blank)

# 3. Drawing a rectangle
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=3)
# cv.imshow('Rectangle', blank)

# 4. Filling the rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

cv.waitKey(0)
