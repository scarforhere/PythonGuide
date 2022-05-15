# coding: utf-8
"""
-------------------------------------------------
   File Name:      code
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-15 10:51 AM
-------------------------------------------------
Description :

    AR Virtual Mouse By Hand Tracking Tools

"""
import cv2
import numpy as np
import HandTrackingModule as htm
import pyautogui as pygui
import time

##########################
frameR = 100  # Frame Reduction
smoothening = 1
#########################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture('http://192.168.178.48:4747/video')
success, img = cap.read()
wCam, hCam,  _ = img.shape
detector = htm.handDetector(maxHands=1)
# wScr, hScr = autopy.screen.size()
wScr, hScr = pygui.size()
# print(wScr, hScr)

while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # print(img.shape)

    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        # print(x1, y1, x2, y2)

    # 3. Check which fingers are up
    fingers = detector.fingersUp()
    # print(fingers)
    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)
    # 4. Middle Finger : Moving Mode
    if fingers[2] == 1:

        # 5. Convert Coordinates
        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

        # 6. Smoothen Values
        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening

        # 7. Move Mouse
        pygui.moveTo(wScr - clocX, clocY)
        cv2.circle(img, (x1, y1), 10, (0, 255, 0), cv2.FILLED)
        plocX, plocY = clocX, clocY

        # 8. Both Index fingers are up and distance between Index and middle Finger > 40 : Clicking Mode
        # 9. Find distance between fingers
        length, _ , _ = detector.findDistance(8, 12, img, False)

        # 10. Click mouse if distancwe short
        if length > 50:
            cv2.circle(img, (x1, y1),15, (0, 0, 255), cv2.FILLED)
            pygui.click()

    # img = cv2.resize(img, (0, 0), fx=3, fy=3)
    img = cv2.flip(img, 1)

    # 11. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    # 12. Display
    cv2.imshow("Image", img)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

