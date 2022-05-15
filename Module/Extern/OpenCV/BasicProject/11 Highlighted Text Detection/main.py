# coding: utf-8
"""
-------------------------------------------------
   File Name:      code
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-15 10:51 AM
-------------------------------------------------
Description :

    Highlighted Text Detection

"""
from utlis import *
import pytesseract

path = 'test.png'
hsv = [18, 44, 86, 255, 255, 255]
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'

#### Step 1 ####
img = cv2.imread(path)
img = cv2.resize(img, dsize=(0, 0), fx=2, fy=2)
# cv2.imshow("Original",img)

#### Step 2 ####
imgResult = detectColor(img, hsv)

#### Step 3 & 4 ####
imgContours, contours = getContours(imgResult, img, showCanny=False, minArea=1000, filter=4, cThr=[100, 150], draw=True)
cv2.imshow("imgContours", imgContours)
print(len(contours))

#### Step 5 ####
roiList = getRoi(img, contours)
# cv2.imshow("TestCrop",roiList[2])
roiDisplay(roiList)

#### Step 6 ####
highlightedText = []
for x, roi in enumerate(roiList):
    # print(pytesseract.image_to_string(roi))
    highlightedText.append(pytesseract.image_to_string(roi))

# saveText(highlightedText)

imgStack = stackImages(0.7, ([img, imgResult, imgContours]))
cv2.imshow("Stacked Images", imgStack)

cv2.waitKey(0)
cv2.destroyAllWindows()
