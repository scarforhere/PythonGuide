# coding: utf-8
"""
-------------------------------------------------
   File Name:      main
   Author :        Tiancheng Song
   E-mail :        tiancheng.song@mailbox.tu-dresden.de
   Date:           2022-01-15 12:10 AM
-------------------------------------------------
Description : 

    Parking Counter

"""
import cv2
import pickle
import cvzone
import numpy as np

# Video Feed
cap = cv2.VideoCapture("carPark.mp4")

width, height = 107, 48

with open("CarParkPos", "rb") as f:
    posList = pickle.load(f)


def checkParkingSpace(imgPro):
    spaceCounter = 0

    for pos in posList:
        x, y = pos

        imgCrop = imgPro[y:y + height, x:x + width]
        # cv2.imshow(str(x*y),imgCrop)

        count = cv2.countNonZero(imgCrop)
        cvzone.putTextRect(img, str(count), (x, y + height), scale=1.3, thickness=1, offset=0, colorR=(0, 0, 255))

        if count < 1100:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)

    cvzone.putTextRect(img, f"Free: {spaceCounter}/{len(posList)}", (100, 50), scale=5, thickness=5, offset=20, colorR=(0, 200, 0))


while True:
    _, img = cap.read()

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgThreshold, kernel, iterations=1)

    checkParkingSpace(imgDilate)

    cv2.imshow("Image", img)
    # cv2.imshow("ImgGray", imgGray)
    # cv2.imshow("ImgBlur", imgBlur)
    # cv2.imshow("ImgThres", imgThreshold)
    # cv2.imshow("ImgMedians", imgMedian)
    # cv2.imshow("ImgDilate", imgDilate)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

print("********************************************************")
print("***                   By Song T.C.                   ***")
print("***       tiancheng.song@mailbox.tu-dresden.de       ***")
print("********************************************************")
