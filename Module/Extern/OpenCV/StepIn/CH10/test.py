# coding: utf-8
"""
-------------------------------------------------
   File Name:      OpenCV10_Morphology
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-14 06:04 PM
-------------------------------------------------
Description :

    小票识别

"""
# https://digi.bib.uni-mannheim.de/tesseract/
# 配置环境变量如E:\Program Files (x86)\Tesseract-OCR
# tesseract -v进行测试
# tesseract XXX.png 得到结果 
# pip install pytesseract
# anaconda lib site-packges pytesseract pytesseract.py
# tesseract_cmd 修改为绝对路径即可
from PIL import Image
import pytesseract
import cv2
import os

preprocess = 'blur'  # thresh

image = cv2.imread(r'E:\Python_Code\PythonGuide\Module\Extern\OpenCV\StepIn\CH10\scan.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if preprocess == "thresh":
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[0]

if preprocess == "blur":
    gray = cv2.medianBlur(gray, 3)

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# Tesseract-OCR识别文字
text = pytesseract.image_to_string(Image.open(filename))
print(text)
os.remove(filename)

cv2.imshow("Image", image)
# cv2.imshow("Output", gray)
cv2.waitKey(0)
