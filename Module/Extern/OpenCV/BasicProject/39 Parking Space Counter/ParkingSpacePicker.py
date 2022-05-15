# coding: utf-8
"""
-------------------------------------------------
   File Name:      ParkingSpacePicker
   Author :        Tiancheng Song
   E-mail :        tiancheng.song@mailbox.tu-dresden.de
   Date:           2022-01-14 11:45 PM
-------------------------------------------------
Description : 

    Park Lot Picker

"""
import cv2
import pickle

img = cv2.imread("carParkImg.png")

width, height = 107, 48

try:
    with open("CarParkPos", "rb") as f:
        posList = pickle.load(f)
except:
    posList = []


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))

    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open("CarParkPos", "wb") as f:
        pickle.dump(posList, f)


while True:

    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()

print("********************************************************")
print("***                   By Song T.C.                   ***")
print("***       tiancheng.song@mailbox.tu-dresden.de       ***")
print("********************************************************")
