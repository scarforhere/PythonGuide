# Programmed by Scar
'''
Bug的常见类型
    粗心导致的语法错误SyntaxError：
        1.  age = input ( '请输入你的年龄：' )
            if age >= 18:
                print ( '成年人，做事需要负法律责任了)

        2.  while i < 10:
                print ( i )

        3.  for i in range(3)
                uname = input( '请输入用户名：' )
                pwd = input( '请输入密码：' )
                if uname = 'admin' and pwd = 'admin' :
                    print( '登录成功！' )
                    break
                else
                    print( '输入有误' )
            else
                print( '对不起，三次均输入错误' )

    由于知识不熟练导致的错误
        1.索引越界问题IndexError
            lst = [11,22,33,44]
            print( lst[4] )

        2. append()方法使用不熟练
            lst = []
            lst = append( 'A' , 'B' , 'C' )
            print( lst )

    由于被动掉坑产生的异常
        程序代码罗技没有错。只是因为用户错误操作或者一些“例外情况”而导致的程序崩溃

    异常的解决方案：
        可以使用异常处理机制          try：       except：        else：         finally：
        可使用多个except结构         try：       except：        except: (错误类型1，错误类型2)
            捕获异常的顺序按照先子类后父类的顺序，为了避免遗漏可能出现的异常，可以在最后增加BaseException（类型）或Exception（描述）
            else之后语句只有没有异常才会执行
            finally中的return是优先级最高的return
        使用traceback模块打印异常信息

    Python常见的异常类型（异常的第一个单词）
        0.  Exception               通用异常类型（基类）
        1.  ZeroDivisionError       除(或取模)零(所有数据类型)
        2.  IndexError              序列中没有此索引(index)
        3.  KeyError                映射中没有这个键
        4.  NameError               未声明 / 初始化对象(没有属性)
        5.  SyntaxError             Python语法错误
        6.  ValueError              传入无效的参数、
        7.  AttributeError          对象没有此属性
        8.  IOError                 输入输出操作失败
        9.  SystemError             解释器系统错误

    粗心导致错误的自查宝典
        1. 楼末尾的冒号， 如if语句，循环语句，else子句等
        2. 缩进错误，该缩进的没锁进，不能缩进的瞎缩进
        3. 把英文符号写成中文符号， 比如说：冒号，一号，括号等
        4. 字符串拼接的时候，把字符串和数字拼在一起
        5. 没有定义变量，比如说while的循环条件变量
        6. '=='比较运算符和'='赋值运算符的混用
'''
age = input('请输入你的年龄：')
if int(age) >= 18:
    print('成年人，做事需要负法律责任了')

i = 0
while i < 10:
    print(i)
    i += 1
print()

# 使用异常处理机制，try：串except：结构
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
    print('结果为：', result)
except ValueError:
    print('只能输入数字串')
except ZeroDivisionError:
    print('对不起，除数不允许为0')
print()

# 使用异常处理机制，try： except： else：结构
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
except BaseException as e:
    print('出错了！错误原因：', e)
else:
    print('结果为：', result)
print('程序结束')
print()

# 使用异常处理机制，try： except： else： finally:结构
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
except BaseException as e:
    print('出错了！错误原因：', e)
else:
    # 只有没有异常才会执行的代码
    print('结果为：', result)
finally:
    # 无论是否有异常，都会执行的代码
    print('程序结束')
    # finally中的return是优先级最高的return
print()

'''
常见异常类型
'''
# ZeroDivisionError
# print(10/0)

# IndexError
lst = [11, 22, 33, 44]
# print(lst[4])

# KeyError
dic = {'name': '张三', 'age': 20}
# print(dic['gender'])

# NameError
# print(num)

# SyntaxError
# int a=20

# ValueError
# a=int('hallo')


'''
使用traceback模块打印异常信息
'''
import traceback

try:
    print(1 / 0)
except:
    traceback.print_exc()
