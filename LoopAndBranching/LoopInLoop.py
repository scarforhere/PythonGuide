# Programmed by Scar
"""
输出一个三行四列的矩形
"""
for i in range(1, 4):
    for j in range(1, 5):
        print("*", end="\t")
    print()  # 换行
print()

"""
打九行直角三角形
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print("*", end="\t")
    print()  # 换行
print()

"""
打九九乘法表
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, "*", j, "=", i * j, end="\t")
    print()  # 换行
print()

"""
流程控制语句break和continue在二重循环中的使用
break只影响1层循环
"""
for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            break
        print(j)
print()

for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            # break
            continue
        print(j, end="\t")
    print()
print()
