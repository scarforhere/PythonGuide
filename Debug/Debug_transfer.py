# Programmed by Scar
"""
产生异常时不会立刻终止程序
产生异常时会返回一个异常值并向前置程序检索异常处理
如果检索至主程序无异常处理机制，则终止程序

利用异常的传递性，在主程序中捕获异常，不必在每个函数中捕获异常
"""


def demo1():
    return int(input("输入整数："))


def demo2():
    return demo1()


# 利用异常的传递性，在主程序中捕获函数内部中的异常
try:
    print(demo2())
except Exception as result:
    print(f"错误位置：{result}")
