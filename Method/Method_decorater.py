# Programmed by Scar
"""
装饰器：
    什么是装饰器：
        装饰器是一种函数
        可以接受函数作为参数
        可以返回函数
        接收一个函数，内部对其处理，然后返回一个新函数，东涛的增强函数功能
        将c函数在a函数中执行，在a函数中可以选择这姓或不执行c函数，也可以对c函数的结果进行二次加工处理
    装饰器的定义：
        def out(func_args):                         # 外围函数
            def inter(*args,**kwargs):              # 内嵌函数
                return func_args(*args,**kwargs)
            return inter                            # 外汇函数必须返回
    装饰器的用法：
        1. 将被调用的函数直接作为参数传入装饰器的外围函数括弧
                def a(func):
                    def b(*args,**kwargs):
                        return func(*args,**kwargs)
                    return b
                def c(name):
                    print(name)
                a(c("Scar"))        # Scar
        2. 将装饰器与被调用的函数绑定在一起
           @符号+装饰器函数放在被调用函数的上一行，被调用的函数正常定义，只需要直接调用被执行函数即可
                @a
                def c(name)
                    print(name)
                c("Scar")           # Scar
"""
import types
def check_str(func):
    # print("func:",func)
    def inner(*args,**kwargs):
        # print("args:",args,"kwargs:",kwargs)
        result=func(*args,**kwargs)         # 将被装饰函数的结果进行判断
        # print(result)
        # print(type(result))
        if result == "ok":
            return f"result is {result}"
        else:
            if isinstance(result, list):
                return f"Input is a list"
            elif isinstance(result, dict):
                return f"Input is a dict"
            elif isinstance(result, int):
                return f"Input is a int"
            else:
                return "Can not be recognized!"
    return inner

@check_str
def test(a):
    return a

l1=[10,20,30]
d1={"a":10,"b":20,"c":30}
print()

result =test(10)
print(result)
print()

result =test(l1)
print(result)
print()

result =test(d1)
print(result)
print()

result =test("ok")
print(result)
print()
