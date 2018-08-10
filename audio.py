import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
	CX=250
	CY=150
	H=80
	ret,frame = cap.read()
	#gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	gray =frame

	dst = np.copy(gray)

	for i in range(1,31,2):dst=cv2.blur(gray,(i,i))

	for i in range(CY-H,CY,3):cv2.line(dst,(CX-100,i),(CX+100,i),(0,255,0),3)
	cv2.ellipse(dst,(CX,CY),(150,30),0,0,360,(0,255,0),-1)
	cv2.ellipse(dst,(CX,CY-H),(100,30),0,0,360,(0,255,0),-1)


	#for i in range(1,31,2):dst=cv2.blur(dst,(i,i))

	##face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')




	cv2.imshow('frame',dst) 
	#cv2.resizeWindow('frame',1000,1000)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destoryAllWindows()

