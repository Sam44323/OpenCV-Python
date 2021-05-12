import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpeg')

cv.imshow('Park', img)

# Translation


def translate(img, x, y):
    # creating a translation matrix
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    return cv.warpAffine(img, transMat, (img.shape[1], img.shape[0]))

# -x ---> Left
# -y ---> Up
# x ---> Right
# y ---> Down


translated = translate(img, 100, 100)
cv.imshow('Translated', translated)


cv.waitKey(0)
