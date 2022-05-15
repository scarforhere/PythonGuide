# coding: utf-8
"""
-------------------------------------------------
   File Name:      OpenCV03_Trim
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-14 04:45 PM
-------------------------------------------------
Description : 

    Basic Operation of OpenCV
        to deal with image or video input

"""
import cv2

# 读取图片
image = cv2.imread(r"E:\Python_Code\PythonGuide\Module\Extern\OpenCV\Material\opencv_logo.jpg")

# 按像素提取部分图片(全色彩通道)
# image[目标行数，目标列数，目标色彩通道]
# 目标选择顺序：左上到右下
trim = image[10:170, 40:200]

cv2.imshow("Trim", trim)
cv2.waitKey()
