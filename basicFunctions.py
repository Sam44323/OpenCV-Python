import cv2 as cv

img = cv.imread('Photos/cat.jpeg')

cv.imshow('Cats', img)

# Converting an image(bgr) to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayed Image', gray)

# Blurring an image(using the Gaussian Blur)

blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blurred', blur)

# Edge cascade (finding the edges present in an image)

canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges Cascading", canny)

cv.waitKey(0)
