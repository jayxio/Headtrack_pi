'''
Created on Apr 15, 2018

A face detection program that use basic function in OpenCV3 on Pi3

It's a practice

@author: sadde
'''

import io
from time import sleep
import picamera
import numpy as np
import cv2


if __name__ == '__main__':
    face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.4.0/data/haarcascades/haarcascade_frontalface_alt.xml')
    eye_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.4.0/data/haarcascades/haarcascade_eye.xml')
    
    with picamera.PiCamera() as camera:
    	camera.resolution = (320,240)
    	# camera.framerate = 24
    	sleep(1)
    	stream = io.BytesIO()
    	for foo in camera.capture_continuous(stream, format='jpeg', use_video_port=True):
    		data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    		image = cv2.imdecode(data, cv2.IMREAD_COLOR)
    		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    		cv2.imshow('gray',gray)
    		# detect faces and get coordinations
    		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    		# detect eyes based on face detection results
    		for (x,y,w,h) in faces:
    			cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    			roi_gray = gray[y:y+h, x:x+w]
    			roi_color = image[y:y+h, x:x+w]
    			eyes = eye_cascade.detectMultiScale(roi_gray)
    			for (ex,ey,ew,eh) in eyes:
    				cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    		
    		cv2.imshow('img', image)
    		# Truncate the stream to the current position
    		# in case prior interation output a longer image
    		stream.truncate()
    		stream.seek(0)
    		
    		if cv2.waitKey(1) & 0xFF == ord('q'): break
  
    
    
    