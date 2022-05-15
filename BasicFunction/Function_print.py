# Programmed by Scar
# 输出数字
import random

print(20)

# 输出字符串
print("Hallo the World")
print('Hallo the World')

# 输出含有运算符的表达式
print(5 + 6)

# 输出数据到文件
fp = open('E:/Die Schulfach im TUD/Python/text.txt', 'a+')  # a+: 读写形式打开文件，没有文件进行创建，有文件在原有文件上添加
print("hallo the world", "what a nice day", "need to go", file=fp)  # 不进行换行输出
fp.close()
# 注意点：指定盘符存在，使用file=fp

for i in range(1, 4):
    for j in range(1, 5):
        print("*", end="\t")  # 不换行输出，以空格结尾
    print()  # 换行

for i in range(1, 4):
    for j in range(1, 5):
        print("*", end="")  # 不换行连续输出
    print()  # 换行

"""
条件判断表达式  if...else
若结果为True，执行左侧表达式
若结果为False，执行右侧表达式
"""
num_a = int(input("请输入第一个整数"))
num_b = int(input("请输入第二个整数"))
print(str(num_a) + "大于等于" + str(num_b) if num_a >= num_b else str(num_a) + "小于" + str(num_b))
print()

