# Programmed by Scar
"""
对象
    面向对象的三大特征
        封装：提高程序的安全性
                将数据（属性）和行为（方法）包装到类对象中。在方法内部对属性进行操作，在类对象的外部调用方法。
                这样无需关心方法内部的具体实现细节，从而隔离了复杂度
                在Python中没有专门的修饰符用于属性的私有，如果该属性不希望再类对象外部被访问，命名时添加前缀'__'

        继承：提高代码的复用性
                语法格式    class 子类类名 ( 父类1，父类2.... )
                                pass
                如果一个类没有继承任何类，则默认继承object
                Python支持多继承
                定义子类时，必须在其构造函数中调用父类的构造函数

        多态：提高程序的可扩展性和可维护性
                简单的说，多态就是“具有多种形态”，
                它指的是：几百年不知道一个变量所引用的对象到底是什么类型，仍让可以通过这个变量调用方法，
                在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法
            静态语言实现多态的三个必要条件：
                    1. 继承
                    2. 方法重写
                    3. 父类引用指向子类对象
            动态语言的多态崇尚“鸭子类型”，当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子
                在鸭子类型中，不需要关心对象是什么类型，到底是不是鸭子，只关心对象的行为

    方法重写
        如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其（方法体）进行重新编写
        子类重写后的方法中可以通过super().xxx()调用父类中被重写的方法

    object类
        object类时所有类的父类，因此所有类都有object类的属性和方法
        内置函数dir()可以查看指定对象的所有属性
        Object有一个'__str__()'的方法，用于返回一个对于“对象的描述”
        内置函数str()经常用于print()方法，帮助我们产看对象信息，所以我们经常会对'__str__()'进行重写

    特殊方法和特殊属性
        特殊属性
            __dict__            获得类对象或实例对象所绑定的所有属性和方法的字典
            __class__           输出了对象所属的类
            __bases__           C类的父类类型的元素
            __mro__             查看类的层次结构
            __subclasses__()    查看子类的列表

        特殊方法
            __len__()       通过重写__len__()方法，让内置函数len()的参数可以是自定义类型
            __add__()       通过重写__add__()方法，可使用自定义对象具有'+'功能
            __neu__()       用于创建对象
            __init__()      对创建的对象进行初始化
            __del__()       在对象生命周期结束时被调用
            __str__()       直接打印该类定义的对象时显示的字符串

    类的浅拷贝与深拷贝
        变量的复制操作
            只是形成两个变量，实际上还是指向同一个对象
        浅拷贝
            Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，
            因此，元对象与拷贝对象会引用同一个子对象
        深拷贝
            使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
"""

'''
封装：提高程序的安全性
                将数据（属性）和行为（方法）包装到类对象中。在方法内部对属性进行操作，在类对象的外部调用方法。
                这样无需关心方法内部的具体实现细节，从而隔离了复杂度
                在Python中没有专门的修饰符用于属性的私有，如果该属性不希望再类对象外部被访问，命名时添加前缀'__'
'''


# 类的封装
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print('汽车已启动')


car = Car('宝马X5')
car.start()
print(car.brand)
print()


# 类的私有  使用'__'前缀
class Student:
    def __init__(self, name, age):
        self._Student__age = None
        self.name = name
        self.__age = age

    def show(self):
        print(self.name, self.__age)


stu = Student('张三', 20)
stu.show()

try:
    print(stu.name)
    print(stu.__age)  # __age通常在封装类的外侧无法被调用
except BaseException as e:
    print('程序错误')
    print('错误原因：', e)
print()

# 强制访问有'__'前缀的私有属性
print(dir(stu))
print(stu._Student__age)  # 在类的外侧强制访问私有属性
print()

'''
继承：提高代码的复用性 -->相同的代码不需要重复编写
            语法格式    class 子类类名 ( 父类1，父类2.... )
                            def __init__(self, 父类属性入口1,父类属性入口2..., stu_no):
                                super().__init__(父类属性入口1,父类属性入口2...)  
                                self.stu_no = stu_no
            如果一个类没有继承任何类，则默认继承object
            Python支持多继承
            定义子类时，必须在其构造函数中调用父类的构造函数
            
'''


