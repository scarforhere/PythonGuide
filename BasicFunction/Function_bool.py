# Programmed by Scar
"""
Python中一切皆对象，所有对象都有一个布尔值
获取对象的布尔值使用 bool()
"""
# 测试对象的布尔值
# 以下对象布尔值为False：
print(bool(False))  # False
print(bool(0))  # 0
print(bool(0.0))  # 0.0
print(bool(None))  # None
print(bool(''))  # 空字符串
print(bool(""))  # 空字符串
print(bool([]))  # 空列表
print(bool(list()))  # 空列表
print(bool(()))  # 空元组
print(bool(tuple()))  # 空元组
print(bool({}))  # 空字典
print(bool(dict()))  # 空字典
print(bool(set()))  # 空集合

print()

# 以下对象布尔值为True：
print(bool(18))
print(bool(True))
print(bool("Hallo the World"))
print()

# 直接使用对象判断
age = int(input("请输入年龄："))
print(age if age else "非法输入")
