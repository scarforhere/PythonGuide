# coding: utf-8
"""
-------------------------------------------------
   File Name:      SkyGuitarSheet
   Author :        Tiancheng Song
   E-mail :        tiancheng.song@mailbox.tu-dresden.de
   Date:           2022-02-10 04:05 PM
-------------------------------------------------
Description : 

    Class SkyGuitarExtract: Extract guitar score from Sky Guitar into A4 format as PDF file
    Class SkyGuitarExtract: Pick up color range of image

"""
import os
import cv2
import numpy as np
import pafy
from PIL import ImageFont, ImageDraw, Image, ImageOps, ImageEnhance
from CV2Tool import stackImages, resizeAntialias, findContours
from GetAllFiles import get_all_files
from TimeRecord import TimeMonitor
from Module.Extern.PyTorch.MNIST_Convolution.HandWritingNumber import model_optimizer_init, predict_from_extern
import pytesseract as ocr

colorType = "Click To Select Point"
color = ""

model_path = r"E:\Python_Code\PythonGuide\Module\Extern\PyTorch\MNIST_Convolution\Data"
model, _ = model_optimizer_init(model_path)


class TrackBar(object):
    def __init__(self, colorRange, trackBarName="TrackBar"):
        self.colorRange = colorRange
        self.trackBarName = trackBarName

        self.__trackbar_initiate(self.colorRange)

    @staticmethod
    def __empty(empty):
        """
        Empty Function for Trackbar
        (Privat Function)

        @param empty: None
        @return: None
        """
        pass

    def __trackbar_initiate(self, colorRange):
        """
        Initiate Trackbar for color range
        (Privat Function)

        @param colorRange: colorRange = [[Hmin, Smin, Vmin], [Hmax, Smax, Vmax], P]
        """
        ((Hmin, Smin, Vmin), (Hmax, Smax, Vmax)), P = colorRange

        cv2.namedWindow(self.trackBarName)
        cv2.resizeWindow(self.trackBarName, 600, 400)
        cv2.createTrackbar("P", self.trackBarName, P, 255, self.__empty)
        cv2.createTrackbar("H min", self.trackBarName, Hmin, 180, self.__empty)
        cv2.createTrackbar("H max", self.trackBarName, Hmax, 180, self.__empty)
        cv2.createTrackbar("S min", self.trackBarName, Smin, 255, self.__empty)
        cv2.createTrackbar("S max", self.trackBarName, Smax, 255, self.__empty)
        cv2.createTrackbar("V min", self.trackBarName, Vmin, 255, self.__empty)
        cv2.createTrackbar("V max", self.trackBarName, Vmax, 255, self.__empty)

    def get_range_value(self):
        """
        Get list of value range

        @return: [[[Hmin, Smin, Vmin], [Hmax, Smax, Vmax]], P]
        """
        P = cv2.getTrackbarPos("P", self.trackBarName)
        Hmin = cv2.getTrackbarPos("H min", self.trackBarName)
        Hmax = cv2.getTrackbarPos("H max", self.trackBarName)
        Smin = cv2.getTrackbarPos("S min", self.trackBarName)
        Smax = cv2.getTrackbarPos("S max", self.trackBarName)
        Vmin = cv2.getTrackbarPos("V min", self.trackBarName)
        Vmax = cv2.getTrackbarPos("V max", self.trackBarName)

        return [[[Hmin, Smin, Vmin], [Hmax, Smax, Vmax]], P]


