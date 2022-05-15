# Programmed by Scar
"""
字符串是Python中的基本数据类型，是不可变字符序列

字符串的主流机制：
    仅保存一份相同且不可变字符串的方法，不同的值被存放在字符串的驻留池中
    Python的主流机制对相同的字符串只保留一份拷贝，后续创建相同字符串时不会开创新空间，二十吧该字符串的地址赋给新创建的变量

驻留机制的几种情况(交互模式，非Pycharm)
    1. 字符串长度为0或
    2. 符合标识符的字符串：字母、数字、下划线
    3. 字符串旨在编译时进行驻留，而非运行时
    4. [-5 , 256]之间的整数数字

sys中的intern方法2个字符串指向同一对象

PyCharm对字符串进行了优化处理

字符串驻留机制的优缺点
    当需要值相同的字符串时，可以直接从字符串池中拿来使用，避免频繁的创建和销毁，提示效率和节约内存
    因此拼接字符串和修改字符串会比较影响性能

    在需要进行字符串拼接时建议使用str类型的join方法，而非“+”
    因为join()方法时先计算出所有字符串中的长度，然后拷贝，只new一次对象，效率比“+”高
"""

'''
创建新字符串
'''
a = 'Python'
b = "Python"
c = '''Python'''
print(a, type(a), id(a))
print(b, type(b), id(b))
print(c, type(c), id(c))  # 相同字符串内容不开辟新地址
print()

"""
字符串的基本操作
"""
# 链接字符串
str1 = 'hallo'
str2 = 'python'
str3 = str1 + str2
print(str3)
print()

# 统计字符串中元素个数 len
str1 = 'Python'
print(len(str1))
print()

# 打印多个重复字符串
print('-' * 20)
print()

'''
字符串的常用方法
    查找和替换的方法：
        index()             查找字符串substr第一次出现的位置，如果查找的字符串不存在时抛出ValueError
        rindex()            查找字符串substr最后一次出现的位置，如果查找的字符串不存在时抛出ValueError
        find()              查找字符串substr第一次出现的位置，如果查找的字符串不存在时，则返回-1
        rfind()             查找字符串substr最后一次出现的位置，如果查找的字符串不存在时，则返回-1
        endwith(str)        判断字符串是否以str为结尾
        startswith(str)     判断字符串是否以str为开头
        replace()       第一个参数指定被替换的字符串
                        第二个参数指定用于替换的字符串
                        该方法返回替换后得到的字符串，替换前的字符串不发生改变
'''
print('查找和替换的方法：:')
print('-' * 60)
s = 'Hallo,hallo'
print('01.', s.index('lo'))  # 3
print('02.', s.find('lo'))  # 3
print('03.', s.rindex('lo'))  # 9
print('04.', s.rfind('lo'))  # 9
print()

# 建议使用find(), 和rfind（）
# print(s.index('k'))       # 异常ValueError
print('05.', s.find('k'))  # -1
# print('',s.rindex('k'))      # 异常ValueError
print('06.', s.rfind('k'))  # -1
print()

# endwith(str)     判断定的字符串是否以str为结尾
print('07. ', 'abcd'.endswith('ab'))  # False
print('08. ', 'abcd'.endswith('cd'))  # True
print('09. ', 'ab张三'.endswith('张三'))  # True
print()

# startswith(str)   判断定的字符串是否以str为开头
print('10. ', 'abcd'.startswith('ab'))  # True
print('11. ', 'abcd'.startswith('cd'))  # False
print('12. ', '张三ab'.startswith('张三'))  # True
print()

# replace() 返回替换后的新字符串，旧字符串不改变
s = 'hallo,Python'
print('13. ', s.replace("Python", 'Java'))
print('14. ', s)
s = 'hallo,Python,Python,Python'
print('15. ', s.replace('Python', 'Java', 2))
print()

