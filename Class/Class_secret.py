# Programmed by Scar
"""
私有属性和私有方法

在实际开发中，对象的某些属性或方法可能只希望在对象的内部被调用，而不希望在外部北方问道
私有属性就是对象不希望公开的属性
私有方法就是对象不希望公开的方法

定义方式：
    在定义私有属性或私有方法时，在属性或方法名前增加"__"
"""


class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 私有方法不允许在对象外部被访问
        print(f"{self.name}的年龄是{self.__age}")


xiaofang = Women("小芳")

# 私有属性在外部不能被直接访问
# print(xiaofang.__age)
# 私有属性在方法的内部是可以被访问的
# xiaofang.secret()

"""
私有方法和属性可以被强制访问
"""
# 或取所有可访问的属性和方法
lst=dir(xiaofang)
for item in lst:
    print(item)

print()
xiaofang._Women__secret()
print(xiaofang._Women__age)