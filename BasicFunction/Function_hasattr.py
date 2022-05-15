# Programmed by Scar
"""
判断实例化的对象中是否有某个类属性并返回bool值
"""


class Test(object):
    a = 1
    b = 2

    def __init__(self):
        self.c = 3
        self.d = 4


print(hasattr('1', 'upper'))
print(hasattr('1', 'fuck'))

print(hasattr(Test, 'a'))
print(hasattr(Test, 'c'))
