'''
Created on Apr 15, 2018

A face detection program that use basic function in OpenCV3

It's a practice

@author: sadde
'''
import cv2 as cv
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('view-stream.html')

@app.route('/<order>')
def order(order):
    if order=='forward':
        return 'forward'
    elif order=='left':
        return 'left'
    elif order=='right':
        return 'right'
    elif order=='back':
        return 'back'
    else:
        return order

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    #face_cascade = cv.CascadeClassifier('cascadG.xml')#_upperbody.xml')
    #face_cascade = cv.CascadeClassifier('cascadeH5.xml')
    face_cascade = cv.CascadeClassifier('heads_cascade.xml')
    #face_cascade = cv.CascadeClassifier('HS.xml')
    
    video_capture = cv.VideoCapture("sample.mp4")
    
    # only when count down equals to 0 can the sub detection zones detect new heads
    # count down for upper sub detection zone
    detection_bar_upper_countdown = 0
    inCountWaittime = 0
    
    block1_upper_countdown = 0
    block2_upper_countdown = 0
    block3_upper_countdown = 0
    block4_upper_countdown = 0
    
    # count down for upper sub detection zone
    detection_bar_lower_countdown = 0
    outCountWaittime = 0
    
    block1_lower_countdown = 0
    block2_lower_countdown = 0
    block3_lower_countdown = 0
    block4_lower_countdown = 0
    
    # number of in and out
    inNum = 0
    outNum = 0
    numofpeople = 40
    
    success = True
    while success:
        success , img = video_capture.read()
        
        img = cv.resize(img,(320,240))
        
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        #print(gray.shape)
        width, length = gray.shape # width now is 240, length is 320
        
        bar_upper_upperedge = int(width*0.05)
        bar_upper_loweredge = 110
        bar_lower_loweredge = int(width*0.95)
        bar_lower_upperedge = 120
        
        '''
        cv.namedWindow('img')
        cv.imshow('img', img)
        cv.waitKey(0)
        
        cv.namedWindow('grey')
        cv.imshow('grey', grey)
        cv.waitKey(0)
        '''
        
        #heads = face_cascade.detectMultiScale(gray, 1.04, 4, minSize=(40,40), maxSize=(80,80)) # HS
        #heads = face_cascade.detectMultiScale(gray, 1.2, 3, minSize=(60,60) ) # cascadeH5
        #heads = face_cascade.detectMultiScale(gray, 1.1, 7, minSize=(70,70) ) # cascadG
        heads = face_cascade.detectMultiScale(gray, 1.03,minNeighbors=5, minSize=(60,60), maxSize=(150,150) ) # heads_cascade
        
        
        
        # upper and lower detection zones
        detection_bar_upper = img[bar_upper_upperedge:bar_upper_loweredge, 0:length]
        detection_bar_lower = img[bar_lower_upperedge:bar_lower_loweredge, 0:length]
        
        # upper detecting block
        block1_upper = img[bar_upper_upperedge:bar_upper_loweredge, 0:int(length/4)]
        block2_upper = img[bar_upper_upperedge:bar_upper_loweredge, int(length/4):int(length/4*2)]
        block3_upper = img[bar_upper_upperedge:bar_upper_loweredge, int(length/4*2):int(length/4*3)]
        block4_upper = img[bar_upper_upperedge:bar_upper_loweredge, int(length/4*3):int(length/4*4)]
        
        # lower detecting block
        block1_lower = img[bar_lower_upperedge:bar_lower_loweredge, 0:int(length/4)]
        block2_lower = img[bar_lower_upperedge:bar_lower_loweredge, int(length/4):int(length/4*2)]
        block3_lower = img[bar_lower_upperedge:bar_lower_loweredge, int(length/4*2):int(length/4*3)]
        block4_lower = img[bar_lower_upperedge:bar_lower_loweredge, int(length/4*3):int(length/4*4)]
        
        #print(detection_bar_upper.shape)
        
        # upper and lower detection zone
        detection_bar_upper_width, detection_bar_upper_length, _ = detection_bar_upper.shape
        detection_bar_lower_width, detection_bar_lower_length, _ = detection_bar_lower.shape
        
        # upper block dimension
        block1_upper_width, block1_upper_length, _ = block1_upper.shape
        block2_upper_width, block2_upper_length, _ = block2_upper.shape
        block3_upper_width, block3_upper_length, _ = block3_upper.shape
        block4_upper_width, block4_upper_length, _ = block4_upper.shape
        # lower block dimension
        block1_lower_width, block1_lower_length, _ = block1_lower.shape
        block2_lower_width, block2_lower_length, _ = block2_lower.shape
        block3_lower_width, block3_lower_length, _ = block3_lower.shape
        block4_lower_width, block4_lower_length, _ = block4_lower.shape
        # draw upper and lower detection zone
        cv.rectangle(detection_bar_upper,(0,0),(detection_bar_upper_length,detection_bar_upper_width-1),(0,255,0),1)
        cv.rectangle(detection_bar_lower,(0,0),(detection_bar_lower_length,detection_bar_lower_width-1),(0,255,0),1)
        
        # draw upper sub detection zones
        cv.rectangle(block1_upper,(0,0),(block1_upper_length,block1_upper_width),(0,255,0),1)
        cv.rectangle(block2_upper,(0,0),(block2_upper_length,block2_upper_width),(0,255,0),1)
        cv.rectangle(block3_upper,(0,0),(block3_upper_length,block3_upper_width),(0,255,0),1)
        cv.rectangle(block4_upper,(0,0),(block4_upper_length,block4_upper_width),(0,255,0),1)
        
        # draw lower sub detection zones
        cv.rectangle(block1_lower,(0,0),(block1_lower_length,block1_lower_width),(0,255,0),1)
        cv.rectangle(block2_lower,(0,0),(block2_lower_length,block2_lower_width),(0,255,0),1)
        cv.rectangle(block3_lower,(0,0),(block3_lower_length,block3_lower_width),(0,255,0),1)
        cv.rectangle(block4_lower,(0,0),(block4_lower_length,block4_lower_width),(0,255,0),1)
        
        # draw boxes for them and check which block do the heads land in
        for (x,y,w,h) in heads:
            # cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
            headcentre_x = int(x+w/2)
            headcentre_y = int(y+h/2)
            #print(headcentre_x,headcentre_y)
            #cv.rectangle(img,(x,y),(headcentre_x,headcentre_y),(255,0,255),1)
            
            # check location
            if headcentre_y>bar_upper_upperedge and headcentre_y<bar_upper_loweredge:
                # only count after a while
                if detection_bar_lower_countdown > 0:
                    if inCountWaittime == 0:
                        inNum += 1
                        numofpeople += 1
                        print('inNum=',inNum)
                        inCountWaittime = 40
                    else:
                        pass
                    
                detection_bar_upper_countdown = 10
                if headcentre_x>0 and headcentre_x<int(length/4):
                    cv.rectangle(block1_upper,(0,0),(block1_upper_length,block1_upper_width),(0,0,255),4)
                    
                elif headcentre_x>int(length/4) and headcentre_x<int(length/4*2):
                    cv.rectangle(block2_upper,(0,0),(block1_upper_length,block1_upper_width),(0,0,255),4)
                    
                elif headcentre_x>int(length/4*2) and headcentre_x<int(length/4*3):
                    cv.rectangle(block3_upper,(0,0),(block1_upper_length,block1_upper_width),(0,0,255),4)
                    
                elif headcentre_x>int(length/4*3) and headcentre_x<int(length/4):
                    cv.rectangle(block4_upper,(0,0),(block1_upper_length,block1_upper_width),(0,0,255),4)
                else:
                    pass
                 
                    
            elif headcentre_y>bar_lower_upperedge and headcentre_y<bar_lower_loweredge:
                # count one out after a while
                if detection_bar_upper_countdown > 0:
                    if outCountWaittime == 0:
                        outNum += 1
                        numofpeople -= 1
                        print('outNum=',outNum)
                        outCountWaittime = 40
                    else:
                        pass
                
                detection_bar_lower_countdown = 10
                if headcentre_x>0 and headcentre_x<int(length/4):
                    cv.rectangle(block1_lower,(0,0),(block1_lower_length,block1_lower_width),(0,0,255),4)
                    
                elif headcentre_x>int(length/4) and headcentre_x<int(length/4*2):
                    cv.rectangle(block2_lower,(0,0),(block1_lower_length,block1_lower_width),(0,0,255),4)
                    
                elif headcentre_x>int(length/4*2) and headcentre_x<int(length/4*3):
                    cv.rectangle(block3_lower,(0,0),(block1_lower_length,block1_lower_width),(0,0,255),4)
                    
                elif headcentre_x>int(length/4*3) and headcentre_x<int(length/4):
                    cv.rectangle(block4_lower,(0,0),(block1_lower_length,block1_lower_width),(0,0,255),4)
                else:
                    pass
                
                
            else:
                pass
            
            '''
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            '''
        
           
        if detection_bar_upper_countdown>0:
            cv.rectangle(detection_bar_upper,(0,0),(detection_bar_upper_length,detection_bar_upper_width-1),(0,0,255),4)
            detection_bar_upper_countdown -= 1
        else:
            detection_bar_upper_countdown = 0
            
        if detection_bar_lower_countdown>0:
            cv.rectangle(detection_bar_lower,(0,0),(detection_bar_lower_length,detection_bar_lower_width-1),(0,0,255),4)
            detection_bar_lower_countdown -= 1
        else:
            detection_bar_lower_countdown = 0
            
        if inCountWaittime>0:
            inCountWaittime -= 1
        else:
            inCountWaittime=0
            
        if outCountWaittime>0:
            outCountWaittime -= 1
        else:
            outCountWaittime=0
        
        font = cv.FONT_HERSHEY_SIMPLEX
        
        text = 'Number of people:'+str(numofpeople) # 'Number of In:'+str(inNum)+'  '+'Number of Out:'+str(outNum)+' 
        print(text)
        cv.putText(img, text, (0,10), font, 0.5, (0,255,255), 2, cv.LINE_AA)
        

        
        cv.namedWindow('img')
        cv.imshow('img', img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    video_capture.release()
    cv.destroyAllWindows()    
    
    
    