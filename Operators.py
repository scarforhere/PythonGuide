# Programmed by Scar
"""
算数运算符   Arithmetic operators
"""
print(1 + 1)  # + :标准算术运算符，加法运算
print(1 - 1)  # _ :标准算术运算符，减法运算
print(1 * 1)  # * :标准算术运算符，乘法运算
print(1 / 2)  # / :标准算术运算符，除法运算
print(11 // 2)  # // :标准算术运算符，整除运算
print(11 % 2)  # % :标准算术运算符，取余运算
print(2 ** 3)  # ** :标准算术算运算符，幂运算

print(9 / 4)  # 2
print(-9 / -4)  # 2

print(9 // -4)  # -3    一正一负整除运算，向下取整
print(-9 // 4)  # -3

print(9 % -4)  # -3    余数=被除数-除数*商 9-(-4)*(3)=-3
print(-9 % 4)  # 3      余数=被除数-除数*商 -9-(4)*(-3)=3
print("\n\n")

"""
赋值运算符   Assignment operators
"""
# 执行顺序：从右到左
i = 3 + 4
print(i)
# 链式赋值
print("链式赋值")
a = b = c = 20
print(a, id(a))  # id():地址
print(b, id(b))
print(c, id(c))
# 参数赋值
print("参数赋值")
a = 20
a += 30  # 相当于a=a+30
print(a)
a -= 30  # 相当于a=a-30
print(a)
a *= 30  # 相当于a=a*30
print(a, type(a))
a /= 30  # 相当于a=a/30
print(a, type(a))
a //= 8  # 相当于a=a//30
print(a, type(a))
a %= 3  # 相当于a=a%30
print(a, type(a))
# 系列解包赋值
a, b, c = 20, 30, 40
print("系列解包赋值：", a, b, c)
# a,b=20,30,40  左右赋值不一致报错
# 交换两个变量的值
a, b = 10, 20
print("交换之前:", a, b)
a, b = b, a
print("交换之后:", a, b)
print("\n\n")

"""
比较运算符   Comparison operators
"""
a, b = 10, 20
print("a>b?", a > b)  # False
print("a<b?", a < b)  # True
print("a>=b?", a >= b)  # False
print("a<=b?", a <= b)  # True
print(a, b)
print("a==b?", a == b)  # False
print(a, b)
print("a!=b?", a != b)  # True
print(a, b)
print("\n\n")
"""
身份运算符   Identity Operators
    =   为赋值运算符           ==  为比较运算符 
    一个变量由三个部分组成：标识(id)，类型，值(value)
    ==  比较值(value)
    is/is not  比较地址(id)     
    
注意：当比较None时，建议使用is进行比较
"""
a = 10
b = 10
print(a == b)  # 说明a与b的值(value)相等
print(a is b)  # 说明a与b的标识(id)相等
print(a is not b)
list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(list1 == list2)  # 说明list1与list2的值(value)相等
print(list1 is list2)  # 说明list1与list2的标识(id)相等
print(list1 is not list2)
print("\n\n")

"""
逻辑运算符   Logical operators
"""
a, b = 1, 2
# and 全为正确才为 True
print(a == 1 and b == 2)  # True
print(a == 1 and b < 2)  # False
print(a != 1 and b == 2)  # False
print(a != 1 and b != 2)  # False
print("\n")
# or 有一个正确就为 True
print(a == 1 or b == 2)  # True
print(a == 1 or b < 2)  # True
print(a != 1 or b == 2)  # True
print(a != 1 or b != 2)  # False
print("\n")
# not 对布尔类型为取反
f1 = True
f2 = False
print(not f1)
print(not f2)
print("\n")
# in 和not in 判断字符是否出现在字符串中  Membership Operators
s = "hallow the world"
print("w" in s)
print("w" not in s)
print("k" in s)
print("k" not in s)
print("\n\n")

"""
位运算符    Bitwise Operators
"""
print(0b100 & 0b1000)  # 0=0000    &：按位与   二进制位全为1输出1，有0输出0
print(0b100 | 0b1000)  # 12=1100   |：按位或   二进制位有1输出1，全不为1输出0
print(0b0010 << 1)  # 左移1位 高位溢出   低位补零
# 左移位相当于乘2
print(0b1000 >> 3)  # 右移3位 高位补零   低位截断
# 右移位相当于除8


"""
多种运算符计算顺序
    0. ()               #括号优先级最高

    1. **
    2. *,/,//,%
    3. +_               #先算乘除，再算加减，幂运算最先

    4. <<,>>
    5. &
    6. |                #位运算，先移位，后与或

    7. >,,,>=,<=,==,!=  #比较运算 Ture False

    8. and
    9. or               #布尔运算

    10. =               #赋值运算

    #有括号先计算括号内，括号内按顺序进行计算
"""