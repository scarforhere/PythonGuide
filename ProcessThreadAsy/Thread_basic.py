# coding: utf-8
"""
-------------------------------------------------
   File Name：     Thread_basic
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-04 04:01 PM
-------------------------------------------------
Description : 
    线程使用方法
        方法名         说明                  举例
        Thread      创建线程            Thread(target,args)
        start       启动线程            start()
        join        阻塞知道线程执行结束  join(timeout=None)
        getName     获取线程的名字         getName()
        setName     设置线程的名字         setName()
        is_alive    判断线程是否存活        is_alive()
        setDaemon   守护线程            setDaemon(True)

    注意：由于GIL全局锁的原因，Python多线程只能使用到单一CPU

    而使用多进程可以利用到多个CPU

    解决方案：多进程+多线程


"""
import random
import time
import threading

lists=['python','django','tornado','flask','bs5','requests','uvloop']
new_lists=[]


def work():
    if len(lists)==0:
        return
    data=random.choice(lists)
    lists.remove(data)
    new_data=f'{data}_new'
    new_lists.append(new_data)
    time.sleep(1)

if __name__ == '__main__':
    start=time.time()
    t_list=[]
    for i in range(len(lists)):
        t=threading.Thread(target=work)
        t_list.append(t)
        t.start()

    for t in t_list:
        t.join()

    print(f'old_list:{lists}')
    print(f'new_list:{new_lists}')
    print(f'time is :{(time.time()-start)}')