# coding: utf-8
"""
-------------------------------------------------
   File Name：     Process_basic
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-04 10:27 AM
-------------------------------------------------
Description : 

    进程：
        进程是程序执行的载体
        打开每个程序都是启动以一个进程
        软件==进程

        进程的口粮：
            CPU算力，内存容量
        多进程：
            同时执行多个进程
            主进程为系统
            子进程为每个程序
        多进程串行：
            执行完一个进程再开始执行下一个进程
        多进行并行：
            同时执行多个程序

    线程：
        什么是线程：
            先有进程再有线程
        线程与进程的关系：
        进程提供线程执行程序的前置要求，线程在重组的资源配备下，去执行程序
            进程初始化所需CPU算力和内存空间
            线程执行业务逻辑

    multiprocessing模块
        函数名         介绍          参数          返回值
        Process     创建一个进程  target,args     进程对象
        start       执行进程        无               无
        join        阻塞程序        无               无
        kill        杀死进程        无               无
        is_alive    进程是否存活    无               无

"""
import time
import os
import multiprocessing


def work_a():
    for i in range(10):
        print(i, 'a', os.getpid())
        time.sleep(1)


def work_b():
    for i in range(10):
        print(i, 'b', os.getpid())
        time.sleep(1)


if __name__ == '__main__':
    # 单进程
    # start=time.time()
    # work_a()
    # work_b()
    # print(time.time()-start)
    # print(f'parent pid is {os.getpid()}')

    # 多进程
    start = time.time()
    #  子进程a
    a_p = multiprocessing.Process(target=work_a)

    #  子进程b
    b_p = multiprocessing.Process(target=work_b)

    # 开启进程
    for p in (a_p, b_p):
        p.start()
        # p.join()    # 阻塞下一个进程

    # 阻塞主进程
    for p in (a_p, b_p):
        p.join()

    # 进程是否存活
    for p in (a_p, b_p):
        print(p.is_alive())

    # 主进程
    print(time.time() - start)
    print(f'parent pid is {os.getpid()}')
