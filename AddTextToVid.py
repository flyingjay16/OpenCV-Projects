import cv2

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Resolution cannot be actuall be set to 1280 x 780
#Max resolution on the web cam is 640 X 480
cap.set(3, 1280)
cap.set(4, 720)

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + " Height: " + str(cap.get(4))

        frame = cv2.putText(frame, text, (10, 50), font, 1, (255, 0, 0), 1, cv2.LINE_AA)

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
        

cap.release()
cv2.destroyAllWindows()