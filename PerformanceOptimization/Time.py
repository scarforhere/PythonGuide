# coding: utf-8
"""
-------------------------------------------------
   File Name:      Time
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-05-23 08:55 AM
-------------------------------------------------
Description : 

    时间模块优化：
        运行速度：
            --> 字符串公式 > 函数 > 包内方法 > time模块

"""

"""
Modul: Time
    Vorteil: sehr einfach
    Nachteil: zusätzlicher („boilerplate“)-Code im Programm verteilt
"""
import time

s = 0
start = time.time()
for i in range(100000):
    s += i ** (0.5)
print("Dauer [s]:", time.time() - start)

"""
Modul: timeit
    Laufzeitmessung eines Statements (meist Funktionsaufruf)
    Gut für Vergleich von Codesnippets für spezielles Problem
    Statement muss als string oder callable übergeben werden
    Vorteile: nicht invasiv, Mittelung mehrerer Durchläufe
"""
import timeit
import math


def wurzel_v1():
    return math.sqrt(2)


def wurzel_v2():
    return 2 ** 0.5


print(timeit.timeit("2**0.5", number=100000))
print(timeit.timeit(wurzel_v1, number=100000))
print(timeit.timeit(wurzel_v2, number=100000))
# 运行速度：
#       --> 字符串公式 > 函数 > 包内方法 > time模块

"""
Modul: cProfil
"""
import cProfile
def main():
    s = 0
    for i in range(100000):
        s += i**2
cProfile.run("main()")