# coding: utf-8
"""
-------------------------------------------------
   File Name:      globle_variante
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-06-29 11:01 AM
-------------------------------------------------
Description : 

        #先必须在主模块初始化（只在Main模块需要一次即可）
        GlobalValue()

        #定义跨模块全局变量
        GlobalValue.set_value('CODE','UTF-8')

        # 读取全局变量
        code = GlobalValue.get_value('CODE')

"""
_global_dict = {}


class GlobalValue:
    def __init__(self):
        global _global_dict

    @staticmethod
    def set_value(key, value):
        """
        Define a global variant
        """
        _global_dict[key] = value

    @staticmethod
    def get_value(key, defValue=None):
        """
        Get value of global variant
        If not exist, return default value
        """

        try:
            return _global_dict[key]
        except KeyError:
            return defValue

    @staticmethod
    def del_value(key):
        _global_dict.pop(key)


if __name__ == '__main__':
    GlobalValue()

    GlobalValue.set_value(1111, 10)
    GlobalValue.set_value(2222, 20)
    GlobalValue.set_value(3333, 30)

    print(GlobalValue.get_value(1111))
    print(GlobalValue.get_value(2222))
    print(GlobalValue.get_value(3333))
