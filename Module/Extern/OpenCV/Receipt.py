# coding: utf-8
"""
-------------------------------------------------
   File Name:      Receipt
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-15 10:51 AM
-------------------------------------------------
Description : 

    Print info with under format:

"""
import cv2

# 需传入电脑摄像头的序号
# 设备管理器
capture = cv2.VideoCapture('http://192.168.178.48:4747/video')

# 需要循环读取每一帧
while True:
    # 读取摄像头
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    ret1, binary_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    cv2.imshow("camera", frame)
    cv2.imshow("gray", gray)
    cv2.imshow("binary", binary)
    cv2.imshow("binary_otsu", binary_otsu)
    key = cv2.waitKey(1)
    if key != -1:
        break

capture.release()