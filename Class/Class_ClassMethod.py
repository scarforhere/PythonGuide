# Programmed by Scar
"""
类方法时针对类对象定义的方法
    在类方法内部可以直接访问类属性，或者调用其他的类方法

类方法需要用修饰器@classmethod来表示，告诉解释器这是一个类方法
    注意：不经过实例化也可以调用
类方法的第一个参数影视cls
    由哪一个类调用的方法，方法内cls就是哪一个类的引用
    这个参数和实例方法的第一个参数self剋四
    提示使用其他名称也可以，不过习惯使用cls
通过类名，调用类方法，调用方法时，不需要传递cls参数、
在方法内部
    可以通过cls.访问类属性
    也可以通过cls.调用其他类方法
"""


class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    def __init__(self, name):
        self.name = name

        # 类属性的值+1
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        print(f"当前工具对象数量为： {cls.count}")


# 1. 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

# 2. 输出工具对象数量
Tool.show_tool_count()