'''
字符串的常用方法
    拆分和链接的方法:
        partition(str)      把字符串分成一个3元素的元组(str前面,str,str后面)
        rpartiation         类似partition()方法，从右边开始拆分
        split()             从字符串左侧开始分劈，默认的分劈字符时空格字符串，返回值是一个列表
                            通过参数sep指定劈分字符串时的字符
                            通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大劈分之后，剩余的字符串会单独作为一部分
        rsplit()            从字符串右侧开始分劈，默认的分劈字符时空格字符串，返回值是一个列表
                            通过参数sep指定劈分字符串时的字符
                            通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大劈分之后，剩余的字符串会单独作为一部分
        splitlines()        按照行\r,\n,\r\m分隔，返回一个包含各行作为元素的列表
        join(seq)           以指定字符串作为分隔符，将seq中所有元素和并作为一个新的字符串
'''
# split() 和 rsplit()    从字符串开始分劈，默认的分劈字符时空格字符串，返回值是一个列表
# 默认参数进行劈分字符串
s = 'hello world Python'
print(s.split())
print(s.rsplit())
print()
# 指定劈分字符
s1 = 'hello|world|Python'
print(s1.split())
print(s1.split(sep='|'))
print(s1.rsplit(sep='|'))
print()
# 指定最大劈分次数
print(s1.split(sep='|', maxsplit=1))
print(s1.rsplit(sep='|', maxsplit=1))
print()

# join(seq)           以指定字符串作为分隔符，将seq中所有元素和并作为一个新的字符串
lst = ['hallo', 'java', 'Pyhton']
print(''.join(lst))
print('|'.join(lst))
print(' '.join(lst))
print('*'.join('Python'))  # 将'Python'作为字符串序列进行拆分
print()

'''
字符串的常用方法
    去除空格的方法：
        strip()     字符串中首尾的空格去除
        rstrip()    去除字符串中右侧空格
        lstrip()    去除字符串中左侧空格
        
    注意：所有对其操作都返回新字符串，不对原有字符串进行操作
'''
print('去除空格的方法:')
print('-' * 60)
# strip()
print('01. ', '|', '     asdasd    asdasd       '.strip(), '|')
# rstrip()
print('02. ', '|', '     asdasd    asdasd       '.rstrip(), '|')
# lstrip()
print('03. ', '|', '     asdasd    asdasd       '.lstrip(), '|')
print()

'''
字符串的常用方法
    判断类型的方法：
        isspace()           判断指定的字符串是否全部由空白字符组成(回车、换行、水平制表符Tab)
        isdecimal()         判断指定的字符串是否全部由十进制的数字组成
        isdigit()           判断是否全部为数字
        isnumeric()         判断指定的字符串是否全部由数字组成
        isalpha()           判断指定的字符串是否全部由字母组成
        isalnum()           判断指定的字符串是否全部由字母和数字组成
        istitle()           判断是否每个单词首字母大写
        isupper()            判断是否所有字符都是大写
        islower()           判断是否所有字符都是小写
        isidentifier()      判断指定的字符串是不是合法的标识符(字母、汉字、数字、下划线)
'''
print('判断类型的方法:')
print('-' * 60)
# isspace()        判断指定的字符串是否全部由空白字符组成(回车、换啊很难过、水平制表符Tab)
print('01. ', '\n\t\r'.isspace())  # True
print('01. ', '    a'.isspace())  # False
print()

# isdecimal()      判断指定的字符串是否全部由十进制的数字组成,不能判断小数！
# 全角数字
print('02. ', '123'.isdecimal())  # True
print('04. ', '123四'.isdecimal())  # False
print('05. ', 'ⅠⅡⅢ'.isdecimal())  # False
print('06. ', '\u00b2'.isdecimal())  # False
print('07. ', '1.23'.isdecimal())  # False
print()

# isdigit()        判断是否全部为数字,不能判断小数！
# 全角数字、(1)、\u00b2
print('08. ', '123'.isdigit())  # True
print('09. ', '123四'.isdigit())  # False
print('10. ', 'ⅠⅡⅢ'.isdigit())  # False
print('11. ', '\u00b2'.isdigit())  # True
print('12. ', '1.23'.isdigit())  # False
print()

# isnumeric()      判断指定的字符串是否全部由数字组成,不能判断小数！
# 全角数字、(1)、\u00b2、中文数字
print('13. ', '123'.isnumeric())  # True
print('14. ', '123四'.isnumeric())  # True
print('15. ', 'ⅠⅡⅢ'.isnumeric())  # True
print('16. ', '\u00b2'.isnumeric())  # True
print('17. ', '1.23'.isnumeric())  # False
print()

# isalpha()        判断指定的字符串是否全部由字母组成
print('18. ', 'abc'.isalpha())  # True
print('19. ', '张三'.isalpha())  # True
print('20. ', '张三_'.isalpha())  # False
print('21. ', '张三1'.isalpha())  # False
print()

# isalnum()        判断指定的字符串是否全部由字母和数字组成
print('22. ', 'abc1'.isalnum())  # True
print('23. ', '张三123'.isalnum())  # True
print('24. ', 'abc!'.isalnum())  # False
print()

