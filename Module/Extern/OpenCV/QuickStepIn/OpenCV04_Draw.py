# coding: utf-8
"""
-------------------------------------------------
   File Name:      OpenCV04_Draw
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-14 04:50 PM
-------------------------------------------------
Description : 

    Basic Operation of OpenCV
        to deal with image or video input

"""
import cv2
import numpy as np

# 创建黑色画布需使用numpy3维无符号数组
image = np.zeros([300, 300, 3], dtype=np.uint8)

# 绘制线段 line(画布名称，起点坐标，终点坐标，颜色，粗细)
cv2.line(image, (100, 200), (250, 250), (255, 0, 0), 2)
# 绘制矩形 rectangle(画布名称，顶点坐标，对角坐标，颜色，粗细)
cv2.rectangle(image, (30, 100), (60, 150), (0, 255, 0), 2)
# 绘制圆形 circle(画布名称，圆心坐标，半径，颜色，粗细)
cv2.circle(image, (150, 100), 20, (0, 0, 255), 3)
# 绘制文字 putText(画布名称，目标字符串，坐标，字体(0为默认字体)，缩放系数，颜色，粗细，线条类型)
cv2.putText(image, "hello", (100, 50), 0, 1, (255, 255, 255), 2, 1)

cv2.imshow("image", image)
cv2.waitKey()

"""
图像绘制缺点：
    1. 转角细节不够清楚
    2. putTest函数无法绘制任意字体
"""
