# coding: utf-8
"""
-------------------------------------------------
   File Name:      OpenCV07_Match
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-14 05:15 PM
-------------------------------------------------
Description : 

    Basic Operation of OpenCV
        to deal with image or video input

"""
import cv2
import numpy as np

# 读取图片
image = cv2.imread(r"E:\Python_Code\PythonGuide\Module\Extern\OpenCV\Material\poker.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 或取特征模板
template = gray[75:105, 235:265]

# 使用标准相关函数匹配算法： 将模板和对象进行标准化再进行匹配
# 可保证结果不受光照强度影响
# 缺点：对图像大小敏感
match = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
# 找出匹配系数大于0.9的点
locations = np.where(match >= 0.9)

# 提取模板的宽和高
w, h = template.shape

# 必须使用*locations[::-1]进行解压，因为橡塑坐标为(y,z)，绘图坐标为(x,y)
for p in zip(*locations[::-1]):
    # 匹配出的点为左上角
    x1, y1 = p[0], p[1]
    x2, y2 = x1 + w, y1 + h
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow("image", image)
cv2.waitKey()

