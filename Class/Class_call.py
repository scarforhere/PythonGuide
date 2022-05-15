# Programmed by Scar
"""
__call__()
共嗯：
    将一个类变成一个函数
"""


class Test(object):
    def __call__(self, *args, **kwargs):
        if args != ():
            print(f"args is {args}")

        if kwargs != {}:
            print(f"kargs is {kwargs}")


t = Test()
t("single", name="Scar", age=24)
print("*" * 30)
t(name="Scar", age=24)
print("*" * 30)
t("single")
print()
