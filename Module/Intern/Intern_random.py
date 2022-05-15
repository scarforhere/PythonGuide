# Programmed by Scar
"""
random模块：
    Python内置的random随机数模块
常用方法：
    random.random()             返回一个[0,1)区间间的随机浮点数
    random.uniform(a,b)         返回一个[a,b]区间内的随机浮点数
    random.randint(a.b)         返回一个[a,b]区间内的随机浮整数
    random.choice(obj)          返回对象中的一个随机元素
    random.sample(obj,n)        返回对象(obj)中的一个指定数目(n)随机元素
    random.randrange(a,b,step)  返回一个[a,b)区间内的随机浮点数,数值间隔为step
"""
import random

# 返回一个(0,1)区间间的随机浮点数
print("random.random()             返回一个(0,1)区间间的随机浮点数")
print(random.random())
print()

# 返回一个(a,b)区间内的随机浮点数
print("random.uniform(a,b)         返回一个(a,b)区间内的随机浮点数")
print(random.uniform(0,10))
print()

# 返回一个(a,b)区间内的随机浮点数
print("random.randint(a.b)         返回一个(a,b)区间内的随机浮整数")
print(random.randint(0,10))
print()

# 返回对象中的一个随机元素
print("random.choice(obj)          返回对象中的一个随机元素")
print(random.choice(['a',1,True,('c','d')]))
print(random.choice('abc'))
print()

# 返回对象(obj)中的一个指定数目(n)随机元素
print("random.choice(obj)          返回对象中的一个随机元素")
print(random.sample(['a',1,True,('c','d')],2))
print(random.sample('abc',2))
print()

# 返回一个(a,b)区间内的随机浮点数,数值间隔为step
print("random.randrange(a,b,step)  返回一个(a,b)区间内的随机浮点数,数值间隔为step")
print(random.randrange(0,10,2))
print()