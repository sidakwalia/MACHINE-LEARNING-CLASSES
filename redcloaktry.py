import cv2
import numpy as np
import time

cap = cv2.videoCapture(0)
time.sleep(3)
count = 0
background = 0

for i in range(60):
	ret, background = cap.read()

background = np.flip(background, axis=1)

while(cap.isOpened()):

	ret, img = cap.read()
	if not ret:
		break
	count+=1
	img = np.flip(img, axis=1)

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	lower_red = ([])
	upper_red = ([])
	mask1 = cv2.inRange(hsv, lower_red, upper_red)

	mask1 = mask1+mask2
	
