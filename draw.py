import cv2 as cv
import numpy as np

# creating a blank image (uint8 means an image)
blank = np.zeros((500, 500, 3), dtype="uint8")

# 1. Paint the image a certain colour
blank[:] = 0, 255, 0  # painting the entire image green

cv.imshow("Blank", blank)
cv.waitKey(0)
