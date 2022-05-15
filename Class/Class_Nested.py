# Programmed by Scar
"""
test.a.b.c.d()
列式操作
"""
class Test(object):
    def __init__(self,attr=''):
        self.__attr=attr

    def __getattr__(self, item):
        if self.__attr:
            key=f"{self.__attr}.{item}"
        else:
            key=item

        print(key)
        return Test(key)

    def __call__(self, *args, **kwargs):
        if args is not None:
            return args
        elif kwargs is not None:
            return kwargs
        else:
            return args, kwargs
t=Test()
name=t.a.b.c.d("Scar")
print(name)