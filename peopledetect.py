#-*- coding:utf-8 -*-
import cv2
import numpy as np
import sys
face_cascade_path = 'haarcascades/haarcascade_frontalface_default.xml'
eye_cascade_path = 'haarcascades/haarcascade_eye.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for x, y, w, h in faces:
        cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_gray = gray[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(face_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
sys.exit(0)