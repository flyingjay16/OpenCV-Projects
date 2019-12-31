import cv2
import numpy as np

def nothing():
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)


while True:
    #frame = cv2.imread('watch.jpg')
    _, frame = cap.read()

    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    u_h = cv2.getTrackbarPos("UH", "Tracking")

    l_s = cv2.getTrackbarPos("LS", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")

    l_v = cv2.getTrackbarPos("LV", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    low_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv_img, low_bound, upper_bound)

    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()