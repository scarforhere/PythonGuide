# Programmed by Scar
# break:用于结束嵌套结构
# 搭配if使用在嵌套结构中
"""
    输入密码
    3此输入机会
    如果正确退出嵌套
"""
for item in range(3):
    PassW = input("Password:")
    if PassW == "888":
        print("Correct Password!")
        break
    else:
        print("Wrong Password!")
print("\n")

a = 0
while a < 3:
    PassW = input("Password:")
    if PassW == "888":
        print("Correct Password!")
        break
    else:
        print("Wrong Password!")
    a += 1
print("\n")
