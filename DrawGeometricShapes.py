import numpy as np
import cv2

img = cv2.imread('watch.jpg', 1)

#parameters: image, starting coordinate, end coordinate
#parameters: rgb color, line thickness
img = cv2.line(img, (0,0), (255,255), (255, 0, 0), 10)

img = cv2.arrowedLine(img, (0,255), (255,255), (0, 0, 255), 10)

#parameters: image, top corner coordinate, bottom corner coordinate,
#paramters: rgb color, line thickness
img = cv2.rectangle(img, (255,0), (124,255), (0, 255, 0), 5)

#More examples:
# - cv2.circle
# - cv2.putText

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()