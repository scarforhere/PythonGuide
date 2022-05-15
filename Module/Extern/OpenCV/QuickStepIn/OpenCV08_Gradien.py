# coding: utf-8
"""
-------------------------------------------------
   File Name:      OpenCV08_Gradien
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-14 05:48 PM
-------------------------------------------------
Description : 

    Basic Operation of OpenCV
        to deal with image or video input

"""
# 图像的匹配是梯度图进行处理，图像梯度就是明暗变化
import cv2

# 读取图片并转化为灰度图
gray = cv2.imread(r"E:\Python_Code\PythonGuide\Module\Extern\OpenCV\Material\opencv_logo.jpg", cv2.IMREAD_GRAYSCALE)

# 拉普拉斯算子，大约对应图像二阶导数
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
# canny算法，定义梯度区间提取边缘(100,200),明暗变化足够强烈
canny = cv2.Canny(gray, 100, 200)

cv2.imshow("gray", gray)
cv2.imshow("laplacian", laplacian)
cv2.imshow("canny", canny)

cv2.waitKey()
