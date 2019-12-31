import cv2 

img = cv2.imread('rb15.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", img)
cv2.imshow("Gray Image", imgray)


ret,thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#3rd parameter tells drawContours() which contour to show
#-1 shows all contours
img = cv2.drawContours(img, contours, -1, (255, 0, 0), 2)

cv2.imshow("Image with contours", img)

cv2.waitKey(0)
cv2.destroyAllWindows()