class Person(object):  # 子类Person继承父类object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Students(Person):  # 定义父类Person的子类Students
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)  # 继承父类Person的属性，使用super().__init__()进行定义
        self.stu_no = stu_no  # 定义新的子类属性


class Teacher(Person):  # 定义父类Person的子类Teacher
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)  # 继承父类Person的属性，使用super().__init__()进行定义
        self.teachofyear = teachofyear  # 定义新的子类属性


stu = Students('张三', 20, '1001')
teacher = Teacher('李四', 34, 10)

# 使用在子类中继承的父类实例方法info()
stu.info()
teacher.info()
print()

"""
多继承：
    子类同时具有所有父类的属性和方法
    如果不同父类中存在相同方法名，则使用多继承需要小心
    当存在上述问题下使用MRO--方法搜索顺序，调用__mro__查看方法的搜索顺序
"""


# 多继承
class A(object):
    def test(self):
        print("A---->Test")

    def demo(self):
        print("A---->Demo")


class B(object):
    def test(self):
        print("B---->Test")

    def demo(self):
        print("B---->Demo")


class C(A, B):  # 子类C同时继承父类A与父类B
    pass


c = C()
c.test()
c.demo()
print()

print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print()
'''
方法重写
        如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其（方法体）进行重新编写
        如果子类中重写了父类的方法，则调用子类时只会调用子类的方法
        父类的方法在重写后不受影响
方法扩展
        子类重写后的方法中可以通过super(object,self).xxx()调用父类中被重写的方法 --> 使用后父类的方法不被覆盖 
                                    当前类     使用父类的方法
        可以简写成super().xxx()       
        
在子类的中调用父类的公有方法：
        self.method
子类无法直接调用父类的私有方法，但可以通过父类的公有方法调用父类的私有属性和私有方法
'''


class Students(Person):  # 定义父类Person的子类Students
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)  # 继承父类Person的属性，使用super().__init__()进行定义
        self.stu_no = stu_no  # 定义新的子类属性

    def info(self):  # 在子类Students中对继承自父类Person中实例方法的重写
        super().info()
        print('学号:', self.stu_no)


class Teacher(Person):  # 定义父类Person的子类Teacher
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)  # 继承父类Person的属性，使用super().__init__()进行定义
        self.teachofyear = teachofyear  # 定义新的子类属性

    def info(self):
        super().info()
        print('教龄：', self.teachofyear)


stu = Students('张三', 20, '1001')
teacher = Teacher('李四', 34, 10)

stu.info()
teacher.info()
print()

'''
object类
        object类时所有类的父类，因此所有类都有object类的属性和方法
        内置函数dir()可以查看指定对象的所有属性
        Object有一个'__str__()'的方法，用于返回一个对于“对象的描述”
        内置函数str()经常用于print()方法，帮助我们产看对象信息，所以我们经常会对'__str__()'进行重写
'''


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # 对父类中方法'__str__()'进行重写
        return '我的名字是{0},我今年{1}岁了'.format(self.name, self.age)


stu = Student('张三', 20)
print(dir(stu))
print(stu)
print(type(stu))
print()

'''
多态：提高程序的可扩展性和可维护性
            简单的说，多态就是“具有多种形态”，
            它指的是：几百年不知道一个变量所引用的对象到底是什么类型，仍让可以通过这个变量调用方法，
            在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法
    静态语言实现多态的三个必要条件：
                1. 继承
                2. 方法重写
                3. 父类引用指向子类对象
    动态语言的多态崇尚“鸭子类型”，当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子
        在鸭子类型中，不需要关心对象是什么类型，到底是不是鸭子，只关心对象的行为
    目的：
        当子类重写了父类中的方法，多态自动选择该调用何种方法
'''


class Animal(object):
    def eat(self):
        print('动物会吃东西')


class Dog(Animal):
    def eat(self):
        print('狗吃骨头...')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼...')


class Person:
    def eat(self):
        print('人吃五谷杂粮')


def fun(obj):
    obj.eat()


fun(Cat())
fun(Dog())
fun(Animal())
fun(Person())
print()

