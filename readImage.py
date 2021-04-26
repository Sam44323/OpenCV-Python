import cv2 as cv

# reading an image and capturing as matrix of pixels it using opencv
img = cv.imread('Photos/cat.jpeg')
cv.imshow('Cat', img)

cv.waitKey(0)
