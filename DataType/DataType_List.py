# Programmed by Scar
"""
列表=结构体
索引  -7      -6      -5      -4      -3      -2      -1
数据  "as"    "ha"    123     90.3    4545    "sad"   4
索引  0       1       2       3       4       5       6

列表特点：
    1. 列表元素按顺序有序排序
    2. 索引映射唯一一个数据
    3. 列表可以存储重复数据
    4. 任意数据类型混存
    5. 根据需要动态分配和回收内存

列表是可变序列
    通过方法对可变序列进行操作不会更改列表所在引用内存的地址
    通过赋值对可变序列进行操作会更改列表所在引用内存的地址
"""
a = 10  # 变量存储的是一个对象的引用

# 创建列表的第一种方式，使用[]
lst = ["hallo", "the", 98, "hallo"]

# 创建列表的第二种方式，使用内置函数
lst2 = list(["hallo", "the", 98])

print(id(lst))
print(type(lst))
print(lst)
print()

print(type(lst[0]))
print(lst[0], lst[-1])
print()

# 空列表的创建方式
lst = []
print(lst)
lst = list()
print(lst)
print()

"""
获取列表中指定元素的索引，index()
    1. 如查列表中N个相同的元素，只返回相同元素的第一个元素的索引
    2. 如果查询的元素在列表中不存在，则会抛出ValueError
    3. 还可以在指定的start和stop之间进行查找
"""
lst = ["hallo", "the", 98, "hallo"]
print(lst.index("hallo"))  # 如查列表中N个相同的元素，只返回相同元素的第一个元素的索引
# print(lst.index("python")) # 如果查询的元素在列表中不存在，则会抛出ValueErro
# print(lst.index("hallo",1,3))      # 如果查询的元素在列表中不存在，则会抛出ValueErro
print(lst.index("hallo", 1, 4))  # 还可以在指定的start和stop之间进行查找
print()

"""
获取列表中的单个元素
    1. 正向索引从0到N-1       lst[0]
    2. 逆向索引从-N到-1       lst[-N]
    3. 指定索引不存在，抛出IndexError
"""
# 希望获取索引为2的元素
print(lst[2])
print(lst[-1])
# print(lst[10])     # 指定索引不存在，抛出IndexError
print()

"""
获取列表中多个元素使用切片
语法格式：
    列表名[start:stop:step]
"""
lst3 = [10, 20, 30, 40, 50, 60, 70, 80]
# start=1   stop=6  step=1
print(lst3[1:6:1])
print("源列表：", id(lst3))
lst4 = lst3[1:6:1]
print("切片片段：", id(lst4))  # 切片片段为新的列表
print(lst3[1:6])  # 默认步长为1
print(lst3[1:6:])  # 默认步长为1
print(lst3[1:6:2])  # 步长为2
print(lst3[:6:2])  # 默认start为0
print(lst3[1::2])  # 默认start为0
print()

# 切片步长为负数
print(lst3)
print(lst3[::-1])
print(lst3[6::-2])
print(lst3[6:0:-2])  # 0不被包括在内

"""
判断元素是否在列表中存在
"""
lst = [10, 20, "python", "Hallo"]
print(10 in lst)
print(100 in lst)
print(10 not in lst)
print(100 not in lst)
print()

for item in lst:  # 列表的遍历输出
    print(item)
print()

"""
列表元素的增删改操作
    增加元素：
        append()    在列表末尾添加一个元素
        extend()    在列表的末尾至少添加一个元素
        insert()    在列表的任意位置添加一个元素
        切片         在列表的任意位置添加只要一个元素
"""
# append()
lst = [10, 20, 30]
print("添加元素之前", lst, id(lst))
lst.append(100)
print("添加元素之后", lst, id(lst))  # 增加元素之后列表的地址不变
lst2 = ["hallo", "the", "World"]
lst.append(lst2)  # 将lst2作为一个元素添加到列表末尾
print(lst)
print()

# extend()
print("添加元素之前", lst, id(lst))
lst.extend(lst2)  # 向列表的末尾添加多个元素
print("添加元素之后", lst, id(lst))
print()

# insert()
print("添加元素之前", lst, id(lst))
lst.insert(4, "Insert")  # 在列表位置为4的地址添加新元素，剩余元素顺位后移
print("添加元素之后", lst, id(lst))
print()

