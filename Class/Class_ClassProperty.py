# Programmed by Scar
"""
类是一个特殊的对象--类对象
类对象在内存中只有一份，使用一个类可以创建多个对象实例
除了封装石磊的属性和方法外，类对象还可以拥有自己的属性和方法
    类属性
    类方法

注意： 类属性记录跟类相关特征，不会记录跟对象相关特征
"""
# 完整写法
class Space(object):

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value

    def __init__(self, name):
        self.__name = name

x1=Space("Scar")
print(x1.name)
x1.name="Super Scar"
print(x1.name)
print()


#简单写法
class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    def __init__(self, name):
        self.name = name

        # 类属性的值+1
        Tool.count += 1


# 1. 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

# 2. 输出工具对象数量
print(Tool.count)
print(tool1.count) # 不推荐使用
