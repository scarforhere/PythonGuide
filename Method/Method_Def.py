# Programmed by Scar
'''
什么是函数
    函数就是执行特定任务用以完成特定功能的一段代码

为什么需要函数
    复用代码
    隐藏实现细节
    提高可维护性
    提高可读性，便于调试

函数的创建语法
    def 函数名 ( [ 输入阐述 ] )
        """
        注释
        点击函数名前小灯泡
        选择Insert a docutation string stub
        自动产生函数注释格式体
        """
        函数体
        [ return xxx ]

    选择封装好的函数按Ctrl+Q显示注释内容
'''

'''
函数的创建
'''


def calc(a, b):  # a,b称为形式参数，简称形参，形参的位置时函数的定义处
    c = a + b
    return c


result = calc(10, 20)  # 10,20称为实际参数的值， 简称实参，实参的位置时函数的调用处
print(result)
print()

'''
函数的参数传递
    位置实参        
        根据形参对应的位置进行实参传递        
            calc( 10 , 20 )
        def calc(  a , b  )     

    关键字实参
        根据形参名称进行实参传递
            calc( b=10 , a=20 )
        def calc(    a ,   b  )
'''
result = calc(b=10, a=20)  # 10,20称为实际参数的值， 简称实参，实参的位置时函数的调用处
print(result)

'''
在函数的调用过程中，进行参数的传递

实参是通过引用传递数据的
    如果传递参数是不可变对象
        在函数体的修改不会影响实参的值     arg1修改为100，不会影响n1的值
    如果是可变对象
        在函数体的修改会影响到实参的值     arg修改.append(10)，会影响到n2的值
'''


def act(a):
    print(f"实参在函数中的地址为：{id(a)}")


a = 10
print(f"变量的地址为：{id(a)}")
act(a)


