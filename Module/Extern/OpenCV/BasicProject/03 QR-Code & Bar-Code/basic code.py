# coding: utf-8
"""
-------------------------------------------------
   File Name:      basic_code
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-15 10:51 AM
-------------------------------------------------
Description :

    Read QR-Code and Bar-Code

"""
import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread('1.jpg')
cap = cv2.VideoCapture('http://192.168.178.48:4747/video')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:

    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)
        pts2 = barcode.rect
        cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (255, 0, 255), 2)

    cv2.imshow('Result', img)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
