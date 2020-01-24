#import numpy as np
import cv2
import time


#cap = cv2.VideoCapture(0, cv2.CAP_V4L)
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("gst-launch-1.0 nvarguscamerasrc ! nvvidconv ! xvimagesink")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
if not cap.isOpened():
    print("Cannot open camera")
    exit()
status = True

while(status):
    #time.sleep(2)
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Display the resulting frame
    img = cv2.imshow('frame', gray)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

    #faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    #status = False

#time.sleep(5)
#When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
