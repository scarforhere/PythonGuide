# coding: utf-8
"""
-------------------------------------------------
   File Name:      OpenCV05_Blur
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-14 04:59 PM
-------------------------------------------------
Description : 

    Basic Operation of OpenCV
        to deal with image or video input

"""
import cv2

# 读取图片
image = cv2.imread(r"E:\Python_Code\PythonGuide\Module\Extern\OpenCV\Material\plane.jpg")

# 使用高斯滤波器处理噪点
gauss = cv2.GaussianBlur(image, (5, 5), 0)
# 使用均值滤波器处理噪点
median = cv2.medianBlur(image, 5)

cv2.imshow("image", image)
cv2.imshow("gauss", gauss)
cv2.imshow("median", median)

cv2.waitKey()
