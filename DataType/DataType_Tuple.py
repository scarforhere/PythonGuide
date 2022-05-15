# Programmed by Scar
"""
不可变序列：字符串，元组
    不可变序列没有增、删、改的操作
可变序列：列表、字典
    可变序列可以对序列执行增、删、盖操作，对象地址不发生改变

卫生么将元组设计成不可变序列：
    多任务环境下，同时操作对象时不需要加所，因此在程序中尽量使用不可变序列
    将列表转换为元组，保护数据安全
    函数的返回值使用元组定义

注意事项：   元组中储存的对象时引用
    1. 如果元组中对象本身时不可变对象，则不能再引用其他对象
    2. 如果元组中的对象时可变对象，则可变对象的引用不允许改变，但对象可以改变
            --> 元组内有列表，则不允许把此元素重新定义为其他数组类型，但此列表可以进行增、删、改操作
"""
s: str = 'hallo'
print('s:', s, id(s))
s += ' the World'
print('s:', s, id(s))  # 字符串进行连接之后内存地址发生更改

'''元组的创建方式'''
# 直接使用小括号进行创建
t = ('Python', 'World', 98)
print('t:', t, type(t))

t2 = 'Python', 'World', 98  # 省略小括号写法
print('t2:', t2, type(t2))
print()

# 使用内置函数tuple()
t1 = tuple(('Python', 'World', 98))
print('t1:', t1, type(t1))
print()

# 包含一个元组的元素需要使用逗号和小括号
t3 = ('Python')
print('t3:', t3, type(t3))
t3 = ('Python',)
print('t3:', t3, type(t3))  # 只有一个元素的时候必须加逗号
print()

# 空元组的创建方式
lst1 = []
lst2 = list()
d1 = {}
d2 = dict()
t4 = ()
t5 = tuple()
print("空列表：", lst1, lst2)
print('空字典：', d1, d2)
print('空元组：', t4, t5)
print()

'''
如果元组中的对象时可变对象，则可变对象的引用不允许改变，但对象可以改变
            --> 元组内有列表，则不允许把此元素重新定义为其他数组类型，但此列表可以进行增、删、改操作
'''
t = (10, [20, 30], 9)
print(t)
print(t[0], type(t[0]), id(t[0]))
print(t[1], type(t[1]), id(t[1]))
print(t[2], type(t[2]), id(t[2]))
# 尝试将t[1]修改为100
print(id(100))
# t[1]=100       # 元组元素不允许修改地址
# 由于[20,30]是列表，列表为可变序列，可以在列表地址不变的情况下进行增、删、改操作
t[1].append(100)
print(t, id(t[1]))
t[1].pop(0)
print(t, id(t[1]))
print()

'''
元组的遍历
'''
t = ('Python', 'World', 98)
# 使用索引获取元组中的元素      --> 前提知道元组中的元素数目
print(t[0])
print(t[1])
print(t[2])
print()

# 使用for-in循环遍历元组内元素
for item in t:
    print(item)
print()

# 元组的地址删除
# del(t)
# print(t)

'''
使用enumerate()函数将元组内每个元素前加从0开始的序号
'''
T = ('hallo', 'world', 'python', 'java')
for index, item in enumerate(T):
    print(index, '\t', item)
print(type(enumerate(T)))
print(enumerate(T))
print()

"""
元组的基本操作
"""
t1 = (312, 'asasaas', 312, 312, 1221)
# 对元组内出现的某一元素次数进行计数
print(t1.count(312))
# 返回元组内某一特定元素的索引
print(t1.index('asasaas'))
# 返回元组内元素的数量
print(len(t1))
print()
