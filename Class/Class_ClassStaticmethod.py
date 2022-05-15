# Programmed by Scar
"""
在开发时，如果需要在类中封装一个方法，这个方法：
    既不需要访问类属性或者调用实例方法
    也不需要访问类属性或者调用类方法
注意：不经过实例化也可以调用

这个时候，可以把这个方法封装乘一个静态方法

类方法需要用修饰器@staticmethod来表示，告诉解释器这是一个静态方法
"""


class Dog(object):

    @staticmethod
    def run():
        print("小狗要跑...")

# 通过类名.调用静态方法
Dog.run()