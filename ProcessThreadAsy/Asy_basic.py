# coding: utf-8
"""
-------------------------------------------------
   File Name：     Asy_basic
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-04 05:18 PM
-------------------------------------------------
Description : 

    异步：
        避免程序阻塞
        轻量级线程：协程
        可以获取异步函数的返回值
        主进程需要异步才行
        适合文件读写使用

    async定义异步：
        async def test():
            pass

    await执行异步
        async def handle():
            result = await test()

    asyncio内置模块调用async函数
        函数名         介绍                  参数          返回值
        gather  将异步函数批量执行       asyncfunc...        List
        run     执行主异步函数             [task]      执行函数的返回结果

"""
import os
import time
import random
import asyncio


async def a():
    for i in range(10):
        print(i, 'a',os.getpid())
        await asyncio.sleep(random.random())
    return 'a function'


async def b():
    for i in range(10):
        print(i, 'b',os.getpid())
        await asyncio.sleep(random.random())
    return 'b function'


async def main():
    result = await asyncio.gather(
        a(),
        b()
    )
    print(result)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)
    print(f'parent is {os.getpid()}')
