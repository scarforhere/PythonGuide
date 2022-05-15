# Programmed by Scar
"""
可以将一个类的属性设置为另一个类
当类的属性在初始化时无法确定，可以设置成None，此时此属性不存在，无法调用
"""


class Gun:
    def __init__(self, model):
        # 1. 枪的型号
        self.model = model

        # 2. 子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 1. 判断子弹数量
        if self.bullet_count <= 0:
            print(f"[{self.model}]没有子弹了")
            return

            # 2. 发射子弹，-1
        self.bullet_count -= 1

        # 3. 提示发射信息
        print(f"[{self.model}]突突突...[{self.bullet_count}]")


class Soldier:
    def __init__(self, name):
        # 1. 姓名
        self.name = name

        # 2. 枪 - 新兵没枪
        self.gun = None

    def fire(self):
        # 1. 判断士兵是否有枪
        if self.gun is None:
            print(f"[{self.name}]还没有枪...")
            return

        # 2. 高喊口号
        print(f"冲啊...[{self.name}]")

        # 3. 让枪装填子弹
        self.gun.add_bullet(30)

        # 4. 让枪发射子弹
        self.gun.shoot()


# 主程序1：

# 1. 创建对象
ak47 = Gun("AK47")

# 2. 创建许三多
xusanduo = Soldier("许三多")
xusanduo.gun = ak47
xusanduo.fire()
