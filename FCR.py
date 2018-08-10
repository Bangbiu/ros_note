

# coding:utf-8

import sys
import numpy as np
    
reload(sys)

sys.setdefaultencoding('utf8')

    #    __author__ = '

    #    __date__ = '2016/9/5'

    #    __Desc__ = 

import cv2

    

imagepath = 'img.jpg'

     

   

face_cascade = cv2.CascadeClassifier('/catkin_ws/src/rbx1/rbx1_vision/data/haar_detectors/haarcascade_frontalface_alt.xml')
print(face_cascade.load('/catkin_ws/src/rbx1/rbx1_vision/data/haar_detector/haarcascade_frontalface_alt.xml'))
     

    

image = cv2.imread(imagepath)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

     

    
rect=None
faces = face_cascade.detectMultiScale(gray,1.3,5)

     
print "find{0}".format(len(faces))

     
for(x,y,w,h) in faces:

        # cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)

	cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)

     

	cv2.imshow("Find Faces!",image)

	cv2.waitKey(0)

