import cv2 as cv

img = cv.imread('Photos/cat.jpeg')

cv.imshow('Cats', img)

# Converting an image(bgr) to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayed Image', gray)

cv.waitKey(0)
