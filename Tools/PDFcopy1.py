# coding: utf-8
"""
-------------------------------------------------
   File Name:      PDFcopy1
   Author :        Tiancheng Song
   E-mail :        tiancheng.song@mailbox.tu-dresden.de
   Date:           2022-05-04 10:53 PM
-------------------------------------------------
Description : 

    Copy text from PDF and remove return
    Press <Ctrl + Alt + E> to esc

    pyinstaler to .exe:
    --hidden-import "pynput.keyboard._win32" --hidden-import "pynput.mouse._win32"

"""
import time
import pyperclip
import threading
from pynput import keyboard


def delete_newline_char(message):
    """
    Delete symbols for return and connection

    :param message: Original String
    :return: Worked String
    """
    message = message.replace('\r\n', ' ')  # replace '\r\n' in message with ' '
    message = message.replace('\2', '')  # delete works connection symbol in message
    return message


def clip_board_monitor():
    """
    Monitoring clipboard to replace "\r\n" with " ” and delete "\2"
    """
    print("Clipboard Monitoring!!!")
    content = pyperclip.paste()  # copy content from clipboard into Var content
    content = delete_newline_char(content)  # delete return symbol in Var content
    pyperclip.copy(content)  # paste content back to clipboard

    while True:  # monitoring changing of content every 0.2 second
        time.sleep(1)
        content_tmp = pyperclip.paste()
        if content_tmp != content:  # if content in clipboard changes, renew content
            content = content_tmp
            content = delete_newline_char(content)
            pyperclip.copy(content)


isEnd = False
listener = None


def on_activate():
    print("Clipboard Monitoring Stopped!!!")
    global isEnd
    isEnd = True
    return False

# create hotkey monitor
hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<alt>+e'), on_activate)


def for_canonical(f):
    global listener
    return lambda k: f(listener.canonical(k))


def main():
    global isEnd
    global listener
    # create hotkey monitor
    listener = keyboard.Listener(on_press=for_canonical(hotkey.press))
    listener.daemon = 1

    # create functional methode
    t2 = threading.Thread(target=clip_board_monitor)
    t2.daemon = 1

    listener.start()
    t2.start()

    while True:
        if isEnd:
            return


if __name__ == '__main__':
    main()

    print("********************************************************")
    print("***                   By Song T.C.                   ***")
    print("***       tiancheng.song@mailbox.tu-dresden.de       ***")
    print("********************************************************")
