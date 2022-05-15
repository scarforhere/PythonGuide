# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Iterator_reduce
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-04 10:13 AM
-------------------------------------------------
Description : 

    reduce功能：
        对循环前后两个数据进行累加

    用法：
        reduce(func,list)

        func: 对数据累加的函数
        list: 需要过滤的列表

"""
from functools import reduce

reduce_result = reduce(lambda x, y: x + y, [0, 1, 2])
print(reduce_result)
print()

reduce_result = reduce(lambda x, y: x * y, [1, 1, 2, 4])
print(reduce_result)
print()

fruits = [
    'apple',
    'banana',
    'orange'
]
reduce_result_str = reduce(lambda x, y: ''.join([x, y]), fruits)
print(reduce_result_str)
print()
