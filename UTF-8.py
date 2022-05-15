# coding:gbk
"""
默认使用UTF-8编码
加上coding:gbk使用国标编码
加上coding:utf-8使用UTF-8编码
加上coding:ascii使用ASCII编码
需要在文件开头进行编码指定
"""

"""
#! /usr/bin/env
指定解释器路径
"""

# Programmed by Scar
"""
计算机中使用1-6个字节来表示一个UTF-8字符，涵盖了地球上几乎所有地区的文字
大多汉字使用3个字节表示
UTF-8时UNICODE编码的一种编码格式
"""
print(chr(0b100111001011000))
# chr()字符转换
# ob 二进制初始表头
print(ord("A"))
# ord()十进制转换
