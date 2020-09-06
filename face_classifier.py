import numpy as np
import cv2

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread('face.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )

faces = face_classifier.detectMultiScale(gray, 1.3, 5)

if faces == ():
    cv2.putText(img, "No Faces Found", (10, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, 3)
    cv2.imshow('img', img)
    cv2.waitKey(0)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow('Face Detection', img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
