# Programmed by Scar
"""
eval()函数
    将字符串当成有效表达式来求职并反水计算结果

注意： 泵滥用eval函数直接转换input，因为可以直接调用系统层面操作
"""
# 几本书觉计算
Example = eval("1+2")
print(type(Example))
print(Example)
print()

# 字符串重复
Example = eval("'*'*10")
print(type(Example))
print(Example)
print()

# 将字符串转换成列表
Example = eval("[1,2,3,4,5]")
print(type(Example))
print(Example)
print()

# 将字符串转化成字典
Example = eval("{'name':'xiaoming','age':'10'}")
print(type(Example))
print(Example)
print()

# 直接对输入进行加减乘除操作
input_str = input("请输入算数操作：")
print(eval(input_str))
