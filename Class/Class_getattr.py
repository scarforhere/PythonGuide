# Programmed by Scar
"""
__getattr__()
功能：
    当调用的属性或者方法不存在时，会返回该方法定义的信息
"""


class Test(object):
    def __getattr__(self, item):
        print(f"这个方法或属性:{item}不存在!")


test = Test()
test.a
