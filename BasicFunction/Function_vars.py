# Programmed by Scar
"""
将实例化的对象内所包含的对象属性作为字典返回
"""


class Test(object):
    a = 1
    b = 2

    def __init__(self):
        self.c = 3
        self.d = 4


test = Test()
result = vars(test)
print(result)

print(vars(Test))
