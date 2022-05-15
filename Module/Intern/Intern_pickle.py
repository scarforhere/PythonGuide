# Programmed by Scar
"""
pickle模块：
    Python的转悠序列化模块

具体操作函数：
    pickle.dumps([1,2])         将对象序列化并返回比特值
    pickle.loads('[1,2,3]')     将比特质进行反序列化返回原始数据类型
"""
import pickle
import json

test = [0 for i in range(8)]
test_pickle = [0 for i in range(8)]
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
    test_pickle[i] = pickle.dumps(test[i])
    print(f"转换后的返回值：{test_pickle[i]}\n转换后的数据类型：{type(test_pickle[i])}\n")
print("*" * 50)
print()

# 将字符串进行反序列化返回原始数据类型
for i in range(0, 8):
    test_load[i] = pickle.loads(test_pickle[i])
    print(f"转换后的返回值：{test_load[i]}\n转换后的数据类型：{type(test_load[i])}\n")
print()
