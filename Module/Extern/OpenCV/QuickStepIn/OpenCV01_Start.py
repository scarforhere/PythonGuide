# coding: utf-8
"""
-------------------------------------------------
   File Name:      OpenCV
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-14 04:16 PM
-------------------------------------------------
Description : 

    Basic Operation of OpenCV
        to deal with image or video input

"""
import cv2

# 或取当前OpenCV版本
print(cv2.getVersionString())

# 读取图片
image = cv2.imread(r"E:\Python_Code\PythonGuide\Module\Extern\OpenCV\Material\opencv_logo.jpg")

# image为numpy数据类型
print(len(image))
print(type(image))

# 包含3个维度
# image内储存(高，宽，色彩通道数目）
print(image.shape)

# 将image内存储图像以Image窗口输出
cv2.imshow("Image", image)

# 等待键盘输入(若不加窗口会一闪而过)
# 在激活窗口上输入任意键，程序结束
cv2.waitKey()
