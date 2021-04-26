import cv2 as cv

img = cv.imread('Photos/cat_large.jpeg')
cv.imshow('Cat Large', img)

# function for rescaling

# frame[1] is the widht and frame[0] is the height


def rescaleFrame(frame, scale=0.75):
    width = int(frame[1] * scale)
    height = int(frame[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTure, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
