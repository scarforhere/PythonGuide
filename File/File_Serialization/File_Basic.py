# Programmed by Scar
"""
序列化：
    将对象信息或数据结构信息通过转化达到存储或网络传输的效果
    在存储和传输过程中被传递的是有一定规格的字符串
    example： encode()

反序列化：
    将存储和传输过程中的据有一定规格的字符串解码为刻度字符串
    example： decode()

可以序列化的数据类型：
    number
    str
    list
    tuple
    dict

注意：
    类，函数，元组是无法进行序列化的

Python中序列化模块
    jason模块
"""
import json


def read(path):
    with open(path, "r") as f:
        data = f.read()
    return json.loads(data)


def write(path, data):
    with open(path, 'w') as f:
        if isinstance(data, dict):
            _data = json.dumps(data)
            f.write(_data)
        else:
            raise TypeError("Data should be dict")
    return True


data = {'name': "张三", "age": 24}

if __name__ == '__main__':
    write("Test.json", data)
    result = read("Test.json")
    print(result)
