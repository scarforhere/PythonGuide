# coding: utf-8
"""
-------------------------------------------------
   File Name:      code
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-15 10:51 AM
-------------------------------------------------
Description :

    Stitch Pictures into single Picture

"""
import cv2
import os

mainFolder = 'Images'
myFolders = os.listdir(mainFolder)
print(myFolders)

for folder in myFolders:
    path = mainFolder + '/' + folder
    images = []
    myList = os.listdir(path)
    print(f'Total No. of images detected {len(myList)}')
    for imgN in myList:
        curImg = cv2.imread(f'{path}/{imgN}')
        curImg = cv2.resize(curImg, (0, 0), None, 0.2, 0.2)
        images.append(curImg)

    stitcher = cv2.Stitcher.create()
    (status, result) = stitcher.stitch(images)
    if (status == cv2.STITCHER_OK):
        print('Panorama Generated')
        cv2.imshow(folder, result)
        cv2.waitKey(1)
    else:
        print('Panorama Generation Unsuccessful')

cv2.waitKey(0)
cv2.destroyAllWindows()
