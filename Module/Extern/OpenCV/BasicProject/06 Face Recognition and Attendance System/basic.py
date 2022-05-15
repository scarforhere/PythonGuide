# coding: utf-8
"""
-------------------------------------------------
   File Name:      basic
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-15 10:51 AM
-------------------------------------------------
Description :

    Face Recognition

        Step:
            1. load Image
            2. turn image from BGR into RGB
            3. face locations detection
            4. face location feature encoding
            5. repeat for image to be tested
            6. compare

"""
import cv2
import face_recognition

imgElon = face_recognition.load_image_file('ImagesBasic/Elon Musk.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImagesBasic/Elon Musk_test.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# get a list of location feature of images
# Location: Top Right Bottom Left
faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

# use SVM to compare
# Bool list of result
results = face_recognition.compare_faces([encodeElon], encodeTest)
# distance- match+
faceDis = face_recognition.face_distance([encodeElon], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('Elon Musk', imgElon)
cv2.imshow('Elon Test', imgTest)
cv2.waitKey(0)

cv2.destroyAllWindows()

