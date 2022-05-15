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
    Double press <Ctrl + C> to clip
    Press <Ctrl + Alt + E> to esc

    pyinstaler to .exe:
    --hidden-import "pynput.keyboard._win32" --hidden-import "pynput.mouse._win32"

"""
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
    content = pyperclip.paste()  # copy content from clipboard into Var content
    content = delete_newline_char(content)  # delete return symbol in Var content
    pyperclip.copy(content)  # paste content back to clipboard
    while (True):
        content_tmp = pyperclip.paste()
        # print("监听剪切板")
        if (content_tmp != content):
            # print("监听剪切板变化")
            content = content_tmp
            content = delete_newline_char(content)
            pyperclip.copy(content)

        eEvent.wait()
        eEvent.clear()


"""
Hotkey to esc
"""
isEnd = False
listenerEsc = None


def on_activate_esc():
    print("Clipboard Monitoring Stopped!!!")
    global isEnd
    isEnd = True
    return False


# create hotkey monitor
hotkeyEsc = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<alt>+e'), on_activate_esc)


def for_canonical_esc(f):
    global listenerEsc
    return lambda k: f(listenerEsc.canonical(k))


"""
Hotkey to clip
"""
eEvent = threading.Event()

listenerClip = None
tap_num = 0


def on_activate_clip():
    global tap_num
    tap_num += 1
    if tap_num == 2:
        print("Clip Change Detected!!!")
        eEvent.set()
        tap_num = 0
    return False


# create hotkey monitor
hotkeyClip = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+c'), on_activate_clip)


def signal_press_to_hotkeys(key):
    hotkeyClip.press(listenerClip.canonical(key))


def signal_release_to_hotkeys(key):
    hotkeyClip.release(listenerClip.canonical(key))


def main():
    global isEnd
    global listenerEsc
    global listenerClip
    # create hotkey monitor
    listenerEsc = keyboard.Listener(on_press=for_canonical_esc(hotkeyEsc.press))
    listenerEsc.daemon = 1
    listenerClip = keyboard.Listener(on_press=signal_press_to_hotkeys, on_release=signal_release_to_hotkeys)
    listenerClip.daemon = 1


    # create functional methode
    t2 = threading.Thread(target=clip_board_monitor)
    t2.daemon = 1

    listenerEsc.start()
    listenerClip.start()
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
