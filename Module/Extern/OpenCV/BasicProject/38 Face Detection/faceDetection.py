# coding: utf-8
"""
-------------------------------------------------
   File Name:      faceDetection
   Author :        Tiancheng Song
   E-mail :        tiancheng.song@mailbox.tu-dresden.de
   Date:           2022-01-14 09:43 PM
-------------------------------------------------
Description : 

    Print info with under format:

"""
import cv2

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier(
    r"E:\Python_Code\PythonGuide\Module\Extern\OpenCV\BasicProject\38 Face "
    r"Detection\haarcascades\haarcascade_frontalface_default.xml")


cap = cv2.VideoCapture('http://192.168.178.48:4747/video')

while True:
    # Choose an imge to detect faces in
    # img = cv2.imread("liudehua2.jpg")
    success, img = cap.read()

    # Must convert to grayscale
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscale_img)

    # Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 10)

    cv2.imshow("RDJ", img)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

print("********************************************************")
print("***                   By Song T.C.                   ***")
print("***       tiancheng.song@mailbox.tu-dresden.de       ***")
print("********************************************************")
