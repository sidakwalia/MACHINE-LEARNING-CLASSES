
import cv2
import numpy as np 

cap = cv2.VideoCapture(-1)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
	ret,frame = cap.read() #it is to read the frame from the video and Ret is used to obtain value from the camera frame either true or false
	gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  # because opencv works in grayscale


	faces = face_cascade.detectMultiScale(gray_frame,1.3,5)         #use that inbuild library and we will insert gray_frames
 #1.3 means that the filter size will reduce by 30 percent in the next loop


	for face in faces:
		x,y,w,h = face    #points of

		offset = 10  #	An offset value to adjust the loaded points.
		face_offset = frame[y-offset:y+h+offset,x-offset:x+w+offset]
		face_selection = cv2.resize(face_offset,(100,100))

		cv2.imshow("Face", face_selection)
		
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

	cv2.imshow("faces",frame)

	key_pressed = cv2.waitKey(1) & 0xFF
	if key_pressed == ord('x'):
		break

cap.release()
cv2.destroyAllWindows()

