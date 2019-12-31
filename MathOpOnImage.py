import numpy as np
import cv2

img = cv2.imread('watch.jpg')
img2 = cv2.imread('rb15.jpg')

print(img.shape) #returns a tuple of nnumber of rows, columns, and channels
print(img.size) #returns amount of pixels access
print(img.dtype) #returns image datatype

b, g, r = cv2.split(img)
img = cv2.merge((b,g,r))

#img[startX:endX, startY: endY]
watch_face = img[500:1000, 200:1000]
img[600:1100, 300:1100] = watch_face

#cv2.imshow('image', img)

img = cv2.resize(img, (1024, 512))
img2 = cv2.resize(img2, (1024, 512))

dst = cv2.add(img, img2)
dst_with_weight = cv2.addWeighted(img, 0.3, img2, 0.7, 0)

cv2.imshow('dst', dst)
cv2.imshow('weight', dst_with_weight)

cv2.waitKey(0)
cv2.destroyAllWindows()