# Programmed by Scar
'''
模块
    模块测英文为Modules
    函数与模块的关系
        一个模块中可以包含多个函数
    在Python中一个扩展名为.py的文件就是一个模块
    使用模块的好处
        方便其他程序和脚本的导入和使用
        避免函数名和变量名冲突
        提高代码的可维护性
        提高代码的可复用性

创建模块
    新建一个.py的文件，名称尽量不要与Python自带的标准模块名称相同

注意：模块名应符合大驼峰命名法

导入模块
    import 模块名称 [as别名]
    from 模块名称 import 函数、变量、类

以主程序形式运行
    在每个模块的定义中都包括一个击落模块名称的变量__name__,
    程序可以检查该变量，以确定他们在那个模块中执行。
    如果一个模块不是被导入到其他程序中执行，那么它可能在解释器顶级模块中执行。
    顶级模块的__name__变量的值为__main__

Python中的包
    包时一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下
    作用：
        代码规范
        必满模块名称冲突
    包与目录的区别
        包含__init__.py文件的目录称为包
        目录里通常不包含__init__.py文件
    包的导入
        import 包名.模块名

Python中常用内置模块
    sys                 与Python解释器及其环境操作相关的标准库
    time                提供与时间相关的各种函数的标准库
    os                  提高了访问操作系统服务功能的标准库
    calendar            提供与日期相关的各种函数的标准库
    urllib              用于读取来自网上（服务器）的数据标准库
    json                用于使用JSON序列化和反序列化对象
    re                  用于在字符串中执行正则表达式匹配和替换
    math                提供标准算数函数的标准库
    decimal             用于进行精度控制运算精度、有效位数和四舍五入操作的十进制运算
    logging             提供了灵活的记录时间、错误、警告和调试信息等日志信息的功能

第三方模块的安装及使用
    第三方模块的安装
        pip install 模块名
    第三方模块的使用
        import 模块名
'''


def fun():
    pass


def fun2():
    pass


class Student:
    native_place = '吉林'

    def eat(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def cm(cls):
        pass

    @staticmethod
    def sm():
        pass


a = 10
b = 20
print(a + b)
print()
'''
导入模块
    import 模块名称 [as别名]
    from 模块名称 import 函数、变量、类
    from 模块名 import *    -->从模块中导入所有工具
'''
# 导入模块中所有模块
import math

print(id(math))
print(type(math))
print(math)
print(dir(math))
print(math.pi)  # 圆周率
print(math.pow(2, 3), type(math.pow(2, 3)))  # 计算2的3次方
print(math.ceil(9.001))  # 想上取整
print(math.ceil(9.999))  # 向下取整
print()

# 从模块单独导入函数
from math import pi
from math import pow

print(pi)
print(pow(2, 3))
print()

# 如何导入自定义模块
# 如果报错，将待引用模块所属文件夹转换为Source文件夹
from Modules_Basic import Calc

print(Calc.add(10, 20))
print(Calc.div(10, 2))

from Modules_Basic.Calc import add

print(add(10, 2))
print()

'''
以主程序形式运行
    在每个模块的定义中都包括一个击落模块名称的变量__name__,
    程序可以检查该变量，以确定他们在那个模块中执行。
    如果一个模块不是被导入到其他程序中执行，那么它可能在解释器顶级模块中执行。
    顶级模块的__name__变量的值为__main__
'''
from Modules_Basic import Calc2

print(Calc2.add(50, 60))
# 由于引用所有函数和语句所以需要在被引用程序中判断是否是顶级模块
print()

'''
Python中的包
    包时一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下
    作用：
        代码规范
        必满模块名称冲突
    包与目录的区别
        包含__init__.py文件的目录称为包
        目录里通常不包含__init__.py文件
    包的导入
        import 包名.模块名
'''
from package_demo.Module_A import a

# print(package_demo.Module_A.a)
print(a)

# 使用import导入时，只能导入包名和模块名

# 使用from...import可以导入包，模块或函数和变量

print()

'''
Python中常用内置模块
    sys                 与Python解释器及其环境操作相关的标准库
    time                提供与时间相关的各种函数的标准库
    os                  提高了访问操作系统服务功能的标准库
    calendar            提供与日期相关的各种函数的标准库
    urllib              用于读取来自网上（服务器）的数据标准库
    json                用于使用JSON序列化和反序列化对象
    re                  用于在字符串中执行正则表达式匹配和替换
    math                提供标准算数函数的标准库
    decimal             用于进行精度控制运算精度、有效位数和四舍五入操作的十进制运算
    logging             提供了灵活的记录时间、错误、警告和调试信息等日志信息的功能
    random              给出一个随机数
'''
import sys

print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))
print()

import time

print(time.time())
print(time.localtime(time.time()))
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print()

import urllib.request

print(urllib.request.urlopen('http://www.baidu.com').read())
print()

import math

print(math.pi)
print()

import random

print(random.randint(1000, 5000))  # 取[1000,2000]之间任意整数
print(type(random.randint(10, 20)))
print()

'''
第三方模块的安装及使用
    第三方模块的安装
        pip install 模块名
    第三方模块的使用
        import 模块名
'''
import schedule


def job():
    print('哈哈----------- ')


schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
