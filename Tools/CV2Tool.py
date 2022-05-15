# coding: utf-8
"""
-------------------------------------------------
   File Name:      CV2Tool
   Author :        Tiancheng Song
   E-mail :        tiancheng.song@mailbox.tu-dresden.de
   Date:           2022-01-15 03:50 PM
-------------------------------------------------
Description : 

    Supporting Functions for Computer vision using OpenCV

"""
import cv2
# import mpmath
import numpy as np
import copy
import PIL
from PIL import Image
from random import randint

def resizeAntialias(_input, scale=1, widthTarget=False, heightTarget=False, squar=False):
    """
    Resize Image or images in list with antialias
    Possible Image Type: numpy.ndarray or PIL.Image.Image
    @param _input: Image or list of images
    @param scale: bigger~1+ and smaller~1-
    @return: Image or list of images
    @param widthTarget: Target width
    @param heightTarget: Target height
    """
    singleImgFlag = False
    if not isinstance(_input, list):
        imageList = [_input]
        singleImgFlag = True
    else:
        imageList = _input

    # CV2 Image Format Resize
    if isinstance(imageList[0], np.ndarray):
        for num, _ in enumerate(imageList):
            if widthTarget and not heightTarget:
                width = imageList[num].shape[1]
                height = int(widthTarget / width * imageList[num].shape[0])
            if heightTarget and not widthTarget:
                height = imageList[num].shape[0]
                width = int(heightTarget / height * imageList[num].shape[1])
            if not heightTarget and not widthTarget:
                height = int(imageList[num].shape[0] * scale)
                width = int(imageList[num].shape[1] * scale)
            else:
                height, width = heightTarget, widthTarget
            if squar:
                height, width = imageList[num].shape[:2]
                height = int(max(height, width) * scale)
                width = height
            imageList[num] = cv2.resize(imageList[num], (width, height))

    # PIL Image Format Resize
    elif isinstance(imageList[0], PIL.Image.Image):
        for num, _ in enumerate(imageList):
            width, height = imageList[num].size
            if widthTarget and not heightTarget:
                width = imageList[0].width
                scale = widthTarget / width
            if heightTarget and not widthTarget:
                height = imageList[0].height
                scale = heightTarget / height

            imageList[num] = imageList[num].resize((int(width * scale), int(height * scale)), Image.ANTIALIAS)

    if singleImgFlag:
        return imageList[0]
    else:
        return imageList


def stackImages(_imgList, cols=1, scale=1.0):
    """
    Stack Images together to display in a single window
    :param _imgList: list of images to stack
    :param cols: the num of img in a row
    :param scale: bigger~1+ and smaller~1-
    :return: Stacked Image
    """
    imgList = copy.deepcopy(_imgList)

    # make the array full by adding blank img, otherwise the openCV can't work
    totalImages = len(imgList)
    rows = totalImages // cols if totalImages // cols * cols == totalImages else totalImages // cols + 1
    blankImages = cols * rows - totalImages

    width = imgList[0].shape[1]
    height = imgList[0].shape[0]
    imgBlank = np.zeros((height, width, 3), np.uint8)
    imgList.extend([imgBlank] * blankImages)

    # resize the images
    for i in range(cols * rows):
        if scale <= 1:
            imgList[i] = cv2.resize(imgList[i], (0, 0), None, scale, scale, interpolation=cv2.INTER_AREA)
        else:
            imgList[i] = cv2.resize(imgList[i], (0, 0), None, scale, scale, interpolation=cv2.INTER_CUBIC)

        if len(imgList[i].shape) == 2:
            imgList[i] = cv2.cvtColor(imgList[i], cv2.COLOR_GRAY2BGR)

    # put the images in a board
    hor = [imgBlank] * rows
    for y in range(rows):
        line = []
        for x in range(cols):
            line.append(imgList[y * cols + x])
        hor[y] = np.hstack(line)
    ver = np.vstack(hor)
    return ver


def stackImages2(_imgList, cols=1, scale=1):
    """
    Stack Images together to display in a single window. Regardless of inhomogeneous size of images
    :param _imgList: list of images to stack
    :param cols: the num of img in a row
    :param scale: bigger~1+ and smaller~1-
    :return: Stacked Image
    """
    imgList = copy.deepcopy(_imgList)

    # make the array full by adding blank img, otherwise the openCV can't work
    totalImages = len(imgList)
    rows = totalImages // cols if totalImages // cols * cols == totalImages else totalImages // cols + 1
    blankImages = cols * rows - totalImages
    width = imgList[0].shape[1]
    height = imgList[0].shape[0]
    imgBlank = np.zeros((height, width, 3), np.uint8)
    imgList.extend([imgBlank] * blankImages)

    # resize the images
    for i in range(cols * rows):
        if scale <= 1:
            imgList[i] = cv2.resize(imgList[i], (0, 0), None, scale, scale, interpolation=cv2.INTER_AREA)
        else:
            imgList[i] = cv2.resize(imgList[i], (0, 0), None, scale, scale, interpolation=cv2.INTER_CUBIC)

        if len(imgList[i].shape) == 2:
            imgList[i] = cv2.cvtColor(imgList[i], cv2.COLOR_GRAY2BGR)

    widthList = []
    heightList = []
    for img in imgList:
        widthList.append(img.shape[1])
        heightList.append(img.shape[0])

    width = max(widthList)
    height = max(heightList)
    imgBlank = np.zeros((height * rows, width * cols, 3), np.uint8)

    # put the images in a board
    for i in range(rows):
        for j in range(cols):
            indexImg = i * cols + j
            imgHeight, imgWidth, _ = imgList[indexImg].shape
            imgHStart = i * height
            imgHEnd = i * height + imgHeight
            imgWStart = j * width
            imgWEnd = j * width + imgWidth
            imgBlank[imgHStart:imgHEnd, imgWStart:imgWEnd] = imgList[indexImg]
    return imgBlank


