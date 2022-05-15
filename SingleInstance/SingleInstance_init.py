# Programmed by Scar
"""
只执行一次初始化工作
    当使用单例设计模式时只有唯一对象，所以只需要执行一次初始化
解决办法：
    定义一个类属性init_flag标记是否执行过初始化运作，初始值为False
    在__init__方法中，判断init_flag,如果为False就执行初始化动作
    然后将init_flag设置为True
    这样，再次自动调用__init__方法时，初始化动作就不会被再次执行了
"""


class MusicPlayer(object):
    # 记录第一个被创建对象的引用
    instance = None

    # 记录是否执行过初始化动作
    init_flag=False

    def __new__(cls, *args, **kwargs):
        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2. 调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3. 返回类属性保存的对象引用
        return cls.instance

    def __init__(self,a):
        # 1. 判断是否执行过初始化动作
        if self.init_flag:
            return

        # 2. 如果没有执行过，在执行性初始化动作
        print("初始化播放器")

        # 3. 修改类属性的标记
        self.init_flag=True

        self.a=a

# 创建多个对象
player1 = MusicPlayer(10)
print(player1)
print(player1.a)

player2 = MusicPlayer(20)
print(player2)
print(player2.a)