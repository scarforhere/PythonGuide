# Programmed by Scar
"""
Lambda函数：

定义一个轻量化的函数
    轻量化：即用即删除，很适合需要完成一项功能，但是此功能只在一处使用

定义方法
    1. 无参数定义：
        f = lambda : value
        f()
    2.  有参数定义：
        f = lambda x,y: x*y
        f(3,4)
"""
# 无参数定义：
f = lambda : 1
result = f()
print(result)

f = lambda : print(1)
f()
print()

# 有参数定义：
f1 = lambda x,y: x*y
print(f1(1,2))

f1 = lambda x,y=2: x*y
print(f1(1))

f1 = lambda x=1,y=2: x*y
print(f1())
print()

# 定义的轻量化函数可以传入种类
f1 = lambda x,y=2: x>y
print(f1(1))
print()

# lambda的使用场景
users=[
    {"name":'dawei'},
    {"name":'xiaomu'},
    {"name":'asan'}
]
users.sort(key=lambda x:x["name"])
print(users)