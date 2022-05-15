# Programmed by Scar
"""
集合是Python提供的内置数据结构
与列表和字典一样都属于可变类型的序列
集合是没有value的字典

hash(dataA)         hash(dataE)         hash(dataB)             hash(dataD)
   dataA               dataE               dataB                   dataD
"""

"""
集合的创建
"""
# 直接使用{}
s = {2, 3, 4, 5, 5, 6, 7, 7}
print(s, type(s))  # 集合中的元素不允许重复，重复元素会被合并
# 通过set()
s1 = set(range(6))
print(s1)
s2 = set([1, 2, 4, 5, 5, 5, 6, 6])
print(s2, type(s2))
s3 = set((1, 2, 4, 5, 65))  # 集合中的元素是无序的
print(s3, type(s3))
s4 = set('Python')  # 集合中的元素是无序的
print(s4, type(s4))
s5 = set({12, 4, 34, 55, 66, 44, 4})
print(s5)

# 定义空集合
s6 = {}  # dict字典类型空姐和
print(type(s6))
s7 = set()  # 定义空集合只能使用set()
print(s7, type(s7))
print()

"""
结合元素的判断操作
    in          no in
"""
s = {10, 20, 30, 405, 60}
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)
print()

"""
集合元素的新增操作
    add()       一次添加一个元素
    update()    一次至少添加一个元素
"""
# add()一次添加一个元素
s.add(80)
print(s)

# update()一次添加多个元素，可以添加集合、元组和列表
s.update([200, 400, 300])
print(s)
s.update({100, 99, 8})
print(s)
s.update((78, 64, 36))
print(s)
print()

"""
集合元素的删除操作
    remove()    一次删除一个指定元素，如果指定元素不存在则抛出KeyError、
    discard()   一次删除一个指定元素，如果指定元素不存在不会抛出异常
    pop()       一次只删除一个任意元素
    clear()     清空集合
"""
# remove()移除指定元素
s.remove(100)
print(s)
# s.remove(500)     # 指定移除元素不存在时抛出KeyError
# print(s)
print()

# discard()移除指定元素       -->比remove()好
s.discard(500)  # 指定元素不存在时不会抛出异常
print(s)
s.discard(200)
print(s)
print()

# pop()随机删除一个元素
s.pop()
# s.pop(400)     # 不能指定参数，一旦指定参数抛出 set.pop() takes no arguments 异常
print(s)
print()

# clear()
s.clear()
print(s)  # 清空集合
print()

# del
# del s          # 擦除集合的地址，完全删除集合
# print(s)


'''
判断集合间的关系
    1. 判断两个集合是否相等
            可以使用运算符==或!=进行判断
    2. 一个集合是否是另一个集合的子集
            可以调用issubset进行判断
            B是A的子集
    3. 一个集合是否是另一个集合的超集
            可以调用方法issuperset进行判断
            A是B的超集
    4. 判断两个集合是否有交际
            可以调用方法isdisjoint进行判断
'''
# 判断集合是否相等
s1 = {10, 20, 30, 40}
s2 = {30, 40, 20, 10}
print(s1 == s2)  # True      元素相同就相等
print(s1 != s2)  # False

# 判断是否为子集
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}
print(s2.issubset(s1))  # s2是否是s1的子集
print(s3.issubset(s1))  # s3是否是s1的子集
print()

# 判断是否是超集
print(s1.issuperset(s2))  # s1是否是s2的子集
print(s1.issuperset(s3))  # s1是否是s3的子集
print()

# 判断是都含有交集
print(s2.isdisjoint(s3))  # s2和s3是否没有交集
print(not s2.isdisjoint(s3))  # s2和s3是否有交集
s4 = {100, 200, 300}
print(s2.isdisjoint(s4))  # s2和s4是否没有交集
print(not s2.isdisjoint(s4))  # s2和s4是否有交集
print()

'''
集合的数学操作
    交集      intersection
    并集      union
    差集      difference
    对称差集   symmetric_difference
'''
# 交集操作
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}
print(s1.intersection(s2))
print(s1 & s2)  # intersection() 与 & 等价
print()

# 并集操作
print(s1.union(s2))
print(s1 | s2)  # union() 与 | 等价
print()

# 差集操作
print(s1.difference(s2))  # s1集合减去s2集合中重复内容
print(s1 - s2)  # difference() 与 - 等价
print(s2.difference(s1))  # s2集合减去s1集合中重复内容
print(s2 - s1)
print()

# 对称差集
print(s1.symmetric_difference(s2))  # 集合s1与s2中不重复的内容
print()

'''
集合生成式
'''
# 列表生成式
lst = [i * i for i in range(6)]
print(lst)

# 字典生成式
item = ['Appel', 'Pizza', 'Icecream']
price = [4, 3, 2]
d1 = {item: price for item, price in zip(item, price)}
print(d1)

# 集合的生成式
s1 = {i * i for i in range(6)}
print(s1)
