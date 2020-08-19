import cv2
import numpy as np

"""
resize()

Change the width and heigh of an image

scaling()

Change the size but keep the width: height ratio
Width: height ratio also known as aspect ratio

interpolation

Method of constructing new data points within the range
of a discrete set of known data points

Enlargening Images:

cv2.INTER_AREA()

Good for shrinking or down sampling

cv2.INTER_NEAREST()

Fastest

cv2.INTER_LINEAR

Good for z4ooming or up sampling

cv2.INTER_CUBIC 

Better

cv2.INTER_LANCZOS4

Best

Image Pyramids: Up scaling (enlarging) and downscaling (shrinking)
Cropping images refer to extracting a segment of that image

"""

img = cv2.imread('rb15.jpg')

image_scaled = cv2.resize(img, None, fx = 0.25, fy = 0.25)
cv2.imshow('Scaling - Linear Interpolation', image_scaled)

image_scaled = cv2.resize(img, None, fx = 0.25, fy = 0.25, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Scaling - Cubic Interpolation', image_scaled)

image_scaled = cv2.resize(img, None, fx = 0.25, fy = 0.25, interpolation=cv2.cv2.INTER_NEAREST)
cv2.imshow('Scaling - Inter Nearest', image_scaled)

image_scaled = cv2.resize(img, (900, 400), interpolation=cv2.INTER_AREA)
cv2.imshow('Scaling - Skewed size', image_scaled)


#more useful for object detection
smaller = cv2.pyrDown(img)
larger = cv2.pyrUp(smaller)

cv2.imshow('Larger', larger)


height, width = img.shape[:2]

start_row, start_col = int(height * 0.25), int(height * 0.25)
end_row, end_col = int(height * 0.75), int(height * 0.75)

cropped = img[start_row:end_row, start_col:end_col]
cv2.imshow('cropped', cropped)




cv2.waitKey(0)
cv2.destroyAllWindows()