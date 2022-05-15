# Programmed by Scar
"""
rang()函数用于生成一个整数数列
range(stop)
range(start,stop)
range(start,stop,step)
range()函数优点：不管整数序列有多长，所有range对象占用内存空间都是相同的，仅储存star，stop和step三个参数
"""
# 第一种创建方式：只有一个参数
r = range(10)  # 默认从0开始，走10步，默认步长为1
print(r)  # range(0,10)
print(list(r))  # 用于查看range()中的参数序列         -->list是列表
print()

# 第二种创建方式，两个参数：指定初始值和结束值(不包含结束值)
r = range(1, 10)  # 从1开始，走到10的前一步，默认步长为1
print(list(r))
print()

# 第三种创建方式，三个参数：指定初始值、结束值(不包含结束值)和步长
r = range(1, 10, 2)  # 从1开始，走到10的前一步，默认步长为1
print(list(r))
print()

# 倒着取值
r = range(10, 0, -1)  # 从1开始，走到10的前一步，默认步长为1
print(list(r))
print()


"""
判断指定整数是否在整数序列中存在
使用 in
使用 not in
"""
print(10 in r)
print(9 in r)
print(10 not in r)
print(9 not in r)
