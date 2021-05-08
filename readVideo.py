import cv2 as cv
# reading videos in opencv
# you will pass integer value to VideoCapture if you are using your webcam or camera

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTure, frame = capture.read()  # getting the video frame by frame
    cv.imshow('Video', frame)  # showing each frames

    # this means if the letter d is pressed then stop displaying the video
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()  # release the capture device
cv.destroyAllWindows()  # destroy the windows
