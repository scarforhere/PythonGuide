# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Iterator_map
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-04 10:11 AM
-------------------------------------------------
Description : 

    map功能：
        对列表中的每个成员是否满足条件返回对应的True与None

    用法：
        map(func,list)

        func: 对每个item进行条件过滤定义
        list: 需要过滤的列表
"""
fruits = [
    'apple',
    'banana',
    'orange'
]

result = filter(lambda x: 'e' in x, fruits)
print(list(result))
print()


# 定义map判断函数
def map_func(item):
    if 'e' in item:
        return True


map_result = map(map_func, fruits)
print(list(map_result))

L = [1, 3, 5, 7, 9]
squares = list(map(lambda z: z ** 2, L))
big_numbers = list(filter(lambda n: n > 5, L))
# 等价于：
squares = [z ** 2 for z in L]
big_numbers = [z for z in L if z > 5]
