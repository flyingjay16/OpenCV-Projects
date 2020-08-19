import cv2
import numpy as np

img = cv2.imread('rb15.jpg')
"""B, G, R = cv2.split(img)

zeros = np.zeros(img.shape[:2], dtype = "uint8")

cv2.imshow("B", cv2.merge([B, zeros, zeros]))
cv2.imshow("G", cv2.merge([zeros, G, zeros]))
cv2.imshow("R", cv2.merge([zeros, zeros, R]))

cv2.imshow("Merged", cv2.merge([B, G, R + 100]))"""

hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv_image)
cv2.imshow('Hue Channel', hsv_image[:, :, 0])
cv2.imshow('Saturation Channel', hsv_image[:, :, 1])
cv2.imshow('Value Channel', hsv_image[:, :, 2])

cv2.waitKey(0)
cv2.destroyAllWindows()

