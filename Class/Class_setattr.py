# Programmed by Scar
"""
__setattr__()
功能：
    拦截当前类不存在的属性与值
"""


class Test(object):
    def __setattr__(self, key, value):
        self.__dict__[key] = value


t = Test()
t.name = 'Scar'
print(t.name)
