# Programmed by Scar
"""
__str__()
使用print输出对象变量，默认情况下，会输出
    这个变量用用的对象是由哪一个类创建的对象
    在内存中的地址（十六禁止表示）

如果在开发中希望使用print输出对象变量时，能够打印自定义内容可以使用内置__str__()方法

注意： __str__()方法必须返回一个字符串
"""


class Demo:
    def __init__(self, new_name):
        self.name = new_name
        print(f"{self.name}程序开始执行")

    def __str__(self):
        return "这是内置方法__str__()所保存的字符串"


sss = Demo("Scar")
print(sss)