def cornerRect(img, bbox, l=30, t=5, rt=1,
               colorR=(255, 0, 255), colorC=(0, 255, 0)):
    """
    :param img: Image to draw on.
    :param bbox: Bounding box [x, y, w, h]
    :param l: length of the corner line
    :param t: thickness of the corner line
    :param rt: thickness of the rectangle
    :param colorR: Color of the Rectangle
    :param colorC: Color of the Corners
    :return:
    """
    x, y, w, h = bbox
    x1, y1 = x + w, y + h
    if rt != 0:
        cv2.rectangle(img, bbox, colorR, rt)
    # Top Left  x,y
    cv2.line(img, (x, y), (x + l, y), colorC, t)
    cv2.line(img, (x, y), (x, y + l), colorC, t)
    # Top Right  x1,y
    cv2.line(img, (x1, y), (x1 - l, y), colorC, t)
    cv2.line(img, (x1, y), (x1, y + l), colorC, t)
    # Bottom Left  x,y1
    cv2.line(img, (x, y1), (x + l, y1), colorC, t)
    cv2.line(img, (x, y1), (x, y1 - l), colorC, t)
    # Bottom Right  x1,y1
    cv2.line(img, (x1, y1), (x1 - l, y1), colorC, t)
    cv2.line(img, (x1, y1), (x1, y1 - l), colorC, t)

    return img


