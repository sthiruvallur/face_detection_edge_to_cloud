#!/usr/bin/env python

import numpy as np
import cv2 as cv
import time

def draw_str(dst, target, s):
    x, y = target
    cv.putText(dst, s, (x+1, y+1), cv.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), thickness = 2, lineType=cv.LINE_AA)
    cv.putText(dst, s, (x, y), cv.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), lineType=cv.LINE_AA)

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        print("ERROR: A Face has not been detected")
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv.rectangle(img, (x1, y1), (x2, y2), color, 2)

def clock():
    return cv.getTickCount() / cv.getTickFrequency()

def main():
    face_cascade = cv.CascadeClassifier('/media/code/haarcascade_frontalface_default.xml')

    cap = cv.VideoCapture(0)

    while True:
        _ret, img = cap.read()
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray = cv.equalizeHist(gray)

        t = clock()
        rects = detect(gray, face_cascade)
        if len(rects) == 0:
            continue
        for x1,y1,x2,y2 in rects:
            face = gray[y1:y2, x1:x2]
            face_img = cv.imshow('face', face)
            

        vis = gray.copy()
        draw_rects(vis, rects, (0, 255, 0))
        dt = clock() - t

        draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
        cv.imshow('facedetect', vis)

        if cv.waitKey(0) & 0xFF == ord('q'):
            break
    
    cap.release()
    print('Done')

if __name__ == '__main__':
    main()
    cv.destroyAllWindows()