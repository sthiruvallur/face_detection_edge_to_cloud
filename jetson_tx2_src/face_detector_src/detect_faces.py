import numpy as np
import cv2 as cv
import time
import pdb


#1 should correspond to /dev/video1, your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')

if not cap.isOpened():
    print("Cannot open camera")
    exit()
status = True
#pdb.set_trace()

while(status):
    #Capture frame by frame
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    #frame = cv.imread('/media/code/homework_3/face_detection_edge_to_cloud/jetson_tx2_src/face_detector_src/satya_face.jpg', cv.IMREAD_GRAYSCALE)
    #frame = cv.imread('/media/code/homework_3/face_detection_edge_to_cloud/jetson_tx2_src/face_detector_src/satya_face.jpg')
    #frame = cv.imread('satya_face.jpg')
    #print("frame returned from cv.imread is {}".format(frame))
    
    #Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.equalizeHist(gray)
    
    #Display the resulting frame
    #img = cv.imshow('frame', gray)

    #time.sleep(10)
    
    faces = face_cascade.detectMultiScale(gray,
        scaleFactor=1.3,
        minNeighbors=4,
        flags=cv.CASCADE_SCALE_IMAGE,
        minSize=(30,30))
            
    for (x,y,w,h) in faces:
        print("In this loop with (x,y,w,h)=({},{},{},{})".format(x,y,w,h))
        #img = cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        face = gray[y:y+h, x:x+w]
        face_img = cv.imshow('face', face)
        #time.sleep(30)
        rc,png = cv.imencode('.png', face_img)
        print("Return code from imencode={}".format(rc))
        msg = png.tobytes()

    #time.sleep(20)

    #if cv.waitKey(0) & 0xFF == ord('q'):
        #break

#When everything is done, release the capture
cap.release()
cv.destroyAllWindows()

