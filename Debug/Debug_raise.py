# Programmed by Scar
"""
手动抛出异常及自定义异常类型
    手动抛出异常
        raise Exception(str)    手动报错，内容显示为str
    自定义异常类型
        继承基类： Exception
        在构造函数中定义错误信息
"""
# 手动抛出异常 raise Exception(str)
try:
    score = int(input('请输入分数：'))
    if 0 <= score <= 100:
        print('分数为：', score)
    else:
        raise Exception('分数不正确')
        # raise ValueError("数据类型错误！")
        # ZeroDivisionError("不能被零除")
        # IndexError("没有指定索引")
except BaseException as e:
    print(e)


# 自定会异常类型
class NumberLimitError(Exception):
    def __init__(self, message):
        self.message = message


class NameLimitError(Exception):
    def __init__(self, message):
        self.message = message


def number_check(num):
    if num >= 100:
        raise NumberLimitError("数字不能大于100")
    else:
        return num


def name_check(name):
    if name == 'fuck':
        raise NameLimitError("请输入合法字符")
    else:
        return name


try:
    # print(name_check("Scar"))
    # print(name_check("fuck"))
    print(number_check(10))
    print(number_check(200))
except Exception as e:
    print(e)
