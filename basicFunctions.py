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
# you can get rid of many edges by adding a lot of blur to the images

canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges Cascading", canny)

# Dilating an image

dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated ', dilated)

# Eroding an image

eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

cv.waitKey(0)
