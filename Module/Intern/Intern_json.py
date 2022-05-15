# Programmed by Scar
"""
json模块：
    通用序列化模块
    序列化与反序列化的规则是统一的\

注意：json无法将转化后数据识别为元组

具体操作函数：
    json.dumps([1,2])       将对象序列化并返回字符串
    json.loads('[1,2,3]')   将字符串进行反序列化返回原始数据类型
"""
import json

test = [0 for i in range(8)]
test_json = [0 for i in range(8)]
test_load = [0 for i in range(8)]

test[0] = 1
test[1] = 'str'
test[2] = [1, 2, 3]
test[3] = (4, 5, 6)
test[4] = {'name': 'Scar'}
test[5] = True
test[6] = False
test[7] = None

# 将对象序列化并返回字符串
for i in range(0, 8):
    test_json[i] = json.dumps(test[i])
    print(f"转换后的返回值：{test_json[i]}\n转换后的数据类型：{type(test_json[i])}\n")
print("*" * 50)
print()

# 将字符串进行反序列化返回原始数据类型
for i in range(0, 8):
    test_load[i] = json.loads(test_json[i])
    print(f"转换后的返回值：{test_load[i]}\n转换后的数据类型：{type(test_load[i])}\n")
print()
