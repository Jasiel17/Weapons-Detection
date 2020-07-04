import numpy as np 
import cv2 

gun_cascade = cv2.CascadeClassifier('cascade.xml') 
#camera = cv2.VideoCapture('video.mp4') 
img = cv2.imread('93.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#firstFrame = None
#gun_exist = False


guns = gun_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y , w ,h) in guns:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)


cv2.imshow('img', img)
cv2.waitKey() 