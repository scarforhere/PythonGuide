# Programmed by Scar
"""
为实例化对象添加属性与值
"""


class Test(object):
    a = 1
    b = 2

    def __init__(self):
        self.c = 3
        self.d = 4


test = Test()

setattr(test, 'e', 3)
print(test.e)
print(vars(test))
