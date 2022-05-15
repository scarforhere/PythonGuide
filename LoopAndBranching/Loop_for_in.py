# Programmed by Scar
# for-in 循环遍历
for item in "Python":
    print(item)
print("\n")

# range() 产生一个整数序列，可迭代对象
for i in range(10):
    print(i)
print("\n")

# 如果在循环体中不需要使用到自定义变量可用，可将自定义变量写为"_"
for _ in range(5):
    print("Hallo the World")
print("\n")

print("使用for循环，计算1到00的偶数和")
sum = 0
for item in range(1, 101):
    if item % 2 == 0:
        sum += item
print("1到100的偶数和为：", sum)
print("\n")

"""
    输出100 到999之间的水仙花数
    举例： 
            153=3*3*3+5*5*5+1*1*1  
"""
for item in range(100, 1000):
    ge = item % 10  # 个位数
    shi = item // 10 % 10  # 十位数
    bai = item // 100  # 百位数
    # print(bai,shi,ge)
    # 判断
    if bai ** 3 + shi ** 3 + ge ** 3 == item:
        print("这个数是水仙花数:", item)
print("\n")

