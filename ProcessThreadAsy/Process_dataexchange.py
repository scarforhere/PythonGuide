# coding: utf-8
"""
-------------------------------------------------
   File Name：     Process_dataexchange
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-04 03:37 PM
-------------------------------------------------
Description : 

    进程间的通信需要使用队列

    函数名         介绍          参数          返回值
    Queue       队列的创建       mac_cout    队列对象
    put         信息放入队列      message     无
    get         获取队列信息      无            str

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
    q = multiprocessing.Queue()
    work = Work(q)
    send = multiprocessing.Process(target=work.send, args=({'name': 'Scar'},))
    recv = multiprocessing.Process(target=work.receive)
    send_all_p = multiprocessing.Process(target=work.send_all)

    send.start()
    recv.start()
    send_all_p.start()

    # 使用执行时常最长的进程对主进程进行阻塞
    send_all_p.join()
    recv.terminate()
