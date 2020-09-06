import cv2
import numpy as np

def get_contour_areas(contours):
    """
    Parameters
    ----------
    contours: list
        List of contours

    Returns
    -------
    list
        List of areas
    """

    areas = []
    for i in contours:
        a = cv2.contourArea(i)
        areas.append(a)
    return areas

def filter_contours(contours, minArea):
    """
    Parameters
    ----------
    contours: list
        List of contours
    minArea: int
        Minimum area to filter by
    

    Returns
    -------
    list
        List of filtered contours
    """

    a = get_contour_areas(contours)
    f = []
    for i in range(len(a)):
        if a[i] > minArea:
            f.append(contours[i])

    return f

def label_contour_center(image, contours):
    """
    Parameters
    ----------
    image: Mat
        Mat representation of image

    contours: list
        List of contours

    Returns
    -------
    i: Mat
        Image with circle drawn on centers

    """

    M = cv2.moments(contours)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    cv2.circle(image, (cx, cy), 10, (0, 0, 255), -1)
    return image


img = cv2.imread('rb15.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(img, 127, 255)

contours, hierarcy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

filtered_contours = filter_contours(contours, 400)

cv2.drawContours(img, filtered_contours, -1, (0, 0, 255), 2)

"""for (i, c) in enumerate(contours):
    orig = label_contour_center(img, c)"""

cv2.imshow('Image w/ Contours', img)
cv2.imshow('Image w/ Filtered Contours', img)
cv2.imshow('centers', img)

cv2.waitKey(0)
cv2.destroyAllWindows()