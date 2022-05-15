# Programmed by Scar
"""
通过对象或取属性并返回所在内存地址
"""


class Test(object):
    a = 1
    b = 2

    def __init__(self):
        self.c = 3
        self.d = 4

    def method(self):
        pass


print(getattr(Test, "method"))
# print(getattr(Test,"methode"))