class ColorValue(object):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, _path, colorRange, scale=1.0):
        self.path = _path
        self.scale = scale
        self.colorRange = colorRange

        self.path = self.__get_path()
        self.img = None
        self.__color_pick_up()

    def __get_path(self):
        """
        Get first PNG file path in folder

        @return: Path of first PNG file
        """
        return get_all_files(self.path, "png")[0]

    @staticmethod
    def __mouseColor(event, x, y, flags, param):
        """
        Callback function of cv2.setMouseCallback

        @param event: Event of action of mouse
        @param x: X position of mouse
        @param y: Y position of mouse
        @param flags: Combination of mouse event
        @param param: Parameter list from cv2.setMouseCallback
        """
        img, height, width = param
        if event == cv2.EVENT_LBUTTONDOWN:
            global colorType, color
            color = img[y, x]

            if y <= height / 3:
                if x <= width / 2:
                    colorType = "Gray"
                    print(colorType, color)
                else:
                    colorType = "HSV"
                    print(colorType, color)
            else:
                colorType = "Click To Select Point"
                color = ''

    def __color_pick_up(self):
        """
        Generate interface to pick up correct color range of Gray and HSV
        """
        tb = TrackBar(self.colorRange)

        while True:
            imgOrig = cv2.imread(self.path)
            frameHeight = int(imgOrig.shape[0] * 0.4675)
            imgOrig = imgOrig[:frameHeight, :, :]
            imgOrig = resizeAntialias(imgOrig, self.scale)

            self.colorRange = tb.get_range_value()

            imgStack = self.__get_img_mask(imgOrig)
            height, width, _ = imgStack.shape

            cv2.namedWindow("Color Picker")
            cv2.setMouseCallback("Color Picker", self.__mouseColor, param=[imgStack, height, width])
            cv2.putText(imgStack, ''.join([colorType, "  ", str(color)]), (10, 30),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            cv2.imshow("Color Picker", imgStack)

            key = cv2.waitKey(1) & 0xFF
            if key == 27:
                print(f"colorRange = {colorRange}")
                break

        cv2.destroyAllWindows()

    @staticmethod
    def __img_mask_GRAY(img, colorRange):
        """
        Generate mask from GRAY range
        (Privat Function)

        @param img: Image to be masked
        @param colorRange: Value range of GRAY
        @return: imgStack
        """
        P = colorRange
        _, mask = cv2.threshold(img, P, 255, cv2.THRESH_BINARY_INV)
        return mask

    @staticmethod
    def __img_mask_HSV(img, colorRange):
        """
        Generate mask from HSV range
        (Privat Function)

        @param img: Image to be masked
        @param colorRange: Value range of HSV
        @return: imgStack
        """
        lower = np.array(colorRange[0])
        upper = np.array(colorRange[1])
        imgMaskRange = cv2.inRange(img, lower, upper)
        return imgMaskRange

    def __get_img_mask(self, img):
        """
        Get masked images from all color spaces、

        @param img: cv2 Image
        @return: imgStack
        """
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        imgMaskedGray = self.__img_mask_GRAY(imgGray, self.colorRange[1])
        imgMaskedHSV = self.__img_mask_HSV(imgHSV, self.colorRange[0])

        imgMasked = cv2.bitwise_not(cv2.bitwise_or(imgMaskedGray, imgMaskedHSV))

        imgStack = stackImages([imgGray, imgHSV], cols=2, scale=0.5)
        imgStack = stackImages([imgStack, imgMasked], cols=1)
        return imgStack


mouseCounter = 0
posList = [[0, 0], [0, 0]]


class AreaPick(object):
    def __init__(self, folderPath, mode):
        self.folderPath = folderPath
        self.area_pick(mode=mode)

    @staticmethod
    def mouse_percent(event, x, y, flags, param):
        """
        Callback function of cv2.setMouseCallback

        @param event: Event of action of mouse
        @param x: X position of mouse
        @param y: Y position of mouse
        @param flags: Combination of mouse event
        @param param: Parameter list from cv2.setMouseCallback
        """
        global mouseCounter, posList
        height, width, _ = param
        if event == cv2.EVENT_LBUTTONDOWN:
            if mouseCounter == 0:
                posList.append([x, y])
                del posList[:2]
                mouseCounter = 1
                print(f"X = {x}  Y = {y}")
            else:
                posList.append([x, y])
                mouseCounter = 0
                print(f"X = {x}  Y = {y}")

    def area_pick(self, mode):
        """
        Get percentage value of trimHeightP and areaP

        :param mode: "compare" -> leftP, upP, rightP, bottomP ; "trimHeight" -> trimHeightP
        :return: Area info
        """
        global posList
        areaStr = None
        path = get_all_files(self.folderPath, "png")[0]
        imgOrig = cv2.imread(path)
        while True:
            imgResize = resizeAntialias(imgOrig, 0.5)
            if len(posList) == 2:
                if mode == "compare":
                    cv2.rectangle(imgResize, posList[0], posList[1], (0, 0, 255), 1)
                    leftP, upP, rightP, bottomP = posList[0][0] / imgResize.shape[1], \
                                                  posList[0][1] / imgResize.shape[0], \
                                                  posList[1][0] / imgResize.shape[1], \
                                                  posList[1][1] / imgResize.shape[0],
                    areaStr = f"area = [{leftP}, {upP}, {rightP}, {bottomP}]"
                if mode == "trimHeight":
                    trimHeight = max(posList[0][1], posList[1][1])
                    cv2.line(imgResize, (0, trimHeight), (imgResize.shape[1], trimHeight), (0, 0, 255), 3)
                    trimHeightP = trimHeight / imgResize.shape[0]
                    areaStr = f"trimHeightP = {trimHeightP}"

            cv2.imshow("Image", imgResize)
            cv2.setMouseCallback("Image", self.mouse_percent, param=imgResize.shape)
            k = cv2.waitKey(1)
            if k == 27 & 0xFF:
                print(areaStr)
                break

        cv2.destroyAllWindows()


class MyCallback:
    def __init__(self, callbackId):
        self.callbackId = callbackId

    def __call__(self, total, recvd, ratio, rate, eta):
        print("\r\tDownloading {:s}: {:>7.3f} MB ".format(self.callbackId, recvd / (1024 * 1024)), end='')
        print("{:>6.1f} % {:>10.1f} kBps    ETA: {:>5.1f} s".format(ratio * 100, rate, eta), end='')


class GuitarTuneCatch(object):
    def __init__(self, folderPath, url, colorRange, videoType="mp4"):
        self.videoType = videoType
        self.folderPath = folderPath
        self.url = url
        self.colorRange = colorRange
        self.imgtest = 0

    def start(self, trimHeighP, areaP, compMode="auto"):
        """
        Start function of GuitarScoreCatch
        """
        if not self.check_image(self.folderPath):
            if not self.check_video(self.folderPath, self.videoType):
                self.download(self.folderPath, self.url, self.videoType)

            self.image_extract(self.folderPath, self.videoType, trimHeighP, areaP, compMode)

        extractor = SkyGuitarScoreExtract(self.folderPath, self.colorRange)
        extractor.start()

    @staticmethod
    def check_video(folderPath, videoType):
        """
        Check if video is already extracted

        @return: True -> Already extracted ; False -> Not extracted
        """
        videoList = get_all_files(folderPath, fileType=videoType)
        if len(videoList) != 0:
            return True
        else:
            return False

    @staticmethod
    def check_image(folderPath, fileType="png"):
        """
        Check if images are already extracted

        @return: True -> Already extracted ; False -> Not extracted
        """
        videoList = get_all_files(folderPath, fileType=fileType)
        if len(videoList) != 0:
            return True
        else:
            return False

    @staticmethod
    def download(folderPath, url, videoType):
        """
        Download video from ulr, which is by url targeted
        """
        print("\nProceeding: Download Video")
        t_download = TimeMonitor("\tTime for Downlaod", 40)

        video = pafy.new(url)
        bestVideo = video.getbestvideo(preftype=videoType)

        resolution = bestVideo.resolution
        extension = bestVideo.extension

        videoName = os.path.split(folderPath)[-1]
        path = "".join([folderPath, "\\", videoName, ".", extension])

        print(f"\tDownload Path: {folderPath}")
        print(f"\tVideo Type: {extension}")
        print(f"\tResolution: {resolution}")

        bestVideo.download(path, quiet=True, callback=MyCallback(videoName))

        t_download.show()
        print("\nDownload Done!!!")

    def image_extract(self, folderPath, videoType, trimHeighP, areaP, compMode="auto"):
        """
        Extract images from video and save in target path
        """
        print("\nProceeding: Extract Key Frame")
        t_extract = TimeMonitor("\n\tTime for Extract", 40)

        videoPath = get_all_files(folderPath, fileType=videoType)[0]
        cap = cv2.VideoCapture(videoPath)

        frameCounts = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        heightTrim = int(height * trimHeighP)
        frameFPS = cap.get(cv2.CAP_PROP_FPS)
        speedRate = 5  # Interval(s) per frame

        print(f"\tTotal Frame: {frameCounts}")
        print(f"\tFrame Width: {width}")
        print(f"\tFrame Height: {height}")
        print(f"\tVideo FPS: {frameFPS:.5}")
        print(f"\tSpeed Accelerate Rate: {speedRate}")

        sampleCount = int(frameCounts // (speedRate * frameFPS))

        imgList = []
        startFlagList = []
        startFrame = 0
        iStartFrame = 0
        maskAVG = 0
        noneZero = 0
        captureFlag = False
        textScale = 0.6
        imgNum = 1
        for i in range(sampleCount):
            sampleFrame = i * speedRate * frameFPS
            cap.set(cv2.CAP_PROP_POS_FRAMES, sampleFrame)
            _, imgOrig = cap.read()
            imgList.append(imgOrig)

            startFlag, imgGray = self.check_start_frame(imgOrig, thres=100)
            startFlagList.append(startFlag)

            # if i > 101:
            #     del imgList[0]
            #     del startFlagList[0]
            #     startFrame = True
            # if True and i > 101:

            if not i < 2:
                del imgList[0]
                del startFlagList[0]

                if not startFlagList[0] and startFlagList[1]:
                    startFrame = sampleFrame
                    iStartFrame = i

            # (i - iStartFrame) > 2 for hands blur
            if startFrame != 0 and (i - iStartFrame) > 1:
                if compMode == "manuel":
                    captureFlag, imgMask, maskAVG, noneZero = self.comparator_bitwise_manuel(imgList,
                                                                                             [heightTrim, width], areaP)
                if compMode == "autoXOR":
                    captureFlag, imgMask, maskAVG, noneZero = self.comparator_bitwise_auto_XOR(imgList,
                                                                                               [heightTrim, width])
                if compMode == "tesseract" or compMode == "nn_MNIST":
                    captureFlag, imgMask, maskAVG, noneZero = self.comparator_bitwise_auto_nn(imgList,
                                                                                              [heightTrim, width],
                                                                                              compMode)
                imgOrig = stackImages([imgOrig, imgMask], cols=1)

                cv2.rectangle(imgOrig, (0, 0), (width, heightTrim), (0, 0, 255), 3)
                cv2.rectangle(imgOrig, (0, 0),
                              (int(width * 0.13 * textScale), int(heightTrim * 0.07 * textScale)),
                              (0, 0, 255), -1)
                cv2.putText(imgOrig, "Capturing",
                            (int(width * 0.006 * textScale), int(heightTrim * 0.047 * textScale)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5 * textScale, (255, 255, 255), 2)

            if captureFlag:
                imgPath = "".join([folderPath, "\\", str(imgNum).zfill(3), ".png"])
                imgNum += 1
                cv2.imwrite(imgPath, imgList[0])

            # if startFrame != 0:
            #     masktest = imgList[0]
            #     self.imgtest += 1
            #     path = ''.join([self.folderPath, "\\", str(self.imgtest).zfill(4), ".png"])
            #     cv2.imwrite(path, masktest)

            print(f"\r\tWorking on Frame: {int(sampleFrame)}  {(i / sampleCount * 100):3.2f} %", end='')
            print(f"  startFrame: {int(startFrame)}  maskAVG = {int(maskAVG)}", end='')
            print(f"  nonZero = {noneZero}  captureFlag: {captureFlag}", end='')

            imgOrig = resizeAntialias(imgOrig, 0.5)
            cv2.imshow("img", imgOrig)

            cv2.waitKey(1)

        cv2.destroyAllWindows()
        t_extract.show()
        print("\nExtract Done!!!")

    @staticmethod
    def check_start_frame(img, thres=100):
        """
        Ship demo part. Get

        @param img:
        @param thres:
        @return:
        """
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        grayAvg = np.mean(img)
        # print(f"  grayAVG: {grayAvg}", end='')
        if grayAvg > thres:
            return True, img
        else:
            return False, img

    def comparator_bitwise_manuel(self, imgList, imgSize, area):
        """
        Compare specific area of images to judge, whether new score is shown

        :param imgList: [img_former, img_now]
        :param imgSize: [img_width, img_height]
        :param area: Position of detected area in percentage[left, up, right, bottom]
        :return: Ture -> new score ; False -> old score
        """
        trimHeight, width = imgSize
        leftP, upP, rightP, bottomP = area

        mask1, _ = SkyGuitarScoreExtract.img_mask(imgList[0][:trimHeight, :, :], self.colorRange)
        mask2, _ = SkyGuitarScoreExtract.img_mask(imgList[1][:trimHeight, :, :], self.colorRange)

        masks = stackImages([mask1, mask2], cols=1)

        left = int(leftP * width)
        up = int(upP * imgList[0].shape[0])
        right = int(rightP * width)
        bottom = int(bottomP * imgList[0].shape[0])

        cv2.rectangle(masks, (left, up), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(masks, (left, up + trimHeight),
                      (right, bottom + trimHeight), (0, 0, 255), 2)

        sectionMask1 = mask1[up:bottom, left:right]
        sectionMask2 = mask2[up:bottom, left:right]
        maskXOR = cv2.bitwise_xor(sectionMask1, sectionMask2)

        noneZero = np.count_nonzero(maskXOR)
        maskAVG = np.mean(maskXOR)

        imgSection = stackImages([sectionMask1, sectionMask2], cols=2, scale=0.5)
        widthmin = min(maskXOR.shape[1], imgSection.shape[1])
        maskXOR = stackImages([imgSection[:, :widthmin], maskXOR[:, :widthmin]], cols=1)

        maskXOR = resizeAntialias(maskXOR, 10)
        cv2.imshow("maskXOR", maskXOR)

        if noneZero > 20:
            captureFlag = True
        else:
            captureFlag = False

        return captureFlag, masks, maskAVG, noneZero

    def comparator_bitwise_auto_XOR(self, imgList, imgSize, display=False):
        """
        Compare specific area of images to judge, whether new score is shown

        :param imgList: [img_former, img_now]
        :param imgSize: [img_width, img_height]
        :return: Ture -> new score ; False -> old score
        """
        mask1, sectionMask1, (x1, y1, w1, h1) = self.comparator_numerArea_picker(imgList[0], imgSize, display=display)
        mask2, sectionMask2, (x2, y2, w2, h2) = self.comparator_numerArea_picker(imgList[1], imgSize, display=display)

        masks = stackImages([mask1, mask2], cols=1)

        cv2.rectangle(masks, (x1, y1),
                      (x1 + w1, y1 + h1), (0, 0, 255), 2)
        cv2.rectangle(masks, (x2, y2 + imgSize[0]),
                      (x2 + w2, y2 + h2 + imgSize[0]), (0, 0, 255), 2)

        heightmax = min(sectionMask1.shape[0], sectionMask2.shape[0])
        widthmax = min(sectionMask1.shape[1], sectionMask2.shape[1])
        sectionMask1 = resizeAntialias(sectionMask1, widthTarget=widthmax, heightTarget=heightmax)
        sectionMask2 = resizeAntialias(sectionMask2, widthTarget=widthmax, heightTarget=heightmax)

        maskXOR = cv2.bitwise_xor(sectionMask1, sectionMask2)
        noneZero = np.count_nonzero(maskXOR)
        maskAVG = np.mean(maskXOR)

        imgSection = stackImages([sectionMask1, sectionMask2], cols=2, scale=0.5)
        widthmin = min(maskXOR.shape[1], imgSection.shape[1])
        maskXOR = stackImages([imgSection[:, :widthmin], maskXOR[:, :widthmin]], cols=1)

        maskXOR = resizeAntialias(maskXOR, 10)
        cv2.imshow("maskXOR", maskXOR)

        if noneZero > 160 and maskAVG > 32:
            captureFlag = True
        else:
            captureFlag = False

        if display:
            print(f"captureFlag={captureFlag}\tmaskAVG={maskAVG:4.3f}\tnoneZero={noneZero}")
            cv2.imshow("masks", resizeAntialias(masks, 0.5))
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # # Get all masked number section area
        # if captureFlag is True:
        #     self.imgtest += 1
        #     path = ''.join([self.folderPath, "\\", str(self.imgtest).zfill(4), ".jpg"])
        #     cv2.imwrite(path, cv2.resize(sectionMask1, (28, 28)))

        return captureFlag, masks, maskAVG, noneZero

    def comparator_bitwise_auto_nn(self, imgList, imgSize, mode="teeseract", display=False):
        """
        Compare specific area of images to judge, whether new score is shown

        :param imgList: [img_former, img_now]
        :param imgSize: [img_width, img_height]
        :return: Ture -> new score ; False -> old score
        """
        mask1, sectionMask1, (x1, y1, w1, h1) = self.comparator_numerArea_picker(imgList[0], imgSize, display=display)
        mask2, sectionMask2, (x2, y2, w2, h2) = self.comparator_numerArea_picker(imgList[1], imgSize, display=display)

        masks = stackImages([mask1, mask2], cols=1)

        cv2.rectangle(masks, (x1, y1),
                      (x1 + w1, y1 + h1), (0, 0, 255), 2)
        cv2.rectangle(masks, (x2, y2 + imgSize[0]),
                      (x2 + w2, y2 + h2 + imgSize[0]), (0, 0, 255), 2)

        heightmax = min(sectionMask1.shape[0], sectionMask2.shape[0])
        widthmax = min(sectionMask1.shape[1], sectionMask2.shape[1])
        sectionMask1 = resizeAntialias(sectionMask1, widthTarget=widthmax, heightTarget=heightmax)
        sectionMask2 = resizeAntialias(sectionMask2, widthTarget=widthmax, heightTarget=heightmax)

        sectionMask1 = cv2.cvtColor(sectionMask1, cv2.COLOR_BGR2GRAY)
        sectionMask2 = cv2.cvtColor(sectionMask2, cv2.COLOR_BGR2GRAY)

        res_lst1, res_lst2 = [], []
        if mode == "BF":
            pass
        else:
            img_list1 = self.char_segm(sectionMask1)
            img_list2 = self.char_segm(sectionMask2)
            if mode == "tesseract":
                custom_config = r'--oem 3 --psm 6 outputbase digits'
                for img in img_list1:
                    res = ocr.image_to_string(img, config=custom_config)
                    res_lst1.append(res)
                for img in img_list2:
                    res = ocr.image_to_string(img, config=custom_config)
                    res_lst2.append(res)
            elif mode == "nn_MNIST":
                res_lst1 = self.nn_MNIST(img_list1)
                res_lst2 = self.nn_MNIST(img_list2)

        imgSection = stackImages([sectionMask1, sectionMask2], cols=2, scale=10)
        cv2.imshow("imgSection", imgSection)

        if res_lst1 != res_lst2:
            captureFlag = True
            # self.imgtest += 1
            # path = ''.join([self.folderPath, "\\", str(self.imgtest).zfill(3), ".jpg"])
            # cv2.imwrite(path, sectionMask1)
        else:
            captureFlag = False

        maskAVG, noneZero = 0, 0

        if display:
            print(f"captureFlag={captureFlag}\tmaskAVG={maskAVG:4.3f}\tnoneZero={noneZero}")
            cv2.imshow("masks", resizeAntialias(masks, 0.5))
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        return captureFlag, masks, maskAVG, noneZero

    def comparator_numerArea_picker(self, img, imgSize, display=False):
        """
        Get section number bbox and img

        :param imgSize: [height, width]
        :return: imgNum, [x, y, w, h]
        """
        height, width = imgSize

        mask, _ = SkyGuitarScoreExtract.img_mask(img[:height, :width], self.colorRange)

        kernel = np.ones((3, 3), np.uint8)
        imgDilate = cv2.dilate(mask[:int(height * 0.3), :int(width * 0.3)], kernel)

        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        imgCon, conInfo = findContours(mask, imgDilate, areaInt=[0, 500], aspect=[0.2, 5], merge=True, mergeRatio=0.5,
                                       sort=False, drawCenter=True, drawRect=True, c=(0, 0, 255))
        conInfo = sorted(conInfo, key=lambda x: x["center"][0])
        # for info in conInfo:
        #     print(info["area"])

        # In case of none contour detected
        try:
            x, y, w, h = conInfo[0]['bbox']
            imgNum = mask[y - 2:y + h + 2, x - 2:x + w + 2]
        except IndexError:
            x, y, w, h = 0, 0, 1, 1
            imgNum = np.zeros_like(mask)[:30, :30]

        if display:
            img = resizeAntialias(imgNum, 10)
            cv2.imshow("img", img)
            cv2.imshow("mask", imgDilate)
            cv2.imshow("imgContour", imgCon)
            # cv2.waitKey(0)

        return mask, imgNum, [x, y, w, h]

    @staticmethod
    def char_segm(imgCV2):
        imgCopy = imgCV2

        _, imgThres = cv2.threshold(imgCV2, 5, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        _, conInfos = findContours(imgCopy, imgThres, drawCenter=True, drawRect=True)
        conInfos = sorted(conInfos, key=lambda x: x["bbox"][0])

        bbox_lst = []
        for idx, conInfo in enumerate(conInfos):
            x, y, w, h = conInfo["bbox"]
            if w / h > 1:
                x1, y1, w1, h1 = x, y, int(w / 2), h
                x2, y2, w2, h2 = x + int(w / 2), y, w - int(w / 2), h
                bbox_lst.append([x1, y1, w1, h1])
                bbox_lst.append([x2, y2, w2, h2])
            else:
                bbox_lst.append([x, y, w, h])

        imgNum_lst = []
        for idx, (x, y, w, h) in enumerate(bbox_lst):
            img = imgCopy[y:y + h, x:x + w]
            # img = cv2.resize(img, (22, 22))
            margin = 3
            img = resizeAntialias(img, squar=True)
            img_len = img.shape[0]
            imgCanvas = np.zeros((img_len + 2 * margin, img_len + 2 * margin), dtype=np.uint8)
            imgCanvas[margin - 1:margin - 1 + img_len, margin - 1:margin - 1 + img_len] = img
            imgCanvas = Image.fromarray(cv2.cvtColor(imgCanvas, cv2.COLOR_GRAY2RGB))
            imgNum_lst.append(imgCanvas)

        return imgNum_lst

    @staticmethod
    def nn_MNIST(imgNum_lst):
        res_lst = []
        if len(imgNum_lst) != 0:
            for img in imgNum_lst:
                pred, pred_probab = predict_from_extern(img, model, test=True)
                # print(pred, pred_probab)
                res_lst.append(pred)
        return res_lst

    @staticmethod
    def BF(img1, img2):
        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)

        bf = cv2.BFMatcher(cv2.NORM_HAMMING)

        matches = bf.knnMatch(des1, trainDescriptors=des2, k=2)

        good = [m for (m, n) in matches if m.distance < 0.75 * n.distance]
        similary = len(good) / len(matches)

        if similary > 0.5:
            return [True], [True]
        else:
            return [True], [False]


class SkyGuitarScoreExtract(object):
    def __init__(self, folderPath=None, colorRange=None):
        self.folderPath = folderPath
        self.P = colorRange[1]
        self.HSVLower = np.array(colorRange[0][0])
        self.HSVUpper = np.array(colorRange[0][1])

    def start(self, resolution=500, title=None, titleSizeP=0.5, titleMarginUpP=0.035, titleMarginDownP=0.01,
              marginUpP=0.04, marginDownP=0.03, pageNoSizeP=0.15):
        """
        Start function of SkyGuitarExtract
        """
        t_total = TimeMonitor("Total Used Time", 40)
        if title is None:
            title = os.path.split(self.folderPath)[-1]
        print(f"\nExtracting Guitar Score From Sky Guitar: {title}")
        print(f"\tFolder path: {self.folderPath}")

        imgListCV2 = self.img_extract(self.folderPath, False)
        imgListPIL = self.convert_cv2_PIL(imgListCV2)
        pageList = self.format_a4(imgListPIL, resolution=resolution, title=title, titleSizeP=titleSizeP,
                                  titleMarginUpP=titleMarginUpP, titleMarginDownP=titleMarginDownP,
                                  marginUpP=marginUpP, marginDownP=marginDownP,
                                  pageNumber=True, pageNoSizeP=pageNoSizeP)
        self.export_pdf(pageList, self.folderPath, resolution=resolution)

        print("\nExtract Down\n")
        t_total.show()

    @classmethod
    def img_extract(cls, path, display=True):
        """
        Extract sheet sections of screen snap from Sky Guitar Guide on Youtube

        @param path: Folder path of images
        @param display: True -> Display each image
        @return: List of images in cv2 format
        """
        print("\nProceeding: Image trim and filter")
        t_extract = TimeMonitor("\tTime for Trim and filter", 40)

        imgListCV2 = []
        imgPathList = get_all_files(path, "png")
        for num, imgPath in enumerate(imgPathList):
            imgOrig = cv2.imread(imgPath)

            frameHeight = int(imgOrig.shape[0] * 0.4675)

            imgTrim = imgOrig[:frameHeight, :, :]

            imgDown, key = cls.img_mask(imgTrim, colorRange, num, display=display, timeFlag=True)
            imgListCV2.append(imgDown)

            if display and key == 27:
                break

        t_extract.show()
        return imgListCV2

    @staticmethod
    def img_mask(img, colorRange, num=0, display=False, timeFlag=False):
        """
        Remove background of image.
        Pick up all sheet sections.
        Return operated image

        @param img: Image to be operated
        @param colorRange: Range of color
        @param num: No. of Image
        @param display: True -> Display each image
        @param timeFlag: True -> Display time cost
        @return: imgStack -> Operated Image, key -> ESC: Quit operation; Enter: Continue
        """
        if timeFlag:
            t_mask = TimeMonitor(f"\tSection No.{num + 1}    Mask down", 40)

        P = colorRange[1]
        HSVLower = np.array(colorRange[0][0])
        HSVUpper = np.array(colorRange[0][1])

        # Make mask from Gray Color Model
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, imgMaskGray = cv2.threshold(imgGray, P, 255, cv2.THRESH_BINARY_INV)

        # Make mask from HSV Color Model
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        imgMaskRange = cv2.inRange(imgHSV, HSVLower, HSVUpper)
        imgMaskHSV = imgMaskRange
        # (thres1, imgThres1) = cv2.threshold(imgHSV[:, :, 1], 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        # (thres2, imgThres2) = cv2.threshold(imgHSV[:, :, 2], 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        # imgMaskThres = cv2.bitwise_or(imgThres1, imgThres2)
        # imgMaskHSV = cv2.bitwise_or(imgMaskRange, imgMaskThres)

        # Merge masks from Gray and HSVColor Model
        imgMask = cv2.bitwise_or(imgMaskGray, imgMaskHSV)

        if display:
            imgMask = cv2.bitwise_not(imgMask)
            imgResize = resizeAntialias(imgMask, 1)
            cv2.imshow("".join(["Image: ", str(num + 1)]), imgResize)
            key = cv2.waitKey(0) & 0xFF
        else:
            key = 10

        if timeFlag:
            t_mask.show()
        return imgMask, key

    @classmethod
    def format_a4(cls, imgList, resolution, title, titleSizeP, titleMarginUpP, titleMarginDownP,
                  marginUpP, marginDownP, pageNoSizeP, pageNumber=True):
        """
        Generate score in ISO A4 format from sheet section

        :param imgList: List of images in type PIL
        :param resolution: Resolution of target PDF file
        :param title: Score Title
        :param titleSizeP: Title size (resolution * titleSizeP)
        :param titleMarginUpP: Up margin of title (height * titleMarginUpP)
        :param titleMarginDownP: Down margin of title (height * titleMarginDownP)
        :param marginUpP: Up margin of pages except first page (height * marginUpP)
        :param marginDownP: Down margin of pages except first page (height * marginDownP)
        :param pageNoSizeP: Title size (resolution * pageNoSizeP)
        :param pageNumber: True -> enable page number ;  False -> disable page number
        :return: List of A4 paper in type PIL
        """
        print("\nProceeding: Reformat score in ISO A4")
        t_reformat = TimeMonitor("\tTime for Reformat", 40)

        pageList = []

        widthA4 = 8.25
        heightA4 = 11.75

        width = int(widthA4 * resolution)
        height = int(heightA4 * resolution)

        fontPath = r'C:\Windows\Fonts\arial.ttf'
        titleSize = int(resolution * titleSizeP)
        titleMarginUp = int(height * titleMarginUpP)
        titleMarginDown = int(height * titleMarginDownP)
        marginUp = int(height * marginUpP)
        marginDown = int(height * marginDownP)
        pageNo = 1
        pageNoSize = int(resolution * pageNoSizeP)
        pageNoMarginDown = height - marginDown

        imgBK_PIL = Image.new('RGB', (width, height), (0, 0, 0))

        heightSection = resizeAntialias(imgList[0], widthTarget=imgBK_PIL.width).height

        flagSectionRemain = True

        while flagSectionRemain:
            t_convert = TimeMonitor(f"\tPage No. {pageNo}    Convert Down", 40)
            imgPIL = imgBK_PIL.copy()

            # Title
            if len(pageList) == 0:
                font = ImageFont.truetype(fontPath, titleSize)
                draw = ImageDraw.Draw(imgPIL)
                titleOffsetX, titleOffsetY = font.getoffset(title)
                titleWidth, titleHeight = font.getsize(title)
                titleX, titley = (int(width / 2 - (titleWidth / 2 + titleOffsetX)), titleMarginUp)
                draw.text((titleX, titley), title, font=font)
                yStart = titley + titleOffsetY + titleHeight + titleMarginDown + 1
            else:
                yStart = marginUp + 1

            # Page Number
            if pageNumber:
                pageStr = ''.join(["- ", str(pageNo), " -"])
                font = ImageFont.truetype(fontPath, pageNoSize)
                draw = ImageDraw.Draw(imgPIL)
                pageNoOffsetX, _ = font.getoffset(pageStr)
                pageNoWidth, _ = font.getsize(pageStr)
                pageNoX, pageNoy = (int(width / 2 - (pageNoWidth / 2 + pageNoOffsetX)), pageNoMarginDown)
                draw.text((pageNoX, pageNoy), pageStr, font=font)
                pageNo += 1

            # Section
            yRemain = height - yStart - marginDown
            numBlock = yRemain // heightSection
            heightBlock = int(yRemain / numBlock)
            for _ in range(numBlock):
                imgSection = imgList[0]
                imgSection = resizeAntialias(imgSection, widthTarget=imgPIL.width)
                imgSection = cls.img_enhance(imgSection)
                box = (0, yStart, imgPIL.width, yStart + heightSection)
                imgPIL.paste(imgSection, box)
                yStart = yStart + heightBlock + 1

                # Check for if images remained
                del imgList[0]
                if len(imgList) == 0:
                    flagSectionRemain = False
                    break

            imgPIL = ImageEnhance.Sharpness(imgPIL)
            imgPIL = imgPIL.enhance(5)
            imgPIL = ImageOps.invert(imgPIL)
            imgPIL = imgPIL.convert("1")
            pageList.append(imgPIL.convert(mode="L"))  # Set mode="L" to reduce file size

            t_convert.show()

        t_reformat.show()
        return pageList

    @staticmethod
    def img_enhance(imgPIL):
        """
        Smooth and sharp the original image

        @param imgPIL:Images in type PIL
        @return: Images in type PIL
        """
        imgCV2 = cv2.cvtColor(np.asarray(imgPIL), cv2.COLOR_RGB2GRAY)

        _, imgCV2 = cv2.threshold(imgCV2, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # Remove noising point and cavity inside blocks
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        imgCV2 = cv2.morphologyEx(imgCV2, cv2.MORPH_CLOSE, kernel)

        # Blur
        imgCV2 = cv2.bilateralFilter(imgCV2, 9, 1, 100)
        # imgCV2 = cv2.medianBlur(imgCV2, 1)

        imgPIL = Image.fromarray(cv2.cvtColor(imgCV2, cv2.COLOR_BGR2RGB))

        return imgPIL

    @staticmethod
    def convert_cv2_PIL(imgList):
        """
        Convert images in list from cv2(BGR) into PIL.Image(RGB)

        @param imgList: List of images in cv2 format
        @return: List of images in PIL format
        """
        print("\nProceeding: Convert images from CV2 into PIL")
        t_convert = TimeMonitor("\tTime for Convert", 40)

        for num, _ in enumerate(imgList):
            imgList[num] = Image.fromarray(cv2.cvtColor(imgList[num], cv2.COLOR_BGR2RGB))

        t_convert.show()
        return imgList

    @staticmethod
    def export_pdf(PIL_List, path, resolution=600.0):
        """
        Export images in list as PDF file

        @param path: Target path of PDF file
        @param PIL_List: List of images in PIL format
        @param resolution: Resolution of target PDF
        """
        print("\nProceeding: Export score as PDF file")
        t_export = TimeMonitor("\tTime for Export", 40)

        namePDF = os.path.split(path)[-1]
        pathPDF = "".join([path, "\\", namePDF, ".pdf"])

        PIL_List[0].save(pathPDF, "PDF", resolution=resolution, save_all=True, append_images=PIL_List[1:])
        t_export.show()



def debug_comparator_auto():
    path = r"E:\Guitar Score\Number_Test"
    imgList = []
    pathList = get_all_files(path, "jpg")
    start = 1
    end = len(pathList)
    imgList.append(cv2.imread(pathList[start - 1]))
    imgSize = [int(imgList[0].shape[0] * 0.4666666666666667), imgList[0].shape[1]]
    for i in range(start - 1, end - 1):
        imgList.append(cv2.imread(pathList[i]))
        cv2.imshow("img1", imgList[0])
        cv2.imshow("img2", imgList[1])
        res = debug_BF(imgList[0], imgList[1], thres=0.55)
        del imgList[0]
        print(res)
        cv2.waitKey(0)


def debug_comparator_autoNN():
    path = r"E:\Guitar Score\Number_Test"
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    pathList = get_all_files(path, "jpg")
    for i in range(len(pathList)):
        res_lst = []

        print(f"idx: {i}  {res_lst}")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    # imgCV2_path = pathList[7]
    # imgCV2 = cv2.imread(imgCV2_path)
    # imgNum_lst = character_segm(imgCV2)
    # nn_OCR(imgNum_lst)
    cv2.waitKey(0)

def debug_BF(img1, img2, thres=0.4):
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    good = [m for (m, n) in matches if m.distance < 0.75 * n.distance]
    similary = len(good) / len(matches)

    if similary > thres:
        return [True], [True]
    else:
        return [True], [False]


if __name__ == '__main__':
    # targetFolderPath = os.getcwd()
    targetFolderPath = r"E:\Guitar Score\Asturias_Auto"
    url = r"https://www.youtube.com/watch?v=ZhbSDAuCXPQ"

    colorRange = [[[0, 0, 0], [180, 255, 205]], 185]
    # colorRange = [[[0, 0, 0], [180, 255, 180]], 133]
    # ColorValue(targetFolderPath, colorRange)

    # TODO: First: Run GuitarTuneCatch.start to catch one image from Video
    # TODO: Second: Run AreaPick in mode="compare" and "trimHeight" to get trimHeightP and area
    # TODO: Third: Delete the image, which is generated in first step
    # TODO: Forth: Run GuitarTuneCatch.start to catch score of Video
    # AreaPick(targetFolderPath, mode="compare")
    trimHeightP = 0.4666666666666667
    area = [0.0375, 0.09259259259259259, 0.058333333333333334, 0.11481481481481481]  # Austrias
    # area = [0.03958333333333333, 0.06666666666666667, 0.05625, 0.09074074074074075]

    catcher = GuitarTuneCatch(targetFolderPath, url, colorRange)
    catcher.start(trimHeightP, area, compMode="nn_MNIST")

    # debug_comparator_auto()
    # debug_comparator_autoNN()

    print("********************************************************")
    print("***                   By Song T.C.                   ***")
    print("***       tiancheng.song@mailbox.tu-dresden.de       ***")
    print("********************************************************")
