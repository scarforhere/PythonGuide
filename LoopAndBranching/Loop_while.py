# Programmed by Scar
"""
while 循环
四步循环法：
    1. 初始化变量
    2. 条件判断
    3. 条件执行体（循环体）
    4. 条件执行体
    总结：初始化变量与条件判断的变量与改变变量为同一个
"""
# 初始化变量
sum = 0
a = 0
# 条件判断
while a < 5:
    # 条件执行体
    sum += a
    # 条件执行体
    a += 1
print("和为：", sum)
print()

"""
使用while循环计算0-100的偶数和
"""
sum = 0
a = 1
while a <= 100:
    if not bool(a % 2):  # if a%2==0:
        sum += a
    a += 1
print("0-100的偶数和为：", sum)
