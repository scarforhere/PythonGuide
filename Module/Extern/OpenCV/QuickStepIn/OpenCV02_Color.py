# coding: utf-8
"""
-------------------------------------------------
   File Name:      OpenCV02_Color
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-14 04:38 PM
-------------------------------------------------
Description : 

    Basic Operation of OpenCV
        to deal with image or video input

"""
import cv2

# 读取图片
image = cv2.imread(r"E:\Python_Code\PythonGuide\Module\Extern\OpenCV\Material\opencv_logo.jpg")

# OpenCV的色彩通道存储顺序为B(image(:,:,0)), G(image(:,:,1)), R(image(:,:,2))，存储阈值为[0,255]
# 显示各色彩通道灰度图像
cv2.imshow("blue", image[:, :, 0])
cv2.imshow("green", image[:, :, 1])
cv2.imshow("red", image[:, :, 2])
cv2.waitKey()

# 将3个色彩通道的灰度平方和加权平均
# 可描述图像明暗分布
# 如从CMOS芯片读取数据，可表示为芯片接收光子数分布图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
cv2.waitKey()
