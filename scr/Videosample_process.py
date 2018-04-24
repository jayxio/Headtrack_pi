import cv2
capture = cv2.VideoCapture("video.avi")
while True:
    ret, img = capture.read()

    result = processFrame(img)

    cv2.imshow('some', result)
    if 0xFF & cv2.waitKey(5) == 27:
        break
cv2.destroyAllWindows()