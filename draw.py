import cv2 as cv
import numpy as np

# creating a blank image (uint8 means an image)
blank = np.zeros((500, 500), dtype="uint8")
cv.imshow("Blank", blank)


cv.waitKey(0)
