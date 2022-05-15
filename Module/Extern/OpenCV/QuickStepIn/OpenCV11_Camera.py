# coding: utf-8
"""
-------------------------------------------------
   File Name:      OpenCV11_Camera
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-14 06:11 PM
-------------------------------------------------
Description : 

    Basic Operation of OpenCV
        to deal with image or video input

"""
import cv2

# 需传入电脑摄像头的序号
# 设备管理器
capture = cv2.VideoCapture('http://192.168.178.48:4747/video')

# 需要循环读取每一帧
while True:
    # 读取摄像头
    ret, frame = capture.read()
    cv2.imshow("camera", frame)
    key = cv2.waitKey(1)
    if key != -1:
        break

capture.release()
