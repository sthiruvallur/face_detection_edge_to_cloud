import numpy as np
import cv2 as cv
import time

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

#1 should correspond to /dev/video1, your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv.VideoCapture(0)
time.sleep(2)


#Capture frame by frame
ret, frame = cap.read()

#Our operations on the frame come here
gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#Display the resulting frame
img = cv.imshow('frame', gray)

faces = face_cascade.detectMultiScale(gray,
        scaleFactor=1.5,
        minNeighbors=5)
        #minSize=(30, 30),
        #flags=cv.CASCADE_SCALE_IMAGE)

for (x,y,w,h) in faces:
    #img = cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    face = gray[y:y+h, x:x+w]
    face_img = cv.imshow('face', face)
    rc,png = cv.imencode('.png', img)
    print("Return code from imencode={}".format(rc))
    #msg = png.tobytes()



#When everything is done, release the capture
cap.release()
cv.destroyAllWindows()

