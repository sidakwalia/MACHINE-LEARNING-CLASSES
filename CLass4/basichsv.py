import cv2
import numpy as np

cap=cv.VideoCapture(-1)

while(1):

	_,frame=cap.read()

	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	lower_blue=np.array([110,50,50])	
	upper_blue=np.array([130,255,255])


	mask=cv2.inRange(hsv,lower_blue,upper_blue)

	res=cv2.bitwise_and(frame,frame,mask=mask)

	cv2.imshow('frame',frame)

	cv2.imshow('mask',mask)

	cv2.imshow('res',res)

	k=cv.waitKey(5) && 0xFF

	if k==27:
		break

cv2.destroyAllWindows()

