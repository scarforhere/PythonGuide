# coding: utf-8
"""
-------------------------------------------------
   File Name:      InstallerCheck
   Author :        Tiancheng Song
   E-mail :        tiancheng.song@mailbox.tu-dresden.de
   Date:           2022-03-11 11:34 PM
-------------------------------------------------
Description : 

    Print info with under format:

"""
import torch

def main():
    print(torch.cuda.is_available())
    print(torch.version.cuda)


if __name__ == '__main__':
    main()

    print("********************************************************")
    print("***                   By Song T.C.                   ***")
    print("***       tiancheng.song@mailbox.tu-dresden.de       ***")
    print("********************************************************")
