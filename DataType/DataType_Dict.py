# Programmed by Scar
"""
字典=键值对 {Key : Value }
              item[0]              item[1]             item[2]             item[3]             item[4]
keys:        hash(key4)          hash(key2)          hash(key1)          hash(key3)          hash(key5)
values:        value4              value2              value1              value3              value1

dict.keys()     取出所有keys的列表
dict.values()   取出所有values的列表
dict.item()     取出所有键值对(key,value)列表

key被经过hash函数计算
    -->key是不可变序列     （整数序列，字符串是不可变序列）
    -->查找效率高

hash算法：
    通过计算给出不可变序列的唯一特征值

Value可以定义为可变序列或不可变序列

字典的特点：
    1. 字典中的所有元素都是一个key-value对，key不允许重复，value可以重复
    2. 字典中的元素是无序的
    3. 字典中的key必须是不可变对象（不能是list）
    4. 字典可以根据需要动态伸缩
    5. 字典会浪费较大的内存，是一种使用空间转换时间的数据结构

建议：
    定义字典时，每一个键值对占单独一行
"""

"""
字典的创建方式
    1. 使用花括号创建          {"German":"Berlin","China","Beijing"}
    2. 使用内置函数dict()      dict(name="Jack",age=20)
"""
scores = {"张三": 100, "李四": 98, "王五": 45}
print(scores)
print(type(scores))
print()

student = dict(name='Jack', age=20)
print(student)
print()

d = {}  # 创建空字典
print(d)
d = dict()
print(d)
print()

"""
从字典中获取数据
    1. []       scroes['张三']
            不存在指定的key时，抛出KeyError异常
    2. get()    scores.get('张三‘）
            不存在指定的key时，返回None
            可通过参数设置默认的Value，以便指定的key不存在时返回
    3. setdefault   scores.setdefault("赵四",20)
            或取某个key的value，如果key不存在于字典中，将会添加key并将value设为默认值
"""
scores = {"张三": 100, "李四": 98, "王五": 45}
# 使用[]获取元素
print(scores['张三'])
# print(scores['陈六'])            # 不存在指定的key时，抛出KeyError异常

# 使用get()获取元素
print(scores.get('张三'))
print(scores.get('陈六'))  # 不存在指定的key时，返回None
print(scores.get('麻七', 99))  # 99是在查找'麻七'所对的value不存在时，提供的默认值
print(scores.get('麻七', '不存在本字典中'))
print()

# 使用setdefault()或取value或添加默认值
scores.setdefault("赵四", 20)
print(scores["赵四"])
scores.setdefault("张三", 20)
print(scores["张三"])
print()

'''
key 的判断             in          not in
'''
scores = {"张三": 100,
          "李四": 98,
          "王五": 45,
          "王二麻子":None}
print('张三' in scores)
print('张三' not in scores)
print()

# in 和 bool(get))的区别
print("王二麻子" in scores) # 判断key是否存在
print(bool(scores.get("王二麻子"))) # 判断key对应的value是否存在
print()

'''
指定字典元素的删除       del     pop()     clear()   popitem()
'''
scores.pop("李四")  # 删除指定的键值对
print(scores)
del scores['张三']  # 删除指定的键值对
print(scores)
scores.clear()  # 清空字典中所有元素
print(scores)
# del(scores)    # 删除字典地址
# print(scores)
print()
# popitem() -->删除当前字典里末尾一组键值对并将其返回
# 返回被删除的键值对，永远组包裹0索引时key，1索引是value
scores = {
    "张三": 100,
    "李四": 98,
    "王五": 45,
    '陈六': 75}
print(scores)
print(scores.popitem())
print(scores)
print(scores.popitem()[0])
print(scores)
print(scores.popitem()[1])
print(scores)
print()

'''
增加修改字典元素
'''
scores = {"张三": 100, "李四": 98, "王五": 45, '陈六': 75}
print(scores)
scores['陈六'] = 100  # 对存在键值对进行修改
print(scores)
print()

'''
获取字典视图的方法
    key()       获取字典中所有key
    value()     获取字典中所有value
    item()      获取字典中所有key.value对
'''
# 获取所有的key
scores = {"张三": 100,
          "李四": 98,
          "王五": 45}
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))  # 将所有键组成的试图转换成列表
print()

# 获取所有的value
values = scores.values()
print(values)
print(type(values))
print(list(values))
print()

# 获取所有的key-value对
item = scores.items()
print(item)
print(list(item))  # 转换之后的列表元素是由元组组成的
print()

'''
字典元素的遍历
'''
scores = {"张三": 100,
          "李四": 98,
          "王五": 45}
for item in scores:
    print(item, scores.get(item))
for values in scores:
    print(values, scores.get(values))
for key in scores:
    print(key, scores.get(key))
print()

"""
统计字典中键值对的数量
"""
scores = {"张三": 100, "李四": 98, "王五": 45}
print(f"键值对的数量为：{len(scores)}")
print()

"""
合并字典
"""
scores = {"张三": 100, "李四": 98, "王五": 45}
temp_scores = {"王二麻子": 56, "赵四": 78}
scores.update(temp_scores)
print(f"合并后的键值对为{scores}")
print(f"合并后的返回值为{scores.update(temp_scores)}")
print()

'''
字典的生成式
    通过内置函数zip()
        -->用于将可迭代的对象作为参数，将对象中对应的元素打包乘一个元组，然后返回由这些元组组成的列表
        -->可迭代对象为可用for-in遍历的对象
'''
items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85]
d = {item: price for item, price in zip(items, prices)}
print(d)
d = {item.upper(): price for item, price in zip(items, prices)}  # ,upper()  -->将元素转化为大写
print(d)
# 若key的数量和value的数量不一致，则多余的key或value被舍去
items = ['Fruits', 'Books', 'Others', 'Anything']
prices = [96, 78, 85, 45, 80]
d = {item: price for item, price in zip(items, prices)}
print(d)
items = ['Fruits', 'Books', 'Others', 'Anything']
prices = [96, 78, 85]
d = {item: price for item, price in zip(items, prices)}
print(d)
print()

"""
字典的拷贝
"""
fruits = {
    'apple': 30,
    'banana': 50,
    'pear': 100
}

# 使用赋值语句不会复制地址块内容，只会复制地址
real_fruits = fruits
real_fruits["peach"] = 30
print(fruits)
print(real_fruits)

# 使用浅拷贝使地址发生改变
real_fruits = fruits.copy()
real_fruits["orange"] = 50
real_fruits.update({'cherry': 100})
print(fruits)
print(real_fruits)
