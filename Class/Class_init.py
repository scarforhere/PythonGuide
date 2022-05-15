# Programmed by Scar
"""
__init__()
内置方法在使用类创建新的对象时被优先执行
一般在该内置方法中保存初始属性
"""


# 在对象生命周期开始希望被执行的程序放在__init__()方法中
class Car:
    def __init__(self):
        print("该对象已被初始化")


car1 = Car
print()


# 类中self变量相当于调用此类创建的对象
class Car:
    def __init__(self):
        print(f"类中self在对象car2中地址为:{self}")


car2 = Car
print("car2的地址为%x" % id(car2))
print()


# 针对类中通用属性可以通过__init__()定义
# 在创建该类对象是需要对属性进行定义
class Car:
    def __init__(self, index_type, index_name):
        self.tpye = index_type
        self.name = index_name


car3 = Car("BWM", "Scar")
print(car3.name)
print(car3.tpye)
