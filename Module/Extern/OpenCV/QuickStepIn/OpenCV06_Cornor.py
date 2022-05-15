# coding: utf-8
"""
-------------------------------------------------
   File Name:      OpenCV06_Feature
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-14 05:03 PM
-------------------------------------------------
Description : 

    Basic Operation of OpenCV
        to deal with image or video input

"""
import cv2

# 读取图片
image = cv2.imread(r"E:\Python_Code\PythonGuide\Module\Extern\OpenCV\Material\opencv_logo.jpg")

# 将图片转化成灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 或取图像中的拐角特征点
# goodFeaturesToTrack(图像变量，最多返回点数量，点质量，特征点间距离大于)
corners1 = cv2.goodFeaturesToTrack(gray, 500, 0.1, 10)
corners2 = cv2.goodFeaturesToTrack(gray, 500, 0.1, 1)


for corner in corners1:
    x, y = corner.ravel()
    # 返回x,y为浮点数，坐标数值类型为整数
    cv2.circle(image, (int(x), int(y)), 3, (255, 0, 255), -1)

cv2.imshow("corners1", image)

for corner in corners2:
    x, y = corner.ravel()
    # 返回x,y为浮点数，坐标数值类型为整数
    cv2.circle(image, (int(x), int(y)), 3, (255, 0, 255), -1)

cv2.imshow("corners2", image)

cv2.waitKey()
