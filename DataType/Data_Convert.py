# Programmed by Scar
# 转换为str类型
name = "Scar"
age = 20
print(type(name), type(age))
# print("my name is:"+name+".my age is:"+age)    #+为数据连接符。 报错原因：数据类型不同
print("my name is:" + name + ".my age is:" + str(age))  # str():将int数据类型转换为str
a = 10
b = 109.9
c = False
print(type(a), type(b), type(c))
print(str(a), type(a), str(b), type(b), str(c), type(c))
print("\n\n")

# 转换为int类型
s1 = "128"
f1 = 98.42
s2 = "198.4"
b1 = False
s3 = "hallo"
print(type(s1), type(f1), type(s2), type(b1), type(s3))
print(int(s1), type(int(s1)))
print(int(f1), type(int(f1)))  # 舍去小数，保留整数
# print(int(s2), type(int(s2)))    #字符串转换必须为整数，否则报错
print(int(b1), type(int(b1)))
# print(int(s3), type(int(s3)))    #字符串转换必须为整数，否则报错
print("\n\n")

# 转换为flaot类型
s1 = "128.98"
s2 = "76"
b1 = False
s3 = "hallo"
i = 98
print(type(s1), type(s2), type(b1), type(s3), type(i))
print(float(s1), type(float(s1)))
print(float(s2), type(float(s2)))
# print(float(s3),type(float(s3)))   #字符串必须为数字，否则报错
print(float(b1), type(float(b1)))
print(float(i), type(float(i)))
