# Programmed by Scar
"""
公共方法：
    可以对Python内预设数据类型进行操作
    内设数据类型：lis, dict, str

Python 内置函数
    len(item)   计算容器中元素个数
    del(item)   删除变量                    del由两种方式
    max(item)   返回容器中最大值             如果是字典，只针对key比较
    min(item)   返回容器中最小值             如果是字典，只针对key比较

    注意：比较符合以下规则： "0" < "A' < "a" < "中文字符"

切片
    支持str, tuple, list
"""
lst=[2,45,7,5,3]
str1="asasdasd"
str2="sdfsa23432"
str3="asdasdASDASD123123"
dict1={"a":1,"b":2}

print(len(lst))
print(len(str1))
print(len(dict1))
print()

print(max(lst))
print(max(str1))
print(max(str2))
print(max(str3))
print(max(dict1))
print()

print(min(lst))
print(min(str1))
print(min(str2))
print(min(str3))
print(min(dict1))
print()
