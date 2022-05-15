# coding: utf-8
"""
-------------------------------------------------
   File Name：     Process_pool
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-04 03:01 PM
-------------------------------------------------
Description : 

    什么是进程池：
        进程池就是允许进程数目的资源池
        避免了创建与关闭的小号
        当进程池被占满时，新增进程排队等待

    进程池的创建：
        函数名                 介绍                  参数          返回值
        Pool            进程池创建               Processcount    进程池对象
        apply_async     任务加入进程池（异步）     func，args      无
        close           关闭进程池               无              无
        join            等待进程池任务结束        无               无

    进程锁的用法：
        from multiprocessing import Manager
        manage = Manager()
        lock = manage.Lock()

        函数名       介绍        参数      返回值
        acquire     上锁          无       无
        release     解锁          无       无

"""
import multiprocessing
import os
import time


def work(count, lock):
    lock.acquire()
    print(count, os.getpid())
    time.sleep(3)
    lock.release()
    return f'result is {count}, pid is{os.getpid()}', 'aaaa'


if __name__ == '__main__':
    pool = multiprocessing.Pool(2)
    manager = multiprocessing.Manager()
    lock = manager.Lock()
    results = []
    for i in range(6):
        # 异步执行程序
        result = pool.apply_async(func=work, args=(i, lock))
        results.append(result)

    for res in results:
        print(res.get()[0])

    # # 当进程池只运行一次时需添加，用来保证主进程在子进程执行完后再结束
    # 关闭进程池 关闭后po不再接受新的请求
    pool.close()
    # 等待po中所有子进程执行完成，必须放在close语句之后
    # 如果没有join，会导致进程中的任务不会执行
    pool.join()
