import numpy as np
import cv2

"""img = cv2.imread('watch.jpg', 1)

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

cv2.imshow('image', img)"""

image = np.zeros((512, 512, 3), np.uint8)
image_bw = np.zeros((512, 512), np.uint8)

pts = np.array([[10, 50], [400, 50], [90, 200], [50, 500]], np.int32)
print(pts, pts.shape)
pts = pts.reshape((-1, 1, 2))
print(pts)
cv2.polylines(image, [pts], True, (0, 0, 255), 3)

cv2.circle(image, (256, 256), 50, (255, 0, 0), -1)

cv2.putText(image, 'Hello World', (75, 290), cv2.FONT_HERSHEY_COMPLEX, 2, (100, 170, 3), 3)


cv2.imshow("Black rectangle (Color)", image)

cv2.imshow("Black rectangle (B&W)", image_bw)


cv2.waitKey(0)
cv2.destroyAllWindows()