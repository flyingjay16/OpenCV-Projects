import cv2
import numpy as np

img = cv2.imread('rb15.jpg')

"""
Affine transforms
- scaling
- rotation
- translation
- skewing
- preserve collinearity and parallelism

Non-affine transforms
- also known as projective transformation, homography
- does not preserve parallelism, length, and angle
- does preserve collinearity and incidence

Translation Matrix = |1 0 Tx|
                     |0 1 Ty|
Tx = shift along x-axis
Ty = shift along y-axis
use cv2.warpAffine to implement translations

Rotation Matrix:
M = |cos(theta) -sin(theta)|
    |sin(theta) cos(theta) |

cv2.getRotationMatrix2D(rotation_center_x, rotation_center_y, angle of rotation, scale)
"""

height, width = img.shape[:2]
quarter_height, quarter_width = height/4, width/4

T = np.float32([[1, 0, -quarter_width], [0, 1, -quarter_height]])

img_translation = cv2.warpAffine(img, T, (width, height))
cv2.imshow('Translation', img_translation)

rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
rotated_image = cv2.warpAffine(img, rotation_matrix, (width, height))

cv2.imshow('Rotation', rotated_image)

t_img = cv2.transpose(img)
cv2.imshow("Transpose", t_img)

h_flipped = cv2.flip(image, 1)
v_flipped = cv2.flip(image, -1)


cv2.waitKey(0)
cv2.destroyAllWindows()