# isidentifier()   判断指定的字符串是不是合法的标识符
s = 'hello,python'
print('25. ', s.isidentifier())  # False
print('26. ', 'hallo'.isidentifier())  # True
print('27. ', '张三_123'.isidentifier())  # True
print()

'''
字符串的常用方法
    文本对其的方法：
        center()     剧中对齐，第一个参数指定宽度，第二个参数指定填充字符，第二个参数是可选的，默认为空格，
                        如果设置宽度小于实际宽度则返回原字符串
        ljust()      左对齐，第一个参数指定宽度，第二个参数指定填充字符，第二个参数是可选的，默认为空格，
                        如果设置宽度小于实际宽度则返回原字符串
        rjust()      右对齐，第一个参数指定宽度，第二个参数指定填充字符，第二个参数是可选的，默认为空格，
                        如果设置宽度小于实际宽度则返回原字符串
        zfill()      右对齐，左边用0填充，该方法只接受一个参数，用于指定字符串的宽度，
                        如果设置宽度小于实际宽度则返回原字符串

    注意：所有对其操作都返回新字符串，不对原有字符串进行操作
'''
print('文本对其的方法：')
print('-' * 60)
# 居中对齐
s = 'hello,Python'
print('01. ', '|', s.center(20, '*'), '|')
print('02. ', '|', s.center(19, '*'), '|')  # 计算完左右不相等时左长右短
print('03. ', '|', s.center(20), '|')  # 默认填充空格
print('04. ', '|', s.center(10), '|')  # 返回原字符串
print()

# 左对齐
print('05. ', '|', s.ljust(20, '*'), '|')
print('06. ', '|', s.ljust(20), '|')  # 默认填充空格
print('07. ', '|', s.ljust(10), '|')  # 返回原字符串
print()

# 右对齐
print('08. ', '|', s.rjust(20, '*'), '|')
print('09. ', '|', s.rjust(20), '|')  # 默认填充空格
print('10. ', '|', s.rjust(10), '|')  # 返回原字符串
print()

# 右对齐，强制左侧填充0
# print(s.zfill(20,'*'))     # 设置第二个参数报错
print('11. ', '|', s.zfill(20), '|')  # 默认左侧填充0
print('12. ', '|', s.zfill(10), '|')  # 返回原字符串
print('13. ', '|', '-8910'.zfill(8), '|')  # 若第一个字符为负号，则0填充到负号右侧
print('14. ', '|', '8-910'.zfill(8), '|')
print()

'''
字符串的切片操作
    字符串时不可变类型
        不具备增、删、改等操作
        切片操作将产生新的对象
'''
s = 'hello,Python'
s1 = s[:5]
s2 = s[6:]
newstr = s1 + s2
print(s, id(s))
print(s1, id(s1))
print(s2, id(s2))
print(newstr, id(newstr))
print(s[1:5:2])  # [ start : stop : step ]
print(s[::2])  # 默认从0开始
print(s[::-1])  # 默认从字符串最后一个元素开始，字符串倒置
print(s[-6::1])  # 索引从-6开始，到字符串最后一位结束
print()

'''
字符串的大小写转换操作的方法
    1. upper()          把字符串所有字符转换为大写字母
    2. lower()          把字符串中所有字符转化成小写字母
    3. swapcase()       把字符串所有字符转换为大写字母，所有字符转化成小写字母
    4. capitalisze()    把第一个字符转化为大写，把其余字符转化为小写
    5. title()          把每个单词的的第一个字符转化为大写，把每个单词的剩余字符转化为小写
'''
# 小写转大写
s = 'hallo.python'
a = s.upper()
print(s, id(s))
print(a, id(a))  # 产生一个新的字符串
print()
# 大写转小写
b = s.lower()
print(s, id(s))
print(b, id(b))  # 产生一个新的字符串
print(b == s)  # True 内容相等
print(b is s)  # False 地址不相等
print()
# 大小写互换
s2 = 'hello,Python'
print(s2.swapcase())
print()
# 每个单词首字母大写，其余字母小写
print(s2.title())
print()
# 第一个字符大写，其余字符小写
print(s2.capitalize())
s3 = '%hello,world'
print(s3.capitalize())
print()

