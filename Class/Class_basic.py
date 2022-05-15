# Programmed by Scar
"""
数据类型：
    不同的数据类型属于不同的类
    使用内置函数type()查看数据类型

对象
    100，99，520都是int类之下包含的相似的不同隔离，这个隔离专业术语称为实例或对象
相比较于函数，面向对象时更大的封装，根据职责在一个对象中封装多个方法
    1. 在完成某一个需求前，首先确定职责
    2. 根据职责确定不同的对象，在对象内部封装不同的方法
    3. 最后完成代码，顺序地让不同对象调用不同地方法
特点：
    1. 注重对象华人职责，不同地对象承担不同的职责
    2. 更加适合应对负责的需求变化，是专门应对复杂项目开发，提供固定的套路
    3.需要在面向过程的基础上，学习面向对象的语法


类和对象是面向对象编程的两个核心概念

类时对一群具有相同特征和行为事物的一个同城，是抽象的，不能直接使用
    特征被称为属性
    行为被称为方法

对象时由类创建出来的一个具体存在，可以直接使用
    由哪一个类类创建出来的对象，就拥有哪一个类中定义的属性和方法

创建类的语法
    class Student :
        pass
    注意：对类取名时需要配满足大驼峰命名法

创建对象的语法
    stu1 = Student(index1, index2, ...)

类的组成：
    1. 类的属性
    2. 实例方法
    3. 静态方法
    4. 类方法
"""


# 创建类
class Student:  # Student为类名，可由一个或多个单词组成，要求每个单词首字母大写，其余字母小写

    # 类属性
    native_place = '吉林'  # 直接卸载类里面的变量，称为类属性

    # 初始化方法
    def __init__(self, name, age):
        self.name = name  # self.namne 称为实体属性，进行了一个赋值操作
        self.age = age

    # 实例方法           --> 在类之外定义的称为函数，在类之内定义的称为方法
    def eat(self):
        print(self.name + '在吃饭...')

    # 静态方法
    @staticmethod
    def method():
        print('我使用了statticmethod进行修饰，所以我是静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('我使用了classmethod进行修饰，所以我是类方法')


# Python中一切皆为对象
print(id(Student))
print(type(Student))
print(Student)
print()

'''
对象的创建又称为类的实例化
    语法：
        实例名 = 类名()

    意义：有了实例，就可以调用类中的内容
'''
# 创建Student类的对象
stul = Student('张三', 20)
print(id(stul))
print(type(stul))
print(stul)
print()

# 调用类的方法和调用对象的方法
stul.eat()  # 对象.方法名()
Student.eat(stul)  # 类。方法名()     定义类的方法是传入参数为self，所以需要在使用是传入自身
print(stul.name, stul.age)
print()

'''
类属性：
    类中方法外的变量称为类属性，被该类的所有对象所共享
类方法：
    使用@classmethod修饰的方法，使用用类名直接访问的方法
静态方法：
    使用@staticmethod修饰的方法，使用用类名直接访问的方法
'''
# 类属性的使用方式
print(Student.native_place)  # 吉林
stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(stu1.native_place)  # 吉林
print(stu2.native_place)  # 吉林

Student.native_place = '天津'
print(stu1.native_place)  # 天津
print(stu2.native_place)  # 天津

stu1.native_place = '山东'
print(Student.native_place)  # 天津
print(stu1.native_place)  # 山东
print(stu2.native_place)  # 天津
print()


# 定义属性时，如果不知道设置什么初始值，可以设置为None
# None关键字表示什么都没有
# 表示一个空对象，没有方法和属性，是一个特殊的常量
# 可以将None赋值给任何一个变量
class Demo:
    def __init__(self, index):
        self.poroerty01 = index
        self.property02 = None

sss=Demo(True)
print(f"该对象的属性01为：{sss.poroerty01}\n")
# print(f"该对象的属性02为：{sss.poroerty02}\n")            -->由与默认属性为None所以不存在
print()

# 类方法的调用
Student.cm()
stu1.cm()
stu2.cm()
print()

# 静态方法的调用
Student.method()
stu1.method()
stu2.method()

'''
动态绑定属性和方法
    Python是动态语言，在创建对象之后，可以动态地绑定属性和方法
'''
print(id(Student))
print(id(stu1))
print(id(stu2))

# 将stu2动态绑定性别属性
stu2.gender = '女'
print(stul.name, stu1.age)
print(stu2.name, stu2.age, stu2.gender)
try:
    print(stu1.name, stu1.age, stu1.gender)
except BaseException as e:
    print('输出失败\n', '错误原因：', end=' ')
    print(e)
print()


# 将show()函数动态绑定为stu1的方法
def show():
    print('定义在类之外的，称为函数')


stu1.show = show
stu1.show()
try:
    stu2.show()
except BaseException as e:
    print('输出失败\n', '错误原因：', end=' ')
    print(e)
print()
