# coding: utf-8
"""
-------------------------------------------------
   File Name:      OpenCV10_Morphology
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-14 06:04 PM
-------------------------------------------------
Description : 

    Basic Operation of OpenCV
        to deal with image or video input

"""
import cv2
import numpy as np

# 读取图片并转化为灰度图
gray = cv2.imread(r"E:\Python_Code\PythonGuide\Module\Extern\OpenCV\Material\opencv_logo.jpg", cv2.IMREAD_GRAYSCALE)

# 固定阈值反向算法  原因：背景白色  目标：背景黑色，图案白色
_, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
# 定义操作核
kernel = np.ones((5, 5), np.uint8)

# 形态学腐蚀算法
erosion = cv2.erode(binary, kernel)
# 形态学膨胀算法
dilation = cv2.dilate(binary, kernel)

cv2.imshow("binary", binary)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)

cv2.waitKey()
