'''
Created on Apr 15, 2018

A face detection program that use basic function in OpenCV3

It's a practice

@author: sadde
'''
import cv2 as cv

if __name__ == '__main__':
    face_cascade = cv.CascadeClassifier('C:\\Users\\sadde\\git\\Headtrack_pi\\scr\\cascadG.xml')#_upperbody.xml')
    #eye_cascade = cv.CascadeClassifier('C:\Program Files\opencv\sources\data\haarcascades\haarcascade_eye.xml')
    
    video_capture = cv.VideoCapture("sample1.mp4")
    
    while True:
        ret, frame = video_capture.read()
        
        img = frame
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        
        '''
        cv.namedWindow('img')
        cv.imshow('img', img)
        cv.waitKey(0)
        
        cv.namedWindow('grey')
        cv.imshow('grey', grey)
        cv.waitKey(0)
        '''
        
        faces = face_cascade.detectMultiScale(gray,1.04, 4)
        for (x,y,w,h) in faces:
            cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            '''
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            '''
        cv.namedWindow('img')
        cv.imshow('img', img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    video_capture.release()
    cv.destroyAllWindows()    
    
    
    