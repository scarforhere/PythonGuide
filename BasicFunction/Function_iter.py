# Programmed by Scar
"""
生成迭代器
    iterable可遍历对象：列表，元组，字典，集合
"""

iter_obj = iter([1, 2, 3])

print(iter_obj, type(iter_obj))


def _next(iter_obj):
    try:
        return next(iter_obj)
    except StopIteration:
        return None


print(_next(iter_obj))
print(_next(iter_obj))
print(_next(iter_obj))
print(_next(iter_obj))
