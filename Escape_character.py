# Programmed by Scar
print("hallo\nworld")  # \n 换行
print("hallo\tworld")  # \t 一组4个空格 = TAB 键
print("hallo\bworld")  # \b 退格
print("hallo\rworld")  # \r 回车 return光标至本行开头
print("hallo\vworld")  # \v 纵向制表符
print("hallo\aworld")  # \a 响铃
print("http:\\\\www.baidu.com") # \\ 反斜杠
print("Teacher says \' Guten morgen\'") # \' 单引号

# 原字符：不希望字符串中的转义字符起作用，使用原字符
# 在字符串前加r或R
print(r"hello\nworld")
print(r"http:\\www.baidu.com")
print(r"Teacher says 'Guten morgen'")
# 注意：最后一个字符不能是反斜线
# Wrong：
# print(r"hello\nworld\")