'''
字符串的比较操作
    运算符：    >   >=  ==   <=  !=

    比较规则：
        首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符
        依次比较下去，知道两个字符串中的字符不相等时
        其比较结果就是两个字符串的比较结果，两个字符串中的所有后续字符将不再被比较

    比较原理
        将字符串进行比较时，比较的是其ordinal value(原始值)
        调用内置函数ord可以得到指定字符的ordinal value
        与其内置函数ord对应的是内置函数chr
        调用内置函数chr时指定ordinal value可以得到其对应的字符
'''
print('apple' > 'app')  # True
print('apple' > 'banana')  # False      相当于比较'a'和'b'的原始值 a:97 < b:98
print()

print(ord('a'), ord('b'))
print(chr(97), chr(98))
print(ord('宋'))
print(chr(23435))
print()

'''
字符串的格式化操作
    格式化字符串的三种方式：
        1. %作为占位符
                '我的名字叫：%是，今年%d岁了'%(name,age)
        2. {}作为占位符
                '我的名字叫：{0}，今年{1}岁了，我真的叫{0}'.format(name,age)
        3. f-string
                f'我叫{name}，今年{age}岁了'

    宽度和精度的两种设置方法
        1. %作为占位符
            %s  字符串
            %d  有符号十进制整数
            %x  十六进制整数
            %u  无符号整形
            %c  格式化字符
            %f  浮点数
                %06d    输出6位整数，不足的地方使用0补全
                %10d    设置宽度为10的整数
                %10.3f  设置宽度为10，精度为3位小数的浮点数
        2. {}作为占位符
                {:.3}format(3.1415926)和{0:.3}format(3.1415926)一样            0表示占位符的顺序
                {0:.3}.format(3.1415926)                                      设置精度为3位数
                {0:.3f}.format(3.1415926)                                     设置精度为3位小数的浮点数
                {0:10.3f}.format(3.1415926)                                   设置宽度为10，精度为3位小数的浮点数
    设置输出长度
        {:^num}。format(str)            将str输出为num个字节长度
                                        如果str长度大于num，则输出原str
'''
name = '张三'
age = 20
# %
print('我的名字叫：%s，今年%d岁了' % (name, age))
print('我的名字叫：%s，今年%d岁了%%' % (name, age))
# {}
print('我的名字叫：{0}，今年{1}岁了，我真的叫{0}'.format(name, age))
# f-string
print(f'我叫{name}，今年{age}岁了')
print()

# % 设置宽度精度
print('hallohallo')
print('%10d' % 99)
print('%10.3f' % 3.1415926)
print('%010.3f' % 3.1415926)
print()

# {} 设置宽度精度
print('hallohallo')
print('{:.3}'.format(3.1415926))
print('{0:10.3}'.format(3.1415926))
print('{0:.3f}'.format(3.1415926))
print('{0:10.3f}'.format(3.1415926))
print()
# {} 设置长度
format_print = '{:^6}{:^6}{:^6}{:^6}{:^6}{:^6}{:^6}'
print(format_print.format(str(1), str(12), str(123), str(1234), str(12345), str(123456), str(1234567)))

'''
字符串的编码转换
    为什么需要编码转换
        str在内存中以Unicode表示，编码只用使用byte字节传输，经过解码在另一台计算机上显示
    编码与解码的方式
        编码：将字符串转化为二进制数据(bytes)
        解码：将bytes类型数据转化乘字符串类型
    注意： 编码形式要与解码形式相同
'''
print(b'asasas')    # bytes can only contain ASCII literal characters.
print(type(b'asasa'))

s = '天涯共此时'

# 编码
print(s.encode(encoding='GBK',errors='ignore'))  # 在GBK这种编码中 一个中文占两个字节
print(s.encode(encoding='UTF-8',errors='ignore'))  # 在GBK这种编码中 一个中文占三个字节
# 解码
byte = s.encode(encoding='GBK',errors='ignore')         # errors=设置遇到错误时的处理方法
print(byte.decode(encoding='GBK',errors='ignore'))      # 默认为strict：报错终止程序      ignore：无视错误执行程序

byte = s.encode(encoding='UTF-8',errors='ignore')
print(byte.decode(encoding='UTF-8',errors='ignore'))
print()

"""
字符串的遍历
"""
str1 = 'Python'
for char in str1:
    print(char)
print()

'''
统计字符串中字符出现的次数
'''


def get_count(s, ch):
    count = 0
    for item in s:
        if ch.upper() == item or ch.lower() == item:
            count += 1
    return count


s = 'dgjdgfasfahsahjgsgjhahgsaj'
print(get_count(s, 'a'))
print()
