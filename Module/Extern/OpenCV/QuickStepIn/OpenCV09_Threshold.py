# coding: utf-8
"""
-------------------------------------------------
   File Name:      OpenCV09_Threshold
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-14 05:56 PM
-------------------------------------------------
Description : 

    Basic Operation of OpenCV
        to deal with image or video input

"""
import cv2

# 读取图片并转化为灰度图
gray = cv2.imread(r"E:\Python_Code\PythonGuide\Module\Extern\OpenCV\Material\bookpage.jpg", cv2.IMREAD_GRAYSCALE)

# 固定阈值算法：    阈值：10   最大灰度：255
ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
# 自适应阈值算法：  将图片分为多个区，每个区独立进行阈值计算    区域大小：115像素
binary_adaptive = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115,1)
# 大金算法：       不需要认为确定阈值区域和大小，自动分配使差异最大化
ret1, binary_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("gray", gray)
cv2.imshow("binary", binary)
cv2.imshow("adaptive", binary_adaptive)
cv2.imshow("otsu", binary_otsu)

cv2.waitKey()
