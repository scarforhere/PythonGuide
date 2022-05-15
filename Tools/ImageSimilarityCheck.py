# coding: utf-8
"""
-------------------------------------------------
   File Name:      ImageSimilarityCheck
   Author :        Tiancheng Song
   E-mail :        tiancheng.song@mailbox.tu-dresden.de
   Date:           2022-02-19 11:26 AM
-------------------------------------------------
Description : 

    Print info with under format:

"""
import os
import cv2
import json
from functools import reduce
from PIL import Image
from GetAllFiles import get_all_files
from TimeRecord import TimeMonitor


class SimilarityMatcher(object):
    def __init__(self, threshold1=0.7, threshold2=0.8):
        # 融合相似度阈值
        self.threshold1 = threshold1
        # 最终相似度较高判断阈值
        self.threshold2 = threshold2

    def calc_image_similarity(self, img1_path, img2_path):
        """
        融合函数计算图片相似度

        :param img1_path: filepath+filename
        :param img2_path: filepath+filename
        :return: 图片最终相似度
        """
        similary_ORB = float(self.ORB_img_similarity(img1_path, img2_path))
        similary_phash = float(self.phash_img_similarity(img1_path, img2_path))
        similary_hist = float(self.calc_similar_by_path(img1_path, img2_path))
        # 如果三种算法的相似度最大的那个大于0.7，则相似度取最大，否则，取最小。
        max_three_similarity = max(similary_ORB, similary_phash, similary_hist)
        min_three_similarity = min(similary_ORB, similary_phash, similary_hist)
        if max_three_similarity > self.threshold1:
            result = max_three_similarity
        else:
            result = min_three_similarity

        return round(result, 3)

    @staticmethod
    def ORB_img_similarity(img1_path, img2_path):
        """
        计算两个图片相似度函数ORB算法

        :param img1_path: 图片1路径
        :param img2_path: 图片2路径
        :return: 图片相似度
        """
        try:
            # 读取图片
            img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
            img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

            # 初始化ORB检测器
            orb = cv2.ORB_create()
            kp1, des1 = orb.detectAndCompute(img1, None)
            kp2, des2 = orb.detectAndCompute(img2, None)

            # 提取并计算特征点
            bf = cv2.BFMatcher(cv2.NORM_HAMMING)
            # knn筛选结果
            matches = bf.knnMatch(des1, trainDescriptors=des2, k=2)

            # 查看最大匹配点数目
            good = [m for (m, n) in matches if m.distance < 0.75 * n.distance]
            similary = len(good) / len(matches)
            return similary

        except:
            return '0'

    @staticmethod
    def phash(img):
        """
        计算图片的局部哈希值--pHash

        :param img: 图片
        :return: 返回图片的局部hash值
        """
        img = img.resize((8, 8), Image.ANTIALIAS).convert('L')
        avg = reduce(lambda x, y: x + y, img.getdata()) / 64.
        hash_value = reduce(lambda x, y: x | (y[1] << y[0]),
                            enumerate(map(lambda i: 0 if i < avg else 1, img.getdata())),
                            0)
        return hash_value

    @classmethod
    def phash_img_similarity(cls, img1_path, img2_path):
        """
        计算两个图片相似度函数局部敏感哈希算法

        :param img1_path: 图片1路径
        :param img2_path: 图片2路径
        :return: 图片相似度
        """
        # 读取图片
        img1 = Image.open(img1_path)
        img2 = Image.open(img2_path)

        # 计算汉明距离
        distance = bin(cls.phash(img1) ^ cls.phash(img2)).count('1')
        similary = 1 - distance / max(len(bin(cls.phash(img1))), len(bin(cls.phash(img1))))
        return similary

    # 直方图计算图片相似度算法
    @staticmethod
    def make_regalur_image(img, size=(256, 256)):
        """
        我们有必要把所有的图片都统一到特别的规格，在这里我选择是的256x256的分辨率。
        """
        return img.resize(size).convert('RGB')

    @staticmethod
    def hist_similar(lh, rh):
        assert len(lh) == len(rh)
        return sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lh, rh)) / len(lh)

    @classmethod
    def calc_similar(cls, li, ri):
        return sum(cls.hist_similar(l.histogram(), r.histogram()) for l, r in zip(cls.split_image(li),
                                                                                  cls.split_image(ri))) / 16.0

    @classmethod
    def calc_similar_by_path(cls, lf, rf):
        li, ri = cls.make_regalur_image(Image.open(lf)), cls.make_regalur_image(Image.open(rf))
        return cls.calc_similar(li, ri)

    @staticmethod
    def split_image(img, part_size=(64, 64)):
        w, h = img.size
        pw, ph = part_size
        assert w % pw == h % ph == 0
        return [img.crop((i, j, i + pw, j + ph)).copy() for i in range(0, w, pw) for j in range(0, h, ph)]

    def similar_search(self, folderPath):
        """
        Find similar Images in target folderPath.
        Export analysis info as folderPath\similarInfo.txt

        @param folderPath: Target folderPath
        @return: similarDict[pathOrig] = [[pathComp1, similarRate1], [pathComp2, similarRate2], ...]
        """
        print("\nProceeding: Matching Image")
        t_total = TimeMonitor("\nMatch Down:", 30)

        pathList = get_all_files(folderPath, "jpg")

        imgCount = len(pathList)
        step = 0
        stepTotal = 0
        for i in range(imgCount):
            stepTotal += i

        similarDict = {}
        similarList = []
        for numOrig, pathOrig in enumerate(pathList):
            if pathOrig in similarList:
                step += len(pathList[(numOrig + 1):])
                continue

            for numComp, pathComp in enumerate(pathList[(numOrig + 1):]):
                similarRate = self.phash_img_similarity(pathOrig, pathComp)

                step += 1
                print(f"\r\tCompare {os.path.split(pathList[numOrig])[1]}", end='')
                print(f"\t\twith {os.path.split(pathList[numComp + numOrig + 1])[1]}", end='')
                print(f"\t\tsimilarRate = {similarRate * 100:.4}%", end='')
                print(f"\t\t{numOrig + 1}/{imgCount - 1}({(step / stepTotal) * 100:5.2f}%)", end='')

                if similarRate >= self.threshold2:
                    if pathOrig not in similarDict.keys():
                        similarDict[pathOrig] = []

                    similarDict[pathOrig].append([pathComp, similarRate])
                    similarList.append(pathComp)

        if len(similarDict) != 0:
            print("\n\n\tSimilarity Info:")
            keys = similarDict.keys()
            for key in keys:
                print(f"\t\tOrigin File: {key}")
                print(f"\t\t\t{len(similarDict[key])} Similar Image(s):")
                for pathComp in similarDict[key]:
                    print(f"\t\t\t\tsimilarRate: {pathComp[1] * 100:5.2f}%\t\tFile: {pathComp[0]}")
        else:
            print("\n\n\tNone Similar Image Detected!!!")

        similarName = ''.join([folderPath, "\\similarInfo.txt"])
        with open(similarName, 'w') as f:
            f.write(json.dumps(similarDict))

        t_total.show()

        return similarDict


if __name__ == '__main__':
    # 搜索文件夹
    folderPath = r'D:\15152\Desktop\Lieber\Nordrhein-Westfalen'
    similarSearcher = SimilarityMatcher(0.7, 0.8)
    similarSearcher.similar_search(folderPath)

    print("********************************************************")
    print("***                   By Song T.C.                   ***")
    print("***       tiancheng.song@mailbox.tu-dresden.de       ***")
    print("********************************************************")
