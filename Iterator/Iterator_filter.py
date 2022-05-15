# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Iterator_filter
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-04 10:08 AM
-------------------------------------------------
Description : 

    filter 功能：
        对星环根据过滤条件进行过滤

    用法：
        filter(func,list)

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


# 定义filter判断函数
def filter_func(item):
    if 'e' in item:
        return True


filter_result = filter(filter_func, fruits)
print(list(filter_result))

L = [1, 3, 5, 7, 9]
squares = list(map(lambda z: z ** 2, L))
big_numbers = list(filter(lambda n: n > 5, L))
# 等价于：
squares = [z ** 2 for z in L]
big_numbers = [z for z in L if z > 5]
