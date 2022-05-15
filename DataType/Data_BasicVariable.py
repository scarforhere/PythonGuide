# Programmed by Scar
"""
标识符只可以由字母、数字、下划线组成
    不能以数字开头
    不能与关键字重名    关键字查看004_Keyword.py
"""
# integer 整数类型：正数、负数、零
n1 = 90
n2 = -76
n3 = 0
print(n1, "\t", type(n1))
print(n2, "\t", type(n2))
print(n3, "\t", type(n3))

print("十进制", 118)  # 十进制
print("二进制", 0b1010111)  # 二进制    0b
print("八进制", 0o176)  # 八进制    0o
print("十六进制", 0x1EAF)  # 十六进制   0x
print("\n\n")

# float 浮点类型
a = 3.14159
print("a:", a, "\t", type(a))
a1 = 1.1
a2 = 2.2
a3 = 2.1
print(a1 + a2)  # 浮点数存储计算不精确
print(a1 + a3)
from decimal import Decimal  # 导入Decimal模块进行精确计算

print(Decimal(a1) + Decimal(a2))
print(Decimal(1.1) + Decimal(2.2))
print(Decimal("1.1") + Decimal("2.2"))
print("\n\n")

# bool 布尔类型：true、false
f1 = True
f2: bool = False
print("f1:", f1, type(f1))
print("f2:", f2, type(f2))
print(f1 + 1)  # 2 True标识为1
print(f2 + 1)  # 1  False表示为0
print("\n\n")

# string 字符串：可使用'',"",'''''',""""""定义
str1 = 'Hallo the World'
str2 = "Hallo the World"
str3 = """Hallo the World
        What a nice day"""
str4 = '''Hallo the World
        What a nice day'''
print("str1:", str1, "\t", type(str1))
print("str2", str2)
print("str3", str3)
print("str4", str4)