def findContours(img, imgPre, sort=True, areaInt=(-1, -1), aspect=(-1, -1), polyFilter=None,
                 merge=False, mergeRatio=0.5, drawCon=False, drawRect=False, drawCenter=False, c=(0, 0, 255)):
    """
    Finds Contours in an image
    :param img: Image on which we want to draw
    :param imgPre: Image on which we want to find contours
    :param areaInt: Area interval to detect as valid contour. Set value to -1 to ship judge
    :param aspect; Ratio interval of width/height
    :param sort: True will sort the contours by area (biggest first)
    :param polyFilter: Filters based on the corner points e.g. 4 = Rectangle or square. Set value to -1 to ship judge
    :param merge: Merge adjacent contours
    :param mergeRatio: Merge interval
    :param drawCon: draw contours boolean
    :param drawRect: draw rectangles boolean
    :param drawCenter: draw center point boolean
    :param c: Contour color
    :return: Foudn contours with [contours, Area, BoundingBox, Center]
    """
    conFound = []
    imgContours = img.copy()
    contours, hierarchy = cv2.findContours(imgPre, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if (areaInt[0] == -1 or areaInt[0] <= area) and \
                (areaInt[1] == -1 or area <= areaInt[1]):
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            if (aspect[0] == -1 or aspect[0] <= w / h) and \
                    (aspect[1] == -1 or w / h <= aspect[1]):
                # print(len(approx))
                if len(approx) == polyFilter or polyFilter is None:
                    cx, cy = x + (w // 2), y + (h // 2)
                    conFound.append({"cnt": cnt, "area": area, "bbox": [x, y, w, h], "center": [cx, cy]})
                    if not merge:
                        if drawCon: cv2.drawContours(imgContours, cnt, -1, c, 3)
                        if drawRect: cv2.rectangle(imgContours, (x, y), (x + w, y + h), c, 2)
                        if drawCenter: cv2.circle(imgContours, (x + (w // 2), y + (h // 2)), 3, c, cv2.FILLED)

    if merge:
        conFound = sorted(conFound, key=lambda x: x["bbox"][0])
        mergeList = []
        i = 0
        while i < len(conFound):
            mergeList.append(conFound[i])
            for j in range(i + 1, len(conFound)):
                mergeList.append(conFound[j])

                x1, x2 = mergeList[0]["bbox"][0], mergeList[1]["bbox"][0]
                w1, w2 = mergeList[0]["bbox"][2], mergeList[1]["bbox"][2]
                h1, h2 = mergeList[0]["bbox"][3], mergeList[1]["bbox"][3]
                cy1, cy2 = mergeList[0]["center"][1], mergeList[1]["center"][1]

                if abs(x1 - x2) <= (w1 + w2) / 2 * (1 + mergeRatio) and abs(cy1 - cy2) <= (h1 + h2) / 2:
                    area = mergeList[0]["area"] + mergeList[1]["area"]
                    if (areaInt[0] != -1 and areaInt[0] >= area) and \
                            (areaInt[1] != -1 and area >= areaInt[1]):
                        del conFound[i]
                        del conFound[j]
                        mergeList = []
                        i -= 1
                        break
                    cnt = np.concatenate((mergeList[0]["cnt"], mergeList[1]["cnt"]), axis=0)
                    x = x1
                    y = min(mergeList[0]["bbox"][1], mergeList[1]["bbox"][1])
                    w = max(x2 + w2, x1 + w1) - x1
                    h = max(mergeList[0]["bbox"][1] + mergeList[0]["bbox"][3],
                            mergeList[1]["bbox"][1] + mergeList[1]["bbox"][3]) - \
                        min(mergeList[0]["bbox"][1], mergeList[1]["bbox"][1])
                    cx, cy = x + (w // 2), y + (h // 2)
                    conFound[i] = {"cnt": cnt, "area": area, "bbox": [x, y, w, h], "center": [cx, cy]}

                    del conFound[j]
                    mergeList = []
                    i -= 1
                    break

                else:
                    del mergeList[1]

            mergeList = []
            i += 1

        for contour in conFound:
            cnt = contour["cnt"]
            x, y, w, h = contour["bbox"]
            if drawCon: cv2.drawContours(imgContours, cnt, -1, c, 3)
            if drawRect: cv2.rectangle(imgContours, (x, y), (x + w, y + h), c, 2)
            if drawCenter: cv2.circle(imgContours, (x + (w // 2), y + (h // 2)), 3, c, cv2.FILLED)

    if sort:
        conFound = sorted(conFound, key=lambda x: x["area"], reverse=True)

    return imgContours, conFound


def overlayPNG(imgBack, imgFront, pos=[0, 0]):
    hf, wf, cf = imgFront.shape
    hb, wb, cb = imgBack.shape
    *_, mask = cv2.split(imgFront)
    maskBGRA = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)
    maskBGR = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    imgRGBA = cv2.bitwise_and(imgFront, maskBGRA)
    imgRGB = cv2.cvtColor(imgRGBA, cv2.COLOR_BGRA2BGR)

    imgMaskFull = np.zeros((hb, wb, cb), np.uint8)
    imgMaskFull[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = imgRGB
    imgMaskFull2 = np.ones((hb, wb, cb), np.uint8) * 255
    maskBGRInv = cv2.bitwise_not(maskBGR)
    imgMaskFull2[pos[1]:hf + pos[1], pos[0]:wf + pos[0], :] = maskBGRInv

    imgBack = cv2.bitwise_and(imgBack, imgMaskFull2)
    imgBack = cv2.bitwise_or(imgBack, imgMaskFull)

    return imgBack


def rotateImage(img, angle, scale=1):
    h, w = img.shape[:2]
    center = (w / 2, h / 2)
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=angle, scale=scale)
    img = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(w, h))
    return img


def putTextRect(img, text, pos, scale=3, thickness=3, colorT=(255, 255, 255),
                colorR=(255, 0, 255), font=cv2.FONT_HERSHEY_PLAIN,
                offset=10, border=None, colorB=(0, 255, 0)):
    """
    Creates Text with Rectangle Background
    :param img: Image to put text rect on
    :param text: Text inside the rect
    :param pos: Starting position of the rect x1,y1
    :param scale: Scale of the text
    :param thickness: Thickness of the text
    :param colorT: Color of the Text
    :param colorR: Color of the Rectangle
    :param font: Font used. Must be cv2.FONT....
    :param offset: Clearance around the text
    :param border: Outline around the rect
    :param colorB: Color of the outline
    :return: image, rect (x1,y1,x2,y2)
    """
    ox, oy = pos
    (w, h), _ = cv2.getTextSize(text, font, scale, thickness)

    x1, y1, x2, y2 = ox - offset, oy + offset, ox + w + offset, oy - h - offset

    cv2.rectangle(img, (x1, y1), (x2, y2), colorR, cv2.FILLED)
    if border is not None:
        cv2.rectangle(img, (x1, y1), (x2, y2), colorB, border)
    cv2.putText(img, text, (ox, oy), font, scale, colorT, thickness)

    return img, [x1, y2, x2, y1]


def main():
    # path = r"D:\15152\Desktop\Lieber\New folder\20210718_114835.jpg"
    # img = cv2.imread(path)
    # imgStake1 = stackImages3([img, img], cols=2)
    # imgStake = stackImages3([img, imgStake1], cols=1, scale=0.1)
    # cv2.imshow("Img", imgStake)
    # cv2.waitKey(0)
    pass


if __name__ == "__main__":
    main()

print("********************************************************")
print("***                   By Song T.C.                   ***")
print("***       tiancheng.song@mailbox.tu-dresden.de       ***")
print("********************************************************")
