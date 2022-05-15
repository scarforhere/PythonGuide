# coding: utf-8
"""
-------------------------------------------------
   File Name:      Process_pool_dataexchange
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-07-01 04:04 PM
-------------------------------------------------
Description : 

    Print info with under format:

"""
import multiprocessing
import json
import time


class Work(object):
    def __init__(self, q):
        self.q = q

    def send(self, message):
        # 只能传输字符串
        if not isinstance(message, str):
            message = json.dumps(message)

        self.q.put(message)

    def receive(self):
        while 1:
            result = self.q.get()
            try:
                res = json.loads(result)
            except:
                res = result
            print(f'recv is {res}')

    def send_all(self):
        for i in range(5):
            self.q.put(i)
            time.sleep(1)


if __name__ == '__main__':
    pool = multiprocessing.Pool(3)
    # 如果使用进程池pool创建进程的话，就需要使用Manager().Queue()
    q = multiprocessing.Manager().Queue()
    work = Work(q)
    send = pool.apply_async(func=work.send, args=({'name': 'Scar'},))
    recv = pool.apply_async(func=work.receive)
    send_all_p = pool.apply_async(func=work.send_all)

    pool.close()
    pool.join()
