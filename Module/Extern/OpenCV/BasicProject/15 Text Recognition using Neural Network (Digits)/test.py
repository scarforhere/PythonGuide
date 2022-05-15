# coding: utf-8
"""
-------------------------------------------------
   File Name:      utils
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-12-15 10:51 AM
-------------------------------------------------
Description :

    OCR-CNN for number recognize

"""
from tensorflow.python.keras.models import load_model
import numpy as np
import cv2
from tensorflow.python.keras.models import model_from_json

"""
PARAMETERS
"""
width = 640
height = 480
threshold = 0.65  # MINIMUM PROBABILITY TO CLASSIFY

"""
CREATE CAMERA OBJECT
"""
cap = cv2.VideoCapture('http://192.168.178.48:4747/video')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


"""
LOAD THE TRAINNED MODEL
"""
# with open("model_trained.txt", "r") as f:
#     json_out = f.read()
#     model = model_from_json(json_out)
model = load_model("model_trained")

"""
PRE-PROCESSING FUNCTION
"""
def preProcessing(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img / 255
    return img


while True:
    success, imgOriginal = cap.read()
    imgOriginal = cv2.rotate(imgOriginal, cv2.ROTATE_90_CLOCKWISE)
    # imgOriginal = cv2.imread(r"E:\Python_Code\PythonGuide\Module\Extern\OpenCV\BasicProject\15 Text Recognition using Neural Network (Digits)\myData\4\img005-00005.png")
    img = np.asarray(imgOriginal)

    img = cv2.resize(img, (32, 32))
    img = preProcessing(img)
    # cv2.imshow("Processsed Image", img)
    img = img.reshape(1, 32, 32, 1)
    """
    PREDICT
    """
    predict_x = model.predict(img)
    classIndex = np.argmax(predict_x)
    print(predict_x)

    # print(predictions)
    probVal = np.amax(predict_x)
    # probVal = int(round(probVal * 100))

    # Avoid too low accurate probability
    if probVal > threshold:
        cv2.putText(imgOriginal, str(classIndex) + "   " + str(int(round(probVal * 100))) + "%",
                    (50, 50), cv2.FONT_HERSHEY_COMPLEX,
                    1, (0, 0, 255), 1)

    cv2.imshow("Original Image", imgOriginal)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