'''
特殊方法和特殊属性
    特殊属性
        __dict__            获得类对象或实例对象所绑定的所有属性和方法的字典
        __class__           输出了对象所属的类
        __bases__           C类的父类类型的元素
        __mro__             查看类的层次结构
        __subclasses__()    查看子类的列表
    特殊方法
        __len__()       通过重写__len__()方法，让内置函数len()的参数可以是自定义类型
        __add__()       通过重写__add__()方法，可使用自定义对象具有'+'功能
        __neu__()       用于创建对象
        __init__()      对创建的对象进行初始化
        __del__()       在对象生命周期结束时被调用
        __str__()       直接打印该类定义的对象时显示的字符串
'''
print(dir(object))
print()


class A(object):
    pass


class B(object):
    pass


class C(A, B):  # 子类C同时继承父类A与父类B
    def __init__(self, name, age):
        self.name = name
        self.age = age


class D(A):
    pass


# 特殊属性
x = C('Jacl', 20)
print(x.__dict__)  # 实例对象的属性字典
print(C.__dict__)  # 类对象的属性字典
print(x.__class__)  # <class '__main__.C'> 输出了对象所属的类
print(C.__bases__)  # C类的父类类型的元素
print(C.__mro__)  # 查看类的层次结构
print(A.__subclasses__())  # 查看子类的列表
print()

# 特殊方法
a = 20
b = 100
c = a + b  # 两个整数类型对象的相加操作
print(c)
print(a.__add__(b))


class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):  # 重写实现两个对象可相加性
        return self.name + other.name

    def __len__(self):
        return len(self.name)  # 重写长度测量方法


stu1 = Student('Jack')
stu2 = Student('李四')

print(stu1 + stu2)  # 由于重写了__add__()方法，所以Student类中的对象有可相加性
print(len(stu1))  # 由于重写了__len__()方法，所以可以测量Student类中对象的长度
print()


class Person(object):  # 当创建新的实例对象时先执行__neu__创建新object，再执行__init__将object进行初始化
    def __new__(cls, *args, **kwargs):
        print('__neu__被调用执行了，cls的id为：{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象的id为：{0}'.format(id(obj)))
        return obj

    def __init__(self, name, age):
        print('__init__被调用执行了，self的id为：{0}'.format(id(self)))
        self.name = name
        self.age = age


print('object的类对象的id为：{0}'.format(id(object)))
print('Person的类对象的id为：{0}'.format(id(Person)))

# 创建Person类的实例对象
p1 = Person('张三', 20)  # --> Person 传入 cls
print('p1这个Person类的实例对象的id为：{0}'.format(id(p1)))
print()

'''
类的浅拷贝与深拷贝
        变量的复制操作
            只是形成两个变量，实际上还是指向同一个对象
        浅拷贝
            Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，
            因此，元对象与拷贝对象会引用同一个子对象
        深拷贝
            使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
'''


class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# 变量的赋值
cpu1 = CPU()
cpu2 = cpu1
print(cpu1, id(cpu1))
print(cpu2, id(cpu2))
print()

# 类的浅拷贝
disk = Disk()  # 创建一个硬盘类对象
computer = Computer(cpu1, disk)  # 创建一个计算机的对象

# 浅拷贝    --> 只拷贝地址，不拷贝数据块
import copy

computer2 = copy.copy(computer)  # 浅拷贝只拷贝此对象，不拷贝实例对象内引用的子实例对象
print(computer, computer.cpu, computer.disk)  # 被拷贝实例对象id与拷贝实例对象id不相同，
print(computer2, computer2.cpu, computer2.disk)  # 被拷贝实例对象与拷贝实例对象的子对象id相同
print()

# 深拷贝   --> 地址和数据块一起拷贝
computer3 = copy.deepcopy(computer)  # 深拷贝拷贝此对象，也拷贝实例对象内引用的子实例对象
print(computer, computer.cpu, computer.disk)  # 被拷贝实例对象id与拷贝实例对象id不相同
print(computer3, computer3.cpu, computer3.disk)  # 被拷贝实例对象与拷贝实例对象的子对象id也不相同
