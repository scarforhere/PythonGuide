# Programmed by Scar
# 单分支结构         if
money = 1000
s = int(input("How much do you wanna to get out："))
if money >= s:
    money -= s
    print('Succeed   Rest of Account is：', money)
print()

# 双分支结构         if...else
num = int(input("请输入一个整数"))
if num % 2 == 0:
    print(num, "是偶数")
else:
    print(num, "是奇数")
print()

# 多分支结构
"""
输入成绩并进行分级
    90-100  A
    80-89   B
    70-79   C
    60-69   D
    0-59    E
    小于0   非法数据(超出成绩范围)
    大于100 非法数据(超出成绩范围)
"""
score = int(input("请输入成绩："))
if 90 <= score <= 100:
    print("A级")
if 80 <= score <= 89:
    print("B级")
if 70 <= score <= 79:
    print("C级")
if 60 <= score <= 69:
    print("D级")
if 0 <= score <= 59:
    print("E级")
else:
    print("非法数据！")
print()

# 嵌套if结构
"""
    会员  >=200    8折
         >=100    9折
         不打折
    非会员 >=200   9.5折
          不打折
"""
answer = input("您是会员么 Y/N：")
money = float(input("请输入您的购物金额:"))
if answer == "Y":
    if money >= 200:
        print("打8折，付款金额为：", money * 0.8)
    elif money >= 100:
        print("打9折，付款金额为：", money * 0.9)
    else:
        print("不打折，付款金额为：", money)
else:
    if money >= 200:
        print("打8折，付款金额为：", money * 0.95)
    else:
        print("不打折，付款金额为：", money)
print()

"""
条件判断表达式  if...else
若结果为True，执行左侧表达式
若结果为False，执行右侧表达式
"""
num_a = int(input("请输入第一个整数"))
num_b = int(input("请输入第二个整数"))
print(str(num_a) + "大于等于" + str(num_b) if num_a >= num_b else str(num_a) + "小于" + str(num_b))

"""
Pass语句
语句什么也不做，只是一个占位符，用在语法上需要语句的地方
什么时候使用：
    先搭建语法结构，还没想好代码怎么写
哪些语句一起使用：、
    if语句的条件执行体
    for_in语句的循环体
    定义函时的函数体
"""
answer = input("您是会员么 Y/N：")
money = float(input("请输入您的购物金额:"))
if answer == "Y":
    pass            # 使语法不报错
else:
    pass
print()