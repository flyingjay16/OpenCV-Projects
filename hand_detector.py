import cv2
import numpy

cap = cv2.VideoCapture(0)

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

face_file_num = 0

while(cap.isOpened):
    ret, frame = cap.read()

    if ret:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray frame', gray_frame)

        faces = face_classifier.detectMultiScale(gray_frame, 1.3, 5)

        
        if faces == ():
            print('no faces')
            cv2.putText(frame, "No Faces Found", (10, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, 3)
        else:
            print('face detected')

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)

                cv2.imwrite('./detected_face_images/face_' + str(face_file_num), frame)
                face_file_num += 1


        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cv2.destroyAllWindows()
cap.release()
