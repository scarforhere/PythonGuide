# coding: utf-8
"""
-------------------------------------------------
   File Name:      angelFinder
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-15 10:51 AM
-------------------------------------------------
Description :

    Measure Angel from a picture by 3-times-clicks

"""
import cv2
import math
import imutils

path = '1.png'
img = cv2.imread(path)
img = imutils.resize(img, width=1200)
pointsList = []


def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointsList)
        if size != 0 and size % 3 != 0:
            cv2.line(img, tuple(pointsList[round((size - 1) / 3) * 3]), (x, y), (0, 0, 255), 2)
        cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)
        pointsList.append([x, y])


def gradient(pt1, pt2):
    return (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])


def getAngle(pointsList):
    pt1, pt2, pt3 = pointsList[-3:]
    try:
        m1 = gradient(pt1, pt2)
        m2 = gradient(pt1, pt3)
        angR = math.atan((m2 - m1) / (1 + (m2 * m1)))
        angD = round(math.degrees(angR))
    except ZeroDivisionError:
        angD = 90

    cv2.putText(img, str(angD), (pt1[0] - 40, pt1[1] - 20), cv2.FONT_HERSHEY_COMPLEX,
                1.5, (0, 0, 255), 2)


while True:
    if len(pointsList) % 3 == 0 and len(pointsList) != 0:
        getAngle(pointsList)

    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', mousePoints)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        pointsList = []
        img = cv2.imread(path)
        img = imutils.resize(img, width=1200)

    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()
