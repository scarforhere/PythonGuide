# coding: utf-8
"""
-------------------------------------------------
   File Name:      Process_pool_SuspendResume
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-06-30 10:52 AM
-------------------------------------------------
Description : 

    Suspend adn resume process between several processes in ProcessPool

"""
import multiprocessing
import psutil
import time
import os


class ProcessControl(object):
    def __init__(self, q):
        self.q = q
        self.pid_dict = dict()

    def send(self, key, value, operation):
        message = [key, value, operation]
        self.q.put(message)

    def receice(self):
        while 1:
            result = self.q.get()
            print(result)

    def set_value(self, pid, stats, operation):
        self.pid_dict[pid] = [stats, operation]

    def del_value(self, pid):
        self.pid_dict.pop(pid)

    def control_main(self):
        while 1:
            result = self.q.get()

            if result[2] == 'set_value':
                self.set_value(result[0], result[1], result[2])
            elif result[2] == 'del_value':
                self.del_value(result[0])
            else:
                continue

            # If ProcessPool is empty, end program
            if self.pid_dict == {}:
                break

            # Suspend and Resume Process
            self.suspend_resume()

    def suspend_resume(self):
        pid_flag = False
        pid_list = []

        # get suspend flag
        # get pid_list except pid with True value
        for pid in self.pid_dict:
            pid_list.append(pid)
            if self.pid_dict.get(pid)[0] is True:
                pid_flag = True
                pid_list.remove(pid)

        # suspend process except pid with True value
        if pid_flag:
            for pid in pid_list:
                pause = psutil.Process(pid)
                pause.suspend()

        # resume process
        else:
            try:
                for pid in pid_list:
                    pause = psutil.Process(pid)
                    pause.resume()
            except BaseException as e:
                print(self.pid_dict)
                print(e)

    def printtest1(self):
        pid = os.getpid()
        self.send(pid, False, 'set_value')

        for j in range(1, 4):
            print(pid, j)
            time.sleep(1)
        self.send(pid, True, 'set_value')

        for j in range(4, 8):
            print(pid, j)
            time.sleep(1)
        self.send(pid, False, 'set_value')
        self.send(pid, False, 'del_value')

    def printtest2(self):
        pid = os.getpid()
        self.send(pid, False, 'set_value')

        for j in range(1, 4):
            print(pid, j)
            time.sleep(1)

        for j in range(4, 8):
            print(pid, j)
            time.sleep(1)

        self.send(pid, False, 'del_value')


if __name__ == '__main__':
    pool = multiprocessing.Pool(4)
    q = multiprocessing.Manager().Queue()
    work = ProcessControl(q)

    ctrl = pool.apply_async(func=work.control_main)
    major = pool.apply_async(func=work.printtest1)
    sub1 = pool.apply_async(func=work.printtest2)
    sub2 = pool.apply_async(func=work.printtest2)
    # receice = pool.apply_async(func=work.receice)

    pool.close()
    pool.join()
