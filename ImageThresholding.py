import cv2
import numpy as np

img = cv2.imread('rb15.jpg', 0)
_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("Image", img)
cv2.imshow("Threshold", th1)
cv2.imshow("Threshold Bin Inv", th2)
cv2.imshow("Threshold Trunc", th3)
cv2.imshow("Threshold Zero", th4)
cv2.imshow("Threshold Zero Inv", th5)

cv2.waitKey(0)
cv2.destroyAllWindows()