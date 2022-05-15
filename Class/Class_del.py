# Programmed by Scar
"""
__del__()
内置方法在使用类创建新的对象被内存释放时被优先执行
一般在该内置方法中保存该对象在生命周期结束前需要的操作
"""


class Demo:
    def __init__(self, new_name):
        self.name = new_name
        print(f"{self.name}程序开始执行")

    def __del__(self):
        print(f"{self.name}程序结束执行")


# sss为全局变量，所以程序结束时才会释放sss所占内存，执行__del__()
sss = Demo("Scar")
print(sss.name)
print("-" * 40)
