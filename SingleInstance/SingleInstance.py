# Programmed by Scar
"""
设计模式
    设计模式是前人工作的总结和提炼，通常，被人们广泛流传的设计模式都是针对某一特定问题的成熟的解决方案
    使用设计模式是为了可重复代码、让代码更容易被他人理解、保证代码可靠性
单例设计模式
    魔都：让类创建的对象，在系统中只有唯一的一个实例
    每次执行类名()返回得分对象，内存地址是相同的
"""


class MusicPlayer(object):
    # 记录第一个被创建对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):
        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2. 调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3. 返回类属性保存的对象引用
        return cls.instance


# 创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
