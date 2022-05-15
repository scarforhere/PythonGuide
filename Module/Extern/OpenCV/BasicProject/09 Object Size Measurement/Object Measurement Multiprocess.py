# coding: utf-8
"""
-------------------------------------------------
   File Name:      Object Measurement Multiprocess
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2022-01-01 01:58 PM
-------------------------------------------------
Description : 

    Measure length of 4 bounders objects in A4 Paper
        use multi core

"""
import cv2
import utlis
import multiprocessing

webcam = True
path = '1.jpg'
cap = cv2.VideoCapture('http://192.168.178.48:4747/video')
cap.set(cv2.CAP_PROP_BRIGHTNESS, 160)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
scale = 3
wP = 210 * scale
hP = 297 * scale

queen_frame = []
queen_a4 = []


def detector_a4(inputQueen, outputQueen):
    while True:
        try:
            img = inputQueen.get()
            imgContours, conts = utlis.getContours(img, minArea=50000, filter=4)

            if len(conts) != 0:
                biggest = conts[0][2]
                # print(biggest)
                imgWarp = utlis.warpImg(img, biggest, wP, hP)

                outputQueen.put((imgWarp, conts))
        except:
            continue


def detector_object(inputQueen, a):
    while True:
        try:
            imgWarp, conts = inputQueen.get()
            imgContours2, conts2 = utlis.getContours(imgWarp, minArea=2000, filter=4, cThr=[50, 50], draw=False)

            if len(conts) != 0:
                for obj in conts2:
                    cv2.polylines(imgContours2, [obj[2]], True, (0, 255, 0), 2)
                    nPoints = utlis.reorder(obj[2])
                    nW = round((utlis.findDis(nPoints[0][0] // scale, nPoints[1][0] // scale) / 10), 1)
                    nH = round((utlis.findDis(nPoints[0][0] // scale, nPoints[2][0] // scale) / 10), 1)
                    cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]),
                                    (nPoints[1][0][0], nPoints[1][0][1]),
                                    (255, 0, 255), 3, 8, 0, 0.05)
                    cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]),
                                    (nPoints[2][0][0], nPoints[2][0][1]),
                                    (255, 0, 255), 3, 8, 0, 0.05)
                    x, y, w, h = obj[3]
                    cv2.putText(imgContours2, '{}cm'.format(nW), (x + 30, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                1.5, (255, 0, 255), 2)
                    cv2.putText(imgContours2, '{}cm'.format(nH), (x - 70, y + h // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                1.5, (255, 0, 255), 2)
            cv2.imshow('A4', imgContours2)
            cv2.waitKey(10)
        except:
            continue


if __name__ == '__main__':
    a = None

    # 创建输入q和输出q
    qf = multiprocessing.Queue()
    qa = multiprocessing.Queue()
    queen_frame.append(qf)
    queen_a4.append(qa)

    # 多核
    p1 = multiprocessing.Process(target=detector_a4, args=(qf, qa))
    p2 = multiprocessing.Process(target=detector_object, args=(qa, a))
    for p in (p1, p2):
        p.daemon = True
        p.start()

    while True:
        success, img = cap.read()
        img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

        for qf in queen_frame:
            qf.put(img)

        img = cv2.resize(img, (0, 0), None, 0.5, 0.5)
        cv2.imshow('Original', img)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()