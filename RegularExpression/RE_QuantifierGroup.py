# coding: utf-8
"""
-------------------------------------------------
   File Name：     RE_QuantifierGroup
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-05 10:13 PM
-------------------------------------------------
Description : 

    正则表达式中的量词符号与组

    量词符号:
          符号                描述
        re1|re2     匹配正则表达式re1或re2
           ^        匹配字符串起始部分（等同于\A）
           $        匹配字符串终止部分（等同于\Z）
           *        匹配0此或多次前面出现的政策表达式
           +        匹配1此或多次前面出现的正则表达式
          {N}       匹配N次前面出现的正则表达式
         {M,N}      匹配M~N次前面出现的正则表达式
         [...]      匹配来自字符集中任意单一字符      (字符集中'^'不再代表开始，而是过滤掉)
        [..x-y..]   匹配x~y范围中的任意单一字符
         [^...]     不匹配此字符集中出现的任何单一字符，包括某一范围的字符（如果再此字符集中出现
           \        将特殊字符无效化

   组：
        符号              描述
         ()      在匹配规则中获取指定的数据

"""
import re

data = 'scar@tu-dresden.com'
# 匹配正则表达式re1或re2
print(re.findall('scar|com|tu-dresden', data))  # 按照字符串顺序返回，不按照匹配规则返回
print(re.findall('sc|ca', data))
print(re.findall('ca|ac', data))
print('*' * 60)
print()

# 匹配字符串起始部分
print(re.findall('^scar', data))
print(re.findall('^emm', data))
print('*' * 60)
print()

# 匹配字符串终止部分
print(re.findall('com$', data))
print(re.findall('emm$', data))
print('*' * 60)
print()
print('*' * 60)
print()

# 匹配0此或多次前面出现的政策表达式
print(re.findall('\w*', data))  # \w* 匹配0次或多次数字和字母
print('*' * 60)
print()

# 匹配1此或多次前面出现的正则表达式
print(re.findall('\w+', data))  # \w* 匹配1次或多次数字和字母
print('*' * 60)
print()

# 匹配N次前面出现的正则表达式
print(re.findall('\w{7}', data))
print(re.findall('\w{3}', data))  # 等同于[a-zA-Z0-9]
print(re.findall('[a-z]{3}', data))
print('*' * 60)
print()

# 匹配M~N此前面出现的正则表达式
print(re.findall('\w{3,7}', data))  # 按照允许的最大值进行返回
print('*' * 60)
print()

# 匹配来自字符集中任意单一字符
print(re.findall('[^scar]', data))  # 字符集中'^'不再代表开始，而是过滤掉
print('*' * 60)
print()

# 匹配x~y范围中的任意单一字符
print('*' * 60)
print()

# 不匹配此字符集中出现的任何单一字符，包括某一范围的字符（如果再此字符集中出现
print('*' * 60)
print()

# 将特殊字符无效化
print('*' * 60)
print()

# 组的应用
data = 'hello scar you are 24 age old'
result = re.search('hello (.*) you are (.*)', data)
print(result.groups())
print(result.group(1))
print(result.group(2))
