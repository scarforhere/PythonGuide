# coding: utf-8
"""
-------------------------------------------------
   File Name:      Match
   Author :        Tiancheng Song
   E-mail :        tiancheng.song@mailbox.tu-dresden.de
   Date:           2022-04-07 09:42 PM
-------------------------------------------------
Description : 

    Print info with under format:

"""


def switch_demo(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print(switcher.get(argument, "Invalid month"))


if __name__ == '__main__':
    s = int(input("Input: "))
    switch_demo(s)

    print("********************************************************")
    print("***                   By Song T.C.                   ***")
    print("***       tiancheng.song@mailbox.tu-dresden.de       ***")
    print("********************************************************")
