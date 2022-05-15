# coding: utf-8
"""
-------------------------------------------------
   File Name:      Json_All
   Author :        Tiancheng Song
   E-mail :        tiancheng.song@mailbox.tu-dresden.de
   Date:           2022-02-13 02:12 AM
-------------------------------------------------
Description : 

    Rewrite json encoder to dump all kinds of files

"""
import json
import cv2
import PIL
from datetime import date, datetime
import numpy as np
import base64

class GEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, np.datetime64):
            return str(obj)[:10]
        elif isinstance(obj, bytes):
            return str(obj, encoding='utf-8');
        else:
            return super(GEncoder, self).default(obj)


# json.dumps(obj, cls=GEncoder)
class Gjson:
    def __init__(self):
        pass

    def JsonToString(self, data_json):
        data_string = json.dumps(data_json, cls=GEncoder)
        return data_string

    def StringToJson(self, data_str):
        data_json = json.loads(data_str)
        return data_json

    def SaveToFile(self, fn, data_json):
        data_str = self.JsonToString(data_json)
        with open(fn, 'w') as f:
            f.write(data_str)
            f.flush
        return True

    def ReadFromFile(self, fn):
        with open(fn, "rb") as json_file:
            data_str = json_file.read()
        data_json = self.StringToJson(data_str)
        return data_json


if __name__ == "__main__":
    gj = Gjson()
    fn_img = r"E:\Python_Code\PythonGuide\Module\Extern\OpenCV\StepIn\CH20\images\liudehua.jpg"
    img = cv2.imread(fn_img)

    dict_1 = {}
    dict_2 = {}
    dict_3 = {}

    dict_1["img"] = img
    res, data_encoded = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    dict_2["img"] = data_encoded
    encoded_image = base64.b64encode(data_encoded)
    dict_3["img"] = encoded_image
    fn_1 = "img_numpy.json"
    fn_2 = "img_str.json"
    fn_3 = "img_base64.json"

    gj.SaveToFile(fn_1, dict_1)
    gj.SaveToFile(fn_3, dict_3)
    gj.SaveToFile(fn_2, dict_2)

    o_1 = gj.ReadFromFile(fn_1)
    o_2 = gj.ReadFromFile(fn_2)
    o_3 = gj.ReadFromFile(fn_3)

    img1 = np.asarray(o_1["img"], dtype="uint8")
    img2 = o_2["img"]
    img2 = np.asarray(img2, dtype="uint8")
    img2 = cv2.imdecode(img2, cv2.IMREAD_COLOR)

    img3 = o_3["img"]
    img3 = base64.b64decode(img3)
    img3 = np.fromstring(img3, np.uint8)
    img3 = cv2.imdecode(img3, cv2.IMREAD_COLOR)

    cv2.imshow("o_1", img1)
    cv2.imshow("o_2", img2)
    cv2.imshow("o_3", img3)
    cv2.waitKey(0)
