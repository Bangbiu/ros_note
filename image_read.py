import numpy as np
import cv2
cv2.namedWindow('HEHE',0)
img = cv2.imread('img.jpg')
cv2.imshow('1',img)
cv2.imshow('2',img)
##tb1=cv2.createTrackbar('tb','1',654,3,None)
cv2.moveWindow('HEHE',0,0)
cv2.resizeWindow('HEHE',500,500)
cv2.waitKey(0)
cv2.destoryAllWindows()

