# Programmed by Scar
# else 可在if，while，for循环嵌套中使用
# 在while和for中，执行完条件就执行else
for item in range(3):
    PassW = input("Password:")
    if PassW == "888":
        print("Correct Password!")
        break
    else:
        print("Wrong Password!")
else:   # 当主循环体被break退出执行时，else的语句不会被执行
    print("3 times wrong input!")
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
else:
    print("3 times wrong input!")
print("\n")
