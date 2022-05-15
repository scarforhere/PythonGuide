# Programmed by Scar
"""
使用类名()创建对象时，Python的解释器首先会调用__new__方法为对象分配空间
__new__时一个由object基类提供的内置静态方法1，主要作用有两个：
    1. 在内存中为对象分配空间
    2. 返回对象的引用
Python的解释器获得对象的引用后，将引用作为第一个参数，传递给__init__方法

重写__new__方法的代码非常固定！
    重写__new__方法一定要return super().__new__(cls)
    否则Python的解释器得不到分配空间的对象的引用，就不会调用对象的初始话方法

注意：__new__是一个静态方法，在调用时需要主动传递cls参数！
"""


class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        # 1. 创建对象时，new方法会被自动调用
        print("创建对象，分配空间")

        # 2. 为对象分配空间
        instance = super().__new__(cls)

        # 3. 返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化")


# 创建播放器对象
player = MusicPlayer()

print(player)
