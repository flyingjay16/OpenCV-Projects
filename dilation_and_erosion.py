import cv2
import numpy as np

img = cv2.imread('rb15.jpg', cv2.COLOR_BGR2GRAY)

"""
dilation()

Adds pixel to the boundaries of objects 
in an image

erosion()

Removes pixels at the boundaries of 
objects in an image

Edge Detections is a very important area in CV, 
especially when dealing with contours

Edges can be defined as sudden changes (discontinuities)
in an image and they can encode just as much information
as pixels

Main types of edge detection:
- sobel - to emphasize vertical or horizontal edges
- laplacian - gets all orientations
- canny: optimal due to lower error rate, well defined
edges and accurate detection
    - applies guassian blurring
    - finds intensity gradient of the image
    - applied non-maximum suppression (removes pixels not edges)
    - hystersis - applies thresholds
"""

kernel = np.ones((9,9,), np.uint8)

"""hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

eroded = cv2.erode(hsv, kernel, 0)
dilate = cv2.dilate(img, kernel, 0)

cv2.imshow('erode', eroded)
cv2.imshow('dilate', dilate)"""

x = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 5)
y = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)
canny = cv2.Canny(img, 50, 120)

cv2.imshow('X',x)
cv2.imshow('Y',y)
cv2.imshow('canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()