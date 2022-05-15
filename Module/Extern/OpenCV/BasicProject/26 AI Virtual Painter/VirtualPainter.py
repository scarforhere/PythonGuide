# coding: utf-8
"""
-------------------------------------------------
   File Name:      code
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-15 10:51 AM
-------------------------------------------------
Description :

    AR Painter By Hand Tracking Tools

"""
import cv2
import numpy as np
import os
import HandTrackingModule as htm

folderPath = "Header-Files"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))
header = overlayList[0]
drawColor = (255, 0, 255)

cap = cv2.VideoCapture('http://192.168.178.48:4747/video')

detector = htm.handDetector(detectionCon=0.65, maxHands=1)
xp, yp = 0, 0

success, img = cap.read()
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
imgCanvas = np.zeros_like(img)

while True:
    # 1. Import image
    success, img = cap.read()
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img = cv2.flip(img, 1)

    # 2. Find Hand Landmarks
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        # print(lmList)

        # tip of index and middle fingers
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # 3. Check which fingers are up
        fingers = detector.fingersUp()
        # print(fingers)

        # 4. If Selection Mode - Two finger are up
        if fingers[1] and y1 < 47:
            # xp, yp = 0, 0
            print("Selection Mode")
            print(x1)
            # # Checking for the click
            if x1 < 50:
                imgCanvas = np.zeros_like(img)
            elif 95 < x1 < 185:
                header = overlayList[0]
                drawColor = (255, 0, 255)
            elif 185 < x1 < 280:
                header = overlayList[1]
                drawColor = (255, 0, 0)
            elif 280 < x1 < 375:
                header = overlayList[2]
                drawColor = (0, 255, 0)
            elif 375 < x1 < 480:
                header = overlayList[3]
                drawColor = (0, 0, 0)

        # 5. If Drawing Mode - Index finger is up
        if fingers[1] and y1 > 47:
            # 6. change the brushThickness
            brushThickness = int(abs(lmList[4][1] - lmList[3][1]) + 1)
            eraserThickness = int(brushThickness * 1.5)

            if lmList[4][1] > lmList[3][1]:
                pointR = 10
            else:
                pointR = int(brushThickness / 2)
            cv2.circle(img, (x1, y1), pointR, drawColor, cv2.FILLED)

            if fingers[0]:
                print("Point Mode")
            else:
                print("Draw Mode")
                if xp == 0 and yp == 0:
                    xp, yp = x1, y1

                if drawColor == (0, 0, 0):
                    # cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                    cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
                else:
                    # cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                    cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

        xp, yp = x1, y1

        # # Clear Canvas when all fingers are up
        # if all (x >= 1 for x in fingers):
        #     imgCanvas = np.zeros((720, 1280, 3), np.uint8)

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    # Setting the header image
    header = cv2.resize(header, (480, 47))
    img[0:47, 0:480] = header
    # img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0)
    cv2.imshow("Image", img)
    # cv2.imshow("Canvas", imgCanvas)
    # cv2.imshow("Inv", imgInv)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
