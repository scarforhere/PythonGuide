# Programmed by Scar
# continue:用于结束当前循环，进入下一个循环
# 搭配if使用在嵌套结构中
"""
    要求输出1到50之间所有5的倍数
    共同点：和5的余数为0
"""
for item in range(2, 51):
    if item % 5 == 0:
        print(item)
print("\n")

for item in range(2, 51):
    if item % 5 != 0:
        continue
    print(item)
print("\n")
