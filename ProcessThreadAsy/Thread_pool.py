# coding: utf-8
"""
-------------------------------------------------
   File Name：     Thread_pool
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-04 04:19 PM
-------------------------------------------------
Description : 

    线程池内志保concurrent.futures

    线程使用方法
        方法名                         说明                              举例
        futures.ThreadPoolExecutor  创建线程池                       tpool=ThreadPoolExecutor(max_workers
        submit                      往线程池种加入任务                   submit(target,args
        done                        线程池中的某个线程是否完成了任务        done()
        result                      获取当前线程执行任务的结果               result()

"""
from concurrent.futures import ThreadPoolExecutor
import time
import threading
import os

lock = threading.Lock()

def work(i):
    lock.acquire()
    print(i)
    time.sleep(1)
    lock.release()
    return f'result is: {i}, pid is: {os.getpid()}'


if __name__ == '__main__':
    print(os.getpid())
    t= ThreadPoolExecutor(2)
    result=[]
    for i in range(20):
        t_result=t.submit(work,i)
        result.append(t_result)

    for res in result:
        print(res.result())

