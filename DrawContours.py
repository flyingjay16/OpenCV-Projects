import cv2 

"""img = cv2.imread('rb15.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", img)
cv2.imshow("Gray Image", imgray)


cv2.CHAIN_APPROX_NONE - Stores all points along the line (inefficient)
cv2.RETR_EXTERNAL - retrieves external/outer contours only
cv2.RETR_COMP  - retrieves all in a 2 - level hierarchy
cv2.RETR_TREE - retrieves all in full hierarchy

hierarchy: [next, previous, first child, and parent]



ret,thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#3rd parameter tells drawContours() which contour to show
#-1 shows all contours
img = cv2.drawContours(img, contours, -1, (255, 0, 0), 2)

cv2.imshow("Image with contours", img)

cv2.waitKey(0)
cv2.destroyAllWindows()"""

img = cv2.imread('rb15.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edge = cv2.Canny(img, 127, 255)

contours, hierarchy = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

cv2.imshow('Image w/ Contours', img)

cv2.waitKey(0)
cv2.destroyAllWindows()