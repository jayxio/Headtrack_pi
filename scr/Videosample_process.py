import cv2

with cv2.VideoCapture("video.avi") as capture:
	while True:
		ret, img = capture.read()
		result = img#processFrame(img)
		cv2.imshow('some', result)
    		if cv2.waitKey(1) & 0xFF == ord('q'):break
cv2.destroyAllWindows()