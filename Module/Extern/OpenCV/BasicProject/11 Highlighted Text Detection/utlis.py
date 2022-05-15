# coding: utf-8
"""
-------------------------------------------------
   File Name:      utils
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-15 10:51 AM
-------------------------------------------------
Description :

    Tools for picture operation

"""
import cv2
import numpy as np


def detectColor(img, hsv):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # cv2.imshow("hsv",imgHSV)
    lower = np.array([hsv[0], hsv[2], hsv[4]])
    upper = np.array([hsv[1], hsv[3], hsv[5]])
    mask = cv2.inRange(imgHSV, lower, upper)
    # cv2.imshow("mask", mask)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    # cv2.imshow("imgResult", imgResult)
    return imgResult


def getContours(img, imgDraw, cThr=[100, 100], showCanny=False, minArea=100, filter=0, draw=False):
    imgDraw = imgDraw.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, cThr[0], cThr[1])
    kernel = np.array((3, 3))
    imgDial = cv2.dilate(imgCanny, kernel, iterations=1)
    imgClose = cv2.morphologyEx(imgDial, cv2.MORPH_CLOSE, kernel, iterations=30)

    if showCanny:
        cv2.imshow('Canny', imgClose)

    contours, hiearchy = cv2.findContours(imgClose, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        for index in range(len(contour[:,0,1])):
            contour[index,0,1] = contour[index,0,1] - 31


    mask = np.zeros_like(imgClose)
    mask = cv2.fillPoly(mask, contours, (255, 255, 255))

    cv2.imshow("mask",mask)
    contours, hiearchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(img,contours,-1,(0,0,255),2)

    # cv2.drawContours(img, contours, -1, (0, 0, 225), 2)

    finalCountours = []
    for i in contours:
        area = cv2.contourArea(i)
        if area > minArea:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.08 * peri, True)
            bbox = cv2.boundingRect(i)
            if len(approx) == filter:
                if len(approx) >= filter:
                    finalCountours.append([len(approx), area, approx, bbox, i])
            else:
                finalCountours.append([len(approx), area, approx, bbox, i])

    finalCountours = sorted(finalCountours, key=lambda x: x[1], reverse=True)
    if draw:
        for con in finalCountours:
            x, y, w, h = con[3]
            cv2.rectangle(imgDraw, (x, y), (x + w, y + h), (255, 0, 255), 3)
            # cv2.drawContours(imgDraw,con[4],-1,(0,0,255),2)
    return imgDraw, finalCountours


def getRoi(img, contours):
    roiList = []
    for con in contours:
        x, y, w, h = con[3]
        roiList.append(img[y:y + h, x:x + w])
    return roiList


def roiDisplay(roiList):
    for x, roi in enumerate(roiList):
        roi = cv2.resize(roi, (0, 0), None, 2, 2)
        cv2.imshow(str(x),roi)


def saveText(highlightedText):
    with open('HighlightedText.csv', 'w') as f:
        for text in highlightedText:
            f.writelines(f'\n{text}')


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver