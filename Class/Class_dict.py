# Programmed by Scar
"""
__dict__()
功能：
    显示当前可调用的方法和属性和其对应的值
"""


class Test(object):
    a = 1

    def b(self):
        pass


print(Test.__dict__)
