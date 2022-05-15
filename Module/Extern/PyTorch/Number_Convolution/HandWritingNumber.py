# coding: utf-8
"""
-------------------------------------------------
   File Name:      HandWritingNumber
   Author :        Tiancheng Song
   E-mail :        tiancheng.song@mailbox.tu-dresden.de
   Date:           2022-03-14 10:18 AM
-------------------------------------------------
Description :

    Predict handwriting number(NN from myData datasets)  Accuracy: 95.96%

    Usage:
        model, _ = model_optimizer_init(model_path)
        pred, pred_probab = predict_from_extern(img, model)

    TensorBoard:
        tensorboard --logdir E:\\Python_Code\\PythonGuide\\Module\\Extern\\PyTorch\\Number_Convolution\\TensorBoard

"""
import os
import cv2
import numpy as np
from PIL import Image
import torch
from torch.utils.data import Dataset
from torchvision.transforms import Compose, ToTensor, Normalize, Resize, ToPILImage, Lambda
from torch.utils.data import DataLoader
from torch import nn
from torch.optim import Adam
from torch.utils.tensorboard import SummaryWriter
from Tools.GetAllFiles import get_all_files


device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device.upper()} device")

writer = SummaryWriter(r"E:\Python_Code\PythonGuide\Module\Extern\PyTorch\Number_Convolution\TensorBoard")
path = r"E:\Python_Code\PythonGuide\Module\Extern\PyTorch\Number_Convolution\Data"


def data_info_txt(path,image_type="png"):
    filelist = get_all_files(path, image_type)
    txt_path = ''.join([path, "\\data_info"])
    if os.path.exists(txt_path):
        os.remove(txt_path)

    for item in filelist:
        img_dir, _ = os.path.split(item)
        _, label = os.path.split(img_dir)
        item_path = item
        line_info = ''.join([label, ' ', item_path, "\n"])
        with open(txt_path, "a+") as f:
            f.writelines(line_info)


class MyDataSets(Dataset):
    def __init__(self, root, transform=None):
        self.data_info = self.get_img_info(root)
        self.transforms = transform

    def __getitem__(self, idx):
        label, img_path = self.data_info[idx]
        image = Image.open(img_path).convert('L')
        if self.transforms is not None:
            image = self.transforms(image)
        label = eval(label)
        return image, label

    def __len__(self):
        return len(self.data_info)

    @staticmethod
    def get_img_info(data_path):
        data_info = []
        txt_path = ''.join([data_path, "\\data_info"])
        if not os.path.exists(txt_path):
            data_info_txt(data_path)
        with open(txt_path) as f:
            lines = f.readlines()
            for line in lines:
                data_info.append(line.strip('\n').split(' '))
        return data_info


def get_mean_std(path):
    transform_fn = Compose([
        ToTensor(),
        Resize((32, 32)),
    ])
    data = MyDataSets(root=path, transform=transform_fn)

    mean, var = 0, 0
    data_len = len(data)
    for i, item in enumerate(data):
        print(f"\rMean: {i + 1}/{data_len} ({(i + 1) / data_len * 100:3.2f}%)", end='')
        data_item = item[0]
        data_item = 1 - data_item
        np_data = np.array(data_item)
        mean += np_data.mean()
    mean = mean / data_len
    print()
    for i, item in enumerate(data):
        print(f"\rVariance: {i + 1}/{data_len} ({(i + 1) / data_len * 100:3.2f}%)", end='')
        data_item = item[0]
        data_item = 1 - data_item
        np_data = np.array(data_item)
        var += np.var(np_data)
    std = (var / data_len) ** 0.5
    print()

    print(f"mean_std=({mean}, {std})")
    return mean, std


def data_load(path, batch_size, train_ratio=0.9, mean_std=None):
    if mean_std is None:
        mean, std = get_mean_std(path)
    else:
        mean, std = mean_std

    transform_fn = Compose([
        ToTensor(),
        Resize((32, 32)),
        Lambda(lambda imgTensor: 1 - imgTensor),
        Normalize(mean=(mean,), std=(std,))
    ])
    data = MyDataSets(root=path, transform=transform_fn)

    data_num_total = len(data)
    data_num_train = int(train_ratio * data_num_total)
    data_num_test = data_num_total - data_num_train

    data_train, data_test = torch.utils.data.random_split(data, [data_num_train, data_num_test])
    data_sets_train = DataLoader(data_train, batch_size=batch_size, shuffle=True)
    data_sets_test = DataLoader(data_test, batch_size=batch_size, shuffle=True)

    return data_sets_train, data_sets_test


class CIFAR10Module(nn.Module):
    def __init__(self):
        super(CIFAR10Module, self).__init__()
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
    model = CIFAR10Module().to(device)
    optimizer = Adam(model.parameters(), lr=lr)
    model_path = ''.join([path, "\\model"])
    optimizer_path = ''.join([path, "\\optimizer"])
    if os.path.exists(model_path):
        model.load_state_dict(torch.load(model_path))
        optimizer.load_state_dict(torch.load(optimizer_path))
    return model, optimizer


def train(epoch, data_sets_train, data_sets_test, model, optimizer, path, display=False):
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
                      f"Loss: {loss.item():2.6f}\t\tAccuracy: {100 * acc:3.2f}%")
                if display:
                    x = i * len(data_sets_train) + batch
                    writer.add_scalar("Loss Value", loss.item(), x)
                    writer.close()
                    writer.add_scalar("Accuracy", acc * 100, x)
                    writer.close()

        torch.save(model.state_dict(), ''.join([path, "\\model"]))
        torch.save(optimizer.state_dict(), ''.join([path, "\\optimizer"]))


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
            return pred.argmax(), pred_fn(pred).max()
        else:
            return None


def test_from_databank(path, model):
    data_set = next(iter(data_load(path, 1, train_ratio=0.9, mean_std=(0.16069158812321166, 0.3506009024555226))))
    data = next(iter(data_set))
    data_pred = data[0]
    print(f"Actual : {data[1].item()}")
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


def predict_from_extern(img, model):
    if isinstance(img, np.ndarray):
        imgPIL = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    else:
        imgPIL = img
    imgPIL = imgPIL.convert('L')
    imgPIL = imgPIL.resize((32, 32))
    imgPIL.show()
    data_pred = ToTensor()(imgPIL)
    data_pred = torch.unsqueeze(data_pred, 1)
    return predict(data_pred, model, test_mode=True)


def test_from_extern(path, model, idx, image_type):
    path_lst = get_all_files(path, image_type)
    imgPIL = Image.open(path_lst[idx])
    imgCV2 = cv2.imread(path_lst[idx])
    res = predict_from_extern(imgCV2, model)
    pred, pred_probab = res
    print(f"Predict: {pred}\t\tPredict Probability: {100 * pred_probab:2.2f}%")


if __name__ == '__main__':
    path = r"E:\Python_Code\PythonGuide\Module\Extern\PyTorch\Number_Convolution\Data"

    model, optimizer = model_optimizer_init(path, 0.0000001)
    # print(model)

    # mean_std=(0.16069158812321166, 0.3506009024555226)
    # data_sets_train, data_sets_test = data_load(path, 20000, train_ratio=0.9, mean_std=mean_std)

    # train(10000, data_sets_train, data_sets_test, model, optimizer, path, False)

    test_from_databank(path, model)

    # path = r"E:\Guitar Score\Number_Test"
    # test_from_extern(path, 0, "jpg")

    print("********************************************************")
    print("***                   By Song T.C.                   ***")
    print("***       tiancheng.song@mailbox.tu-dresden.de       ***")
    print("********************************************************")

