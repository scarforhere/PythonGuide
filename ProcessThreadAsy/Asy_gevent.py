# coding: utf-8
"""
-------------------------------------------------
   File Name：     Asy_gevent
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-04 05:40 PM
-------------------------------------------------
Description : 

     gevent模块常用方法：
        函数名         介绍            参数          返回值
        spawn       创建写成对象       Func,args   协程对象
        joinall     批量处理协程对象   [spawnobj]  [spawnobj]

"""
import os
import time
import random
import asyncio
import gevent

def gevent_a():
    for i in range(10):
        print(f'i  a_gevent {os.getpid()}')
        gevent.sleep(random.random())
    return 'gevent a result'

def gevent_b():
    for i in range(10):
        print(f'i  b_gevent {os.getpid()}')
        gevent.sleep(random.random())
    return 'gevent b result'

if __name__ == '__main__':
    start = time.time()

    g_a=gevent.spawn(gevent_a)
    g_b=gevent.spawn(gevent_b)
    gevent_list=[g_a,g_b]
    result=gevent.joinall(gevent_list)
    print(result)
    print(dir(result))
    print(dir(result[0]))
    print(dir(result))
    # 提取结果
    print(result[0].value)
    print(result[1].value)

    print(time.time() - start)
    print(f'parent is {os.getpid()}')