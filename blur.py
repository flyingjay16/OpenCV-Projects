import cv2
import numpy as np

img = cv2.imread('watch.jpg')

kernel_3 = np.ones((3,3),np.float32)/9
kernel_7 = np.ones((7,7), np.float32)/49

blur_1 = cv2.filter2D(img, -1, kernel_3)
cv2.imshow('blur1', blur_1)

blur_2 = cv2.filter2D(img, -1, kernel_7)
cv2.imshow('blur2', blur_2)

g_blur = cv2.blur(img, (3,3), 0)
cv2.imshow('g_blur', g_blur)

g_blur = cv2.GaussianBlur(img, (3,3), 0)
cv2.imshow('g_blur', g_blur)

m = cv2.medianBlur(img, 3)
cv2.imshow('m', m)


cv2.waitKey(0)
cv2.destroyAllWindows()