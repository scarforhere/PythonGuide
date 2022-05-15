# Programmed by Scar
"""
# 保留字

标识符：变量、函数、类、模块的名字
字母、数字、下划线
不能以数字开头
不能是保留字
严格区分大小写

通用命名法：
    变量名所有字符都为小写
    单词间由"_"链接
     exp. : data_s, data_d

 驼峰命名法：
    小驼峰命名法：
        第一个单词以小写字母开始
        后续字符使用大写首字母
        exp. : firstName, secondName
    大驼峰命名法：
        每一个单词首字母大写
        exp. : FirstName, SecondName
"""
import keyword
lst=keyword.kwlist
for item in lst:
    print(item)


