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
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)

# 5. Drawing a circle
# cv.circle(blank, (250, 250), 100, (0, 134, 145), thickness=-1)
# # -1 also means FILLED
# cv.imshow("Circle", blank)

# 6. Drawing a line
# cv.line(blank, (0, 0), (blank.shape[1]//2,
#         blank.shape[0]//2), (0, 134, 145), thickness=3)
# cv.imshow("Line", blank)

# 7. Writing a text on an image
cv.putText(blank, "Hello!", (225, 225),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 3)
cv.imshow("Text", blank)

cv.waitKey(0)
