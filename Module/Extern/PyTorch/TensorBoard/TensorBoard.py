# coding: utf-8
"""
-------------------------------------------------
   File Name:      TensorBoard
   Author :        Tiancheng Song
   E-mail :        tiancheng.song@mailbox.tu-dresden.de
   Date:           2022-03-13 02:34 PM
-------------------------------------------------
Description : 

    In Terminal Type:
        tensorboard --logdir log_path

"""
import torch
import numpy as np
from PIL import Image
from Tools.GetAllFiles import get_all_files
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter(r"E:\Python_Code\PythonGuide\Module\Extern\PyTorch\TensorBoard")

for i in range(1000):
    x = i
    y = x ** 2 + 500
    writer.add_scalar("Y = X ^ 2 + 500", y, x)

image_path = r"E:\Guitar Score\Test"
path_lst = get_all_files(image_path, "png")[:10]
for i, path in enumerate(path_lst):
    image_PIL = Image.open(path)
    image_array = np.array(image_PIL)
    writer.add_image("Score", image_array, i+1, dataformats="HWC")

writer.close()

print("********************************************************")
print("***                   By Song T.C.                   ***")
print("***       tiancheng.song@mailbox.tu-dresden.de       ***")
print("********************************************************")
