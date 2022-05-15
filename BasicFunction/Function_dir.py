# Programmed by Scar
"""
在Python中所有东西都是对象

验证方法：
    1. 在标识符/数据后输入一个"."然后按下"TAB"键，iPython会提示该对象能够调用的方法列表
    2. 使用内置函数dir传入标识符/数据，可以查看对象内的所有属性和方法

"""


def demo():
    """
    这是一个测试用的demo函数

    :return:
    """
    print("hallo python")


print(dir(demo))

print(demo.__doc__)
