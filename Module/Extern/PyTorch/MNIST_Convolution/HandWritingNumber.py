# coding: utf-8
"""
-------------------------------------------------
   File Name:      HandWritingNumber
   Author :        Tiancheng Song
   E-mail :        tiancheng.song@mailbox.tu-dresden.de
   Date:           2022-03-13 05:43 PM
-------------------------------------------------
Description : 

    Predict handwriting number(NN from MNIST datasets)  Accuracy: 98.79%

    Usage:
        model, _ = model_optimizer_init(model_path)
        pred, pred_probab = predict_from_extern(img, model)

    TensorBoard:
        tensorboard --logdir E:\\Python_Code\\PythonGuide\\Module\\Extern\\PyTorch\\MNIST_Convolution\\TensorBoard

"""
import os
import cv2
import numpy as np
from PIL import Image
import torch
from torchvision.datasets import MNIST
from torchvision.transforms import Compose, ToTensor, Normalize, Resize, ToPILImage
from torch.utils.data import DataLoader
from torch import nn
from torch.optim import Adam
from torch.utils.tensorboard import SummaryWriter
from Tools.GetAllFiles import get_all_files

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device.upper()} device")

writer = SummaryWriter(r"E:\Python_Code\PythonGuide\Module\Extern\PyTorch\MNIST_Convolution\TensorBoard")


def data_load(path, batch_size, train=False):
    transform_fn = Compose([
        ToTensor(),
        Resize((32, 32)),
        Normalize(mean=(0.1307,), std=(0.3081,))
    ])

    mnist = MNIST(root=path, train=train, download=True, transform=transform_fn)
    data_sets = DataLoader(mnist, batch_size=batch_size, shuffle=True)

    return data_sets


class MnistModule(nn.Module):
    def __init__(self):
        super(MnistModule, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Conv2d(1, 8, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(8, 8, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(8, 16, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(256, 64),
            nn.ReLU(),
            nn.Linear(64, 10)
        )

    def forward(self, inlet):
        out = self.linear_relu_stack(inlet)
        return out


def model_optimizer_init(path, lr=0.00001):
    model = MnistModule().to(device)
    optimizer = Adam(model.parameters(), lr=lr)
    model_path = ''.join([path, "\\model"])
    optimizer_path = ''.join([path, "\\optimizer"])
    if os.path.exists(model_path):
        model.load_state_dict(torch.load(model_path))
        optimizer.load_state_dict(torch.load(optimizer_path))
    return model, optimizer


def train(epoch, data_sets_train, data_sets_test, model, optimizer, display=False):
    batch_size = len(data_sets_train)
    for i in range(epoch):
        loss_fn = nn.CrossEntropyLoss()

        for batch, (x, y) in enumerate(data_sets_train):
            x, y = x.to(device), y.to(device)

            pred = model(x)
            loss = loss_fn(pred, y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if batch % 1 == 0:
                acc = test(data_sets_test, model)
                print(f"\rEpoch: {i + 1}\t\tBatch: {batch + 1}/{batch_size}\t\t"
                      f"Loss: {loss.item():2.6f}\t\tAccuracy: {100 * acc:2.2f}%")
                if display:
                    x = i * len(data_sets_train) + batch
                    writer.add_scalar("Loss Value", loss.item(), x)
                    writer.close()
                    writer.add_scalar("Accuracy", acc * 100, x)
                    writer.close()

        torch.save(model.state_dict(), r"./Data/model")
        torch.save(optimizer.state_dict(), r"./Data/optimizer")
        print()


def test(data_sets_test, model):
    acc = 0
    model.eval()
    for batch, (x, y) in enumerate(data_sets_test):
        x, y = x.to(device), y.to(device)
        with torch.no_grad():
            pred = model(x)
            acc += (pred.argmax(1) == y).float().sum().item()
        acc /= len(data_sets_test.dataset)
    return acc


def predict(data, model, thres=0.85, test_mode=False):
    model.eval()
    pred_fn = nn.Softmax(dim=1)
    with torch.no_grad():
        data = data.to(device)
        pred = model(data)
        if pred_fn(pred).max() >= thres or test_mode is True:
            return pred.argmax().item(), pred_fn(pred).max().item()
        else:
            return None


def test_from_databank(path, model):
    data_set = next(iter(data_load(path, 1, False)))
    data_pred = data_set[0]
    print(f"Actual : {data_set[1].item()}")
    data_img = torch.squeeze(data_pred, 1)
    print(data_pred.size())
    imgPIL = ToPILImage()(data_img)
    imgPIL = Resize((500, 500))(imgPIL)
    imgPIL.show()
    res = predict(data_pred, model, test_mode=True)
    if res is not None:
        pred, pred_probab = res
        print(f"Predict: {pred}\t\tPredict Probability: {100 * pred_probab:2.2f}%")
    else:
        print(f"None Number is detected!!!")


def predict_from_extern(img, model, thres=0.85, test=False, display=False):
    if isinstance(img, np.ndarray):
        imgPIL = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    else:
        imgPIL = img
    imgPIL = imgPIL.convert('L')
    imgPIL = imgPIL.resize((32, 32))
    if display:
        imgPIL.show()
    data_pred = ToTensor()(imgPIL)
    data_pred = torch.unsqueeze(data_pred, 1)
    return predict(data_pred, model, thres=0.85, test_mode=test)


def test_from_extern(path, model, idx, image_type):
    path_lst = get_all_files(path, image_type)
    imgPIL = Image.open(path_lst[idx])
    imgCV2 = cv2.imread(path_lst[idx])
    res = predict_from_extern(imgCV2, model)
    pred, pred_probab = res
    print(f"Predict: {pred}\t\tPredict Probability: {100 * pred_probab:2.2f}%")


if __name__ == '__main__':
    MNIST_datasets_path = r".\Data"

    model, optimizer = model_optimizer_init(MNIST_datasets_path, 0.00001)
    # print(model)

    # data_sets_train = data_load(MNIST_datasets_path, 10000, True)
    # data_sets_test = data_load(MNIST_datasets_path, 10000, False)
    # train(10000, data_sets_train, data_sets_test, model, optimizer, False)

    test_from_databank(MNIST_datasets_path, model)

    # path = r"E:\Guitar Score\Number_Test"
    # test_from_extern(path, model, 1, "jpg")

    print("********************************************************")
    print("***                   By Song T.C.                   ***")
    print("***       tiancheng.song@mailbox.tu-dresden.de       ***")
    print("********************************************************")
