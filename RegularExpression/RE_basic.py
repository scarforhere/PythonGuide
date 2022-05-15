# coding: utf-8
"""
-------------------------------------------------
   File Name：     RE_basic
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-05 09:39 PM
-------------------------------------------------
Description : 

    正则表达式应用场景：
        判断一个字符串是否符合规则
        取出指定数据
        爬虫岗位叫为核心的技术
        彩票网站匹配彩票信息

    导入政策表达式模块 re

    匹配字符串的需要条件：
        正则表达式模块 re
        匹配“针”的规则
        取“针”的字符串

    正则表达式中的特殊字符:
        \d  匹配任何十进制数字，与[0-9]一直
        \D  匹配任意非数字
        \w  匹配任何字母数字下划线字符   等同于[a-zA-Z0-9]
        \W  匹配非字母数字及下划线
        \s  匹配任何空格字符与[\n\t\r\v\f]相同
        \S  匹配任意非空字符
        \A  匹配字符串的起始
        \Z  匹配字符串的结束
        .   匹配任何字符（除了\n之外）

"""
import re

data = 'hello scar you are 24 age old'

# 匹配任何十进制数字，与[0-9]一直
print(re.findall('\d',data))
print()


def had_number(data):
        """
        判断字符串中是否有数字
        :param data:
        :return:
        """
        result=re.findall('\d',data)
        for i in result:
            return  True
        return  False

print(had_number(data))
print('*'*60)
print()

# 匹配任意非数字
def remove_number(data):
    """
    移除字符串中数字
    :param data:
    :return:
    """
    result = re.findall('\D', data)
    print(result)
    return ''.join(result)

print(remove_number(data))
print('*'*60)
print()

# 匹配任何空格字符与[\n\t\r\v\f]相同
print(re.findall('\s',data))
print('*'*60)
print()

# 匹配任意非空字符
def real_len(data):
    """
    返回字符串中除空格外长度
    :param data:
    :return:
    """
    result= re.findall('\S',data)
    return len(result)

print(len(data))
print(real_len(data))
print('*'*60)
print()


data = 'i am scar, i am 24'
# 匹配任何字母数字下划线字符
print(re.findall('\w',data))
print('*'*60)
print()

data = 'hello scar you are 24  year\'s old'
# 匹配非字母数字及下划线
print(re.findall('\W',data))
print('*'*60)
print()

# 匹配字符串的起始
print(re.findall('\Ahello',data))
print()
print(re.findall('\Ahellos',data))
print('*'*60)
print()


# 匹配字符串的结束
print(re.findall('old\Z',data))
print()
print(re.findall('ald\Z',data))
print('*'*60)
print()


# 匹配任何字符
print(re.findall('.',data))
print('*'*60)
print()

