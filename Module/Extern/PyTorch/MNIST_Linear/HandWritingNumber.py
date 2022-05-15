# coding: utf-8
"""
-------------------------------------------------
   File Name:      HandWritingNumber
   Author :        Tiancheng Song
   E-mail :        tiancheng.song@mailbox.tu-dresden.de
   Date:           2022-03-12 08:30 PM
-------------------------------------------------
Description : 

    Print info with under format:

"""
import numpy as np
import torch
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision.transforms import Compose, ToTensor, Normalize
from torch import nn
from torch.optim import Adam
import os
import matplotlib.pyplot as plt



batch_size = 64
test_batch_size = 1000

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device.upper()} device")


def data_load(path, batch_size, train=False):
    """
    """
    transform_fn = Compose([
        ToTensor(),
        Normalize(mean=(0.1307,), std=(0.3081,))
    ])

    mnist = MNIST(root=path, train=train, download=False, transform=transform_fn)
    data_sets = DataLoader(mnist, batch_size=batch_size, shuffle=True)

    return data_sets


class MnistModule(nn.Module):
    def __init__(self):
        super(MnistModule, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28 * 28, 256),
            nn.ReLU(),
            nn.Linear(256, 64),
            nn.ReLU(),
            nn.Linear(64, 10),
        )

    def forward(self, inlet):
        x = self.flatten(inlet)
        out = self.linear_relu_stack(x)
        return out


def model_optimizer_init(path, lr=0.00001):
    model = MnistModule().to(device)
    optimizer = Adam(model.parameters(), lr=0.00001)
    model_path = ''.join([path, "\\model"])
    optimizer_path = ''.join([path, "\\optimizer"])
    if os.path.exists(model_path):
        model.load_state_dict(torch.load(model_path))
        optimizer.load_state_dict(torch.load(optimizer_path))
    return model, optimizer


def train(epoch, data_sets, model, optimizer, display=False):
    loss_lst = []
    batch_size = len(data_sets)
    for i in range(epoch):
        loss_fn = nn.CrossEntropyLoss()

        for batch, (x, y) in enumerate(data_sets):
            x, y = x.to(device), y.to(device)

            pred = model(x)
            loss = loss_fn(pred, y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if batch % 100 == 0:
                print(f"\repoch: {i+1}\t\tbatch: {batch + 1}/{batch_size}\t\tloss: {loss.item():2.6f}")
                if display:
                    loss_lst.append(loss.item())
                    plt.plot(loss_lst)
                    plt.show()

        torch.save(model.state_dict(), r"./Data/model")
        torch.save(optimizer.state_dict(), r"./Data/optimizer")
        print()


def test(data_sets, model):

    loss_fn = nn.CrossEntropyLoss()
    test_loss, correct = 0, 0
    model.eval()
    for batch, (x, y) in enumerate(data_sets):
        x, y = x.to(device), y.to(device)
        with torch.no_grad():
            pred = model(x)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).float().sum().item()
        test_loss /= len(data_sets)
        correct /= len(data_sets.dataset)
        print(f"\r{batch + 1} / {len(data_sets)}", end='')
    print()
    print(f"Acc = {100 * np.mean(correct):2.2f}%\t\tLoss = {np.mean(test_loss):}")


def predict(data, model):
    model.eval()
    pred_fn = nn.Softmax(dim=1)
    with torch.no_grad():
        data = data.to(device)
        pred = model(data)
        print(pred_fn(pred))
        return pred.argmax(), pred_fn(pred).max()


if __name__ == '__main__':
    path = r"./Data"

    model, optimizer = model_optimizer_init(path, 0.0001)

    # data_sets = data_load(path, 64, True)
    # train(10, data_sets, model, optimizer)

    # data_sets_test = data_load(path, 10000, False)
    # test(data_sets_test, model)

    # data_set = next(iter(data_load(path, 1, False)))
    # data_pred = data_set[0][0]
    # print(f"Actual : {data_set[1][1]}")
    # pred, pred_probab = predict(data_pred, model)
    # print(f"Predict: {pred}\t\tPredict Probability: {100 * pred_probab:2.2f}%")

    print("********************************************************")
    print("***                   By Song T.C.                   ***")
    print("***       tiancheng.song@mailbox.tu-dresden.de       ***")
    print("********************************************************")
