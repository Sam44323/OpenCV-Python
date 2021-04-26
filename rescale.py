import cv2 as cv

img = cv.imread('Photos/cat.jpeg')
size = (1000, 1000)
resized = cv.resize(img, size)
cv.imshow('Cat', resized)

cv.waitKey(0)
