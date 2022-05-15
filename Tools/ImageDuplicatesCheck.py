# coding: utf-8
"""
-------------------------------------------------
   File Name:      ImageDuplicatesCheck
   Author :        Tiancheng Song
   E-mail :        tiancheng.song@mailbox.tu-dresden.de
   Date:           2022-02-18 02:23 PM
-------------------------------------------------
Description : 

    Detect Duplicated Images And Delete

"""
import os
import cv2
import json
import hashlib as hash
from TimeRecord import TimeMonitor
from GetAllFiles import get_all_files
from CV2Tool import stackImages


# Generate hash info for files in target folderPath
class HashInfoGenerator(object):
    def __init__(self, folderPath):
        self.hash_all(folderPath)

    def hash_all(self, folderPath):
        """
        Calculate hash value for each image in target folderPath.
        Export analysis info as folderPath\duplicationInfo.txt

        @param folderPath: Target folderPath
        """
        print("\nProceeding: Generating Hash Info")
        time_hash = TimeMonitor("Generate Hash Info Down", 40)

        pathList = get_all_files(folderPath)

        hashList = []
        for num, path in enumerate(pathList):
            hashInfo = self.hash_type_choose(path)

            print(f"\r\tWorking on {os.path.split(path)[1]}", end='')
            print(f"\t\thashResult = {hashInfo}", end='')
            print(f"\t\t{num + 1}/{len(pathList)}", end='')
            print(f"({(num + 1) / len(pathList) * 100:5.2f}%)", end='')

            hashList.append([path, hashInfo])

        hashList = self.hash_info_sort(hashList)

        hashName = ''.join([folderPath, "\\duplicationInfo.txt"])
        with open(hashName, 'w') as f:
            f.write(json.dumps(hashList))
        print(f"\n\tHash info stored in foler: {hashName}")

        time_hash.show()

    def hash_type_choose(self, path):
        fileType = os.path.splitext(path)[1]
        if fileType in [".jpg", ".png", ".jpeg"]:
            return self.hash_image(path)
        else:
            return self.hash_others(path)

    @staticmethod
    def hash_image(path):
        img = cv2.imread(path)
        img = cv2.resize(img, (8, 8))
        imgInfo = str(img.tolist())
        hashInfo = hash.sha1(imgInfo.encode("utf-8")).hexdigest()
        return hashInfo

    @staticmethod
    def hash_others(path):
        try:
            with open(path, 'r') as f:
                data = f.read()
            hashInfo = hash.sha1(data.encode("utf-8")).hexdigest()
            return hashInfo
        except UnicodeDecodeError:
            print(f"\r\tError: Load {path} failed")

    @staticmethod
    def hash_info_sort(hashList):
        hashList = sorted(hashList, key=lambda x: x[1])
        return hashList


def find_duplication(folderPath):
    """
    Find all duplicated files by hashInfo.txt

    @param folderPath: Folder, in where hashInfo.txt is stored
    @return: Dictionary of fuplicated files
    """
    print("\nProceeding: Comparing Hash Info")
    time_comp = TimeMonitor("Compare Down", 40)

    path = get_all_files(folderPath, "txt")[0]
    with open(path, 'r') as f:
        data = f.read()
        dataList = json.loads(data)
        pathList = [path for (path, _) in dataList]
        hashList = [hash for (_, hash) in dataList]

    imgCount = len(pathList)
    step = 0
    stepTotal = 0
    for i in range(imgCount):
        stepTotal += i

    DuplDict = {}
    DuplCompListAll = []
    for numOrig, hashInfoOrig in enumerate(hashList):
        if pathList[numOrig] in DuplCompListAll:
            step += len(pathList[(numOrig + 1):])
            continue

        for numComp, hashInfoComp in enumerate(hashList[(numOrig + 1):]):
            step += 1
            print(f"\r\tCompare {os.path.split(pathList[numOrig])[1]}({hashInfoOrig})", end='')
            print(f"\t\twith {os.path.split(pathList[numComp + numOrig + 1])[1]}({hashInfoComp})", end='')
            print(f"\t\t{numOrig + 1}/{imgCount - 1}(({(step / stepTotal) * 100:5.2f}%)", end='')

            if hashInfoOrig == hashInfoComp:
                print("\t\tDuplication Detected!!!")
                pathComp = pathList[numComp + numOrig + 1]

                keys = DuplDict.keys()
                if pathList[numOrig] not in keys:
                    DuplDict[pathList[numOrig]] = [pathComp]
                else:
                    DuplDict[pathList[numOrig]].append(pathComp)

                DuplCompListAll.append(pathComp)

    if len(DuplDict) != 0:
        print("\n\n\tDuplication File:")
        keys = DuplDict.keys()
        for key in keys:
            print(f"\t\tOrigin File: {key}")
            print(f"\t\t\t{len(DuplDict[key])} Duplicated File(s):")
            for pathComp in DuplDict[key]:
                print(f"\t\t\t\t{pathComp}")
    else:
        print("\n\n\tNone Duplication File Detected!!!")

    time_comp.show()

    return DuplDict


def view_delete(DulpDict):
    """
    View all duplicated images, which info stored in DulpDict.
    Press "Del" -> Delete duplicated images
    Press any other keys -> Ship

    @param DulpDict: DulpDict[pathOrig] = [pathComp1, pathCamp2, ...]
    """
    print("\nProceeding: Deleting Duplicated Image")
    keys = DulpDict.keys()
    for pathOrig in keys:
        imgOrig = cv2.imread(pathOrig)
        imgCompList = []
        for pathComp in DulpDict[pathOrig]:
            imgCompList.append(cv2.imread(pathComp))
        imgStake = stackImages(imgCompList, cols=len(imgCompList), scale=1 / len(imgCompList))
        imgStake = stackImages([imgOrig, imgStake], cols=1, scale=0.1)

        print(f"\tOrigin: {pathOrig}\t\tDuplication: {DulpDict[pathOrig]}", end='')

        cv2.putText(imgStake, "Press Del: Delete Dupilcation", (10, 25), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
        cv2.putText(imgStake, "Press Any Other Key: Ship", (10, 55), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)

        cv2.imshow("Image", imgStake)

        keyBoard = cv2.waitKey(0) & 0xFF
        if keyBoard == 8:
            for pathComp in DulpDict[pathOrig]:
                if os.path.exists(pathComp):
                    os.remove(pathComp)
            print("\t\tDeleted!")
        else:
            print("\t\tShipped!")

    print("Delete Down!\n")


if __name__ == '__main__':
    folderPath = r"D:\15152\Desktop\Lieber\Nordrhein-Westfalen"

    HashInfoGenerator(folderPath)
    DulpDict = find_duplication(folderPath)
    view_delete(DulpDict)

    print("********************************************************")
    print("***                   By Song T.C.                   ***")
    print("***       tiancheng.song@mailbox.tu-dresden.de       ***")
    print("********************************************************")