# 切片
print("添加元素之前", lst, id(lst))
lst3 = [True, False, "hallo"]
lst[1:] = lst3  # 切片添加相当于将指定元素之后包括指定元素在内的所有元素进行增加操作
print("添加元素之后", lst, id(lst))

"""
列表元素的增删改操作
    删除元素：
        remove()        一次删除一个元素
                        重复元素只删除第一个
                        元素不存在抛出ValueError
        pop()           删除一个指定索引位置的元素
                        指定索引不存在抛出IndexError
                        不指定索引，删除列表中最后一个元素
        切片             一次至少删除一个元素
        clear()         清空列表
        del             删除列表
                        删除指定索引元素(内存中删除，释放内存空间)
"""
# remove()
lst = [10, 20, 30, 40, 50, 60, 30]
lst.remove(30)  # remove() 一次只移除重元素中的第一个元素
print(lst)
# lst.remove(100)                # remove() 不存在的元素时，抛出ValueError
print()

# pop()

print(lst.pop(1))  # pop() 删除指定索引的元素
print(lst)
# lst.pop(5)                       # pop() 不存在的元素时，IndexError
lst.pop()  # pop() 不指定索引时，删除列表最后一个元素
print(lst)
print()

# 切片
new_lst = lst[1:3]
print("源列表：", lst)  # 产生新的列表！
print("切片后列表：", new_lst)
lst[1:3] = []  # 不产生新列表
print(lst)

# clear()
lst.clear()  # 清除所有元素
print(lst)

# del
# del lst                            # del 直接删除列表
# print(lst)
lst = [10, 20, 30, 40, 50, 60, 30]
del lst[0]
print(lst)
print()

"""
列表元素的增删改操作
    改变元素：
        指定索引的元素并赋予一个新值
        为指定的切片赋予一个新值
"""
lst = [10, 20, 30, 40]
# 一次修改一个值
lst[2] = 100
print(lst)
lst[1:3] = [200, 300, 400, 500]
print(lst)

"""
列表的排序操作
    1. 调用sort()，列序中所有元素默认按照从小到大顺序进行排序，可以指定reverse = True 进行降序排序，原列表不发生改变
    2. 调用内置函数sorted()，可以指定reverse = True 进行降序排序，原列表不发生改变
    3. .reverse()反转列表
"""
lst = [20, 40, 10, 90, 54]
print("排序前的列表：", lst, id(lst))
# 开始排序，调用列表对象sort()方法，升序排序
lst.sort()
print("排序后的列表：", lst, id(lst))
# 通过指定关键字参数，将列表中的元素进行降序排序
lst.sort(reverse=True)  # reverse=True降序
print(lst)
lst.sort(reverse=False)  # reverse=False升序
print(lst)
lst = [20, 40, 10, 90, 54]
lst.reverse()  # reverse=False升序
print(lst)
print()

# sortet() 排序产生新的列表对象
lst = [20, 40, 10, 90, 54]
print("原列表：", lst)
new_lst = sorted(lst)  # reverse=True降序
print(new_lst)
new_lst = sorted(lst, reverse=True)
print(new_lst)
print()

"""
列表统计
    len(list)   计算列表的长度
    list.count(数据) 统计数据在列表中出现的次数
"""
lst=[1,2,3,4,5,6,7,2,34,45,6,4,3]
print(len(lst))
print(lst.count(3))
print()

"""
列表生成式
    语法格式：
        [i for i in range(1,10)]
"""
lst = [i * i for i in range(1, 10)]
print(lst)

lst = [i * 2 for i in range(1, 6)]
print(lst)

lst = [i for i in range(2, 11, 2)]
print(lst)
print()

lst=[[i for i in range(4)]for j in range(8)]
print(lst)
print()

lst1=[1,2,3,4]
lst2=[5,6,7,8]
lst3=["a","b","c","d"]
lst=[lst1,lst2,lst3]
print(lst)
print(lst[0][3])
print()

"""
通过列表分解字符串，并获取字符数目
"""
str = 'Hallo the World'
lst = list(str)
print(lst)
i = 0
for item in lst:
    i += 1
print(i)
print()

'''
使用enumerate()函数将元组内每个元素前加从0开始的序号
'''
lst3=["a","b","c","d"]
for index,item in enumerate(lst3):
    print(index,'\t',item)
print(type(enumerate(lst3)))
print(enumerate(lst3))
print()
