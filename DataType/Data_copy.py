# Programmed by Scar
"""
浅拷贝
    Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，
    因此，元对象与拷贝对象会引用同一个子对象
深拷贝
    使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
"""
import copy

a = [1, 2, 3]
b = a
print(f"a={a}\nb={b}")
print("*" * 40)
a.append(4)
print(f"a={a}\nb={b}")
print("*" * 40)
print()
# a=[1, 2, 3, 4]
# b=[1, 2, 3, 4]
# 由于a=b是指针相同，所以a指针指向的内存块内容改变时b也发生变化

a = [1, 2, 3]
b = copy.copy(a)
print(f"a={a}\nb={b}")
print("*" * 40)
a.append(4)
print(f"a={a}\nb={b}")
print("*" * 40)
print()
# a=[1, 2, 3, 4]
# b=[1, 2, 3]
# 使用浅拷贝时创建的列表与原列表地址不同，只拷贝内存块中内容

a = [[1, 2, 3], ["a", "b", "c"]]
b = copy.copy(a)
print(f"a={a}\nb={b}")
print("*" * 40)
a[1].append("d")
print(f"a={a}\nb={b}")
print("*" * 40)
print()
# a=[[1, 2, 3], ['a', 'b', 'c', 'd']]
# b=[[1, 2, 3], ['a', 'b', 'c', 'd']]
# 浅拷贝只对第一层指针指向内存块的内容进行拷贝
# 第一层指针指向内存块中保存的第二层指针指向的内存块中保存的内容并没有开辟新的空间进行保存

a = [[1, 2, 3], ["a", "b", "c"]]
b = copy.deepcopy(a)
print(f"a={a}\nb={b}")
print("*" * 40)
a[1].append("d")
print(f"a={a}\nb={b}")
print("*" * 40)
print()
# 深拷贝对所有层级的内容开辟新内存空间进行拷贝
# 原列表中所有内容不随新列表改变发生改变
