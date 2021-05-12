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

# Rotation


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    # creating a rotation matrix
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    return cv.warpAffine(img, rotMat, (img.shape[1], img.shape[0]))


rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

cv.waitKey(0)