def fun(arg1, arg2):
    print('arg1:', arg1)
    print('arg2', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1:', arg1)
    print('arg2', arg2)


n1 = 11
n2 = [22, 33, 44]
print('n1:', n1)
print('n2:', n2)
fun(n1, n2)
print('n1:', n1)
print('n2:', n2)

'''
函数的返回值
    函数返回多个值时，结果为元组

    1. 如果函数没有返回值(函数体执行完毕之后，不需要给调用处提供数据) return可以省略不写
    2. 函数的返回值如果是1个，直接返回原值
    3. 函数的返回值如果是多个，返回的结果为元组
    4. return后的代码不会被执行
    5. 可以同时接收多个返回值
    6. 函数可以返回一个方法名，后期可直接调用方法名

函数的返回值是通过引用进行传递的！
'''


def fun1(num):
    odd = []  # 存奇数
    even = []  # 存偶数
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


# 函数的调用
lst = [10, 29, 34, 23, 44, 53, 55]
print(fun1(lst))
print()


# 函数中没有返回值
def fun2():
    print('hello')
    # return


fun2()


# 函数只有一个返回值
def fun3():
    return 'hello'


result = fun3()
print(result)


# 返回值为多个元素
def fun4():
    return 'hello', 'world'
    # 等价于 return ('hello', 'world')


print(fun4())
print(fun4()[0], '\t\t', fun4()[1])
print()

# 接收多个返回值
str1, str2 = fun4()
print(f"第一个返回值为{str1}")
print(f"第二个返回值为{str2}")
print()


# 函数的返回值是通过引用进行传递的！
def xxx():
    result = 20
    print(f"函数返回值的内存地址为：{id(result)}")
    return result


a = xxx()
print(f"返回值所在变量的地址为：{id(a)}")
print()

# 函数可以返回一个方法名，后期可直接调用方法名
import math


def normal_value(key):
    if key == 'math':
        return math


test = normal_value("math")
print(test.pi)
print()

'''
函数的参数定义
    函数定义默认值参数
        函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参
        -->实参优先级高于形参
        调用带有多个缺省参数的函数时，需要指定参数名，确保解释器知道参数的传递关系！
        注意：  确保带有默认值的缺省参数在参数列表的末尾
               错误定义： def print_info(name,gender=True,title)
    个数可变的位置参数       (只能定义一个)
        定义函数时，可能无法事先确定传递的位置实参的个数时，使用可变的位置参数
        使用'*'定义个数可变的位置形参
        结果为一个元组
    个数可变的关键字形参      (只能定义一个)
        定义函数时，可能无法事先确定传递的关键字实参的个数时，使用可变的关键字形参
        使用'**'定义个数可变的位置形参
        结果为一个字典
    将序列中的每个元素都转换为位置实参
        在函数调用时使用'*'
    将字典中的每个键值对都转化为关键字实参
        在函数调用时使用'**'
    混合定义
        在遵循上述原则的同时可以进行混合定义
            def fun (a,b,*arg1,**arg2)
            def fun (a,b,*,c,d)     -->从'*'之后的所有参数只能采用关键字传递
            def fun (a,b,*,c,d,**arg2)
        注意：可以同时定义个数可变的位置参数和个数可变的关键字参数，但是要求位置参数要在关键字参数之前！！！
    元组和字典的拆包：
        在调用带有多值参数的函数时
            将一个元组变量，直接传递给args，则在元组便两千增加一个*
            将一个字典变量，直接传递给kargs，则在元组便两千增加一个**
    指定参数类型
        def try7(a:int, b:bool, *, c:str, d, **arg2:list):
            pass
'''


#  函数定义默认值参数
def fun5(a, b=10):
    print(a, b)


fun5(100)
fun5(20, 30)

print('Hallo')
print('World')
print('Hallo', end='\t')
print('World')
print()


# 个数可变的位置参数
def fun6(*args):
    print(args)
    print(args[0])


fun6(10)
fun6(10, 30)
fun6(10, 20, 30)


# 个数可变的关键字形参
def fun7(**args):
    print(args)


fun7(a=10, b=20, c=30)
print()


# 将序列中的每个元素都转换为位置实参
def fun8(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


lst = [11, 22, 33]
fun8(*lst)

# 将字典中的每个键值对都转化为关键字实参
dic = {'a': 11, 'b': 22, 'c': 33}
fun8(**dic)
print()


# 混合定义
# def try1 (*arg1,*arg2):
# def try2 (**arg1,arg2):
# def try3 (**arg2,*arg1):
def try4(*arg1, **atg2):
    pass


def try5(a, b, *arg1, **arg2):
    pass


def try6(a, b, *, c, d, **arg2):
    pass


def fun9(a, b, *, c, d):
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


# fun9(10,20,30,40)     # '*'后必须使用关键字传递参数
fun9(10, 20, c=30, d=40)
print()


# 元组和字典的拆包
def demo(*tup, **dic):
    print(tup)
    print(dic)


gl_num = (1, 2, 3)
gl_xiaoming = {"name": "小明", "age": 18}
demo(*gl_num, **gl_xiaoming)
print()


# 指定参数类型
def try7(a: int, b: bool, *, c: str, d, **arg2: list):
    pass


'''
变量的作用域
    程序代码能访问该变量的区域
    根基变量的有效范围可分为
        局部变量
            在函数内定义并使用的变量，只在函数内部有效
            局部变量使用global声明，这个变量就会变成全局变量
        全局变量
            函数体外定义的变量，可作用在函数的内外
        如果全局变量和局部变量的名称相同，会在局部变量下标注虚线
            
不允许在函数内部改变全局变量的引用！！！
(函数内的赋值语句不被执行，全局函数的方法可执行)
    如果使用赋值语句会在函数内部定义一个局部变量
    如果想在函数内部修改全局变量，需要使用关键字global
    定义全局变量时最好以g_或gl_开头
注意：list在函数内部使用"+="实际使用的是extend()方法，所以可以对全局变量进行操作
'''


def fun10(a, b):  # a,b为函数的形参，作用范围也是函数的内部，属于局部变量
    c = a + b  # c为局部变量，因为c实在函数体内定义的变量
    print(c)


# print(a)
# print(c)       a，c超出了定义范围

name = 'Scar'  # name为全局变量，作用与全程序，属于全局变量


def fun11():
    print(name)


fun11()


def fun12():
    global age  # 将age从局部变量转化为全局变量
    age = 20
    print(age)


fun12()
print(age)
print()

# 不允许在函数内部改变全局变量的引用！！！
# 如果使用赋值语句会在函数内部定义一个局部变量
a = 10


def aaa():
    a = 20
    print(f"全局变量在函数内部改变后的值：{a}")
    print(f"全局变量在函数内部改变后的地址：{id(a)}")


aaa()
print(f"全局变量在函数内部改变后的值：{a}")
print(f"全局变量在函数内部改变后的地址：{id(a)}")
print()


# 如果想在函数内部修改全局变量，需要使用关键字global

def bbb():
    global a
    a = 20
    print(f"全局变量在函数内部改变后的值：{a}")
    print(f"全局变量在函数内部改变后的地址：{id(a)}")


bbb()
print(f"全局变量在函数内部改变后的值：{a}")
print(f"全局变量在函数内部改变后的地址：{id(a)}")
print()
'''
递归函数：
    什么叫递归函数
        如果在一个函数的函数体内调用了函数本身，这个函数就成为递归函数
    递归的组成部分
        递归调用与递归终止条件
    递归的调用过程
        每递归调用一次函数，都会在栈内存分配一个栈帧
        每执行完一次函数，都会释放相应的空间
    递归的优缺点
        缺点：占用内存多，效率低下
        有点：思路和代码简单
'''


# 定义函数fac()计算阶乘
def fac(n):
    if n <= 0:
        return 'ValueError'
    elif n == 1:
        return 1
    else:
        return n * fac(n - 1)


print(fac(3))
print()


# 使用函数输出斐波那契数列第n位数字
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(6))

# 输出斐波那契数列前n位数字
for i in range(1, 30):
    print('斐波那契数列第{0:2}位数字为：{1:6}'.format(i, fib(i)))
