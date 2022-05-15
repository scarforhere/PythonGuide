# Programmed by Scar
"""
base64模块：
    通用
    可解密
常用方法：
    base62.encodestring(b'py')      进行base64加密返回Byte
    base62.decodestring(b'py')      进行base64加密返回Byte
    base62.encodebytes(b'py')       进行base64加密返回Byte
    base62.decodebytes(b'py')       进行base64加密返回Byte
注意：传入参数都为Byte
"""
import base64

replace_one = "%"
replace_two = "$"


def encode(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif isinstance(data, bytes):
        data = data
    else:
        raise TypeError("Data need to be Bytes or string")
    _data = base64.encodebytes(data).decode('utf-8')

    return _data.replace('a', replace_one).replace('2', replace_two)


def decode(data):
    replace_one_b = replace_one.encode("utf-8")
    replace_two_b = replace_two.encode("utf-8")

    if not isinstance(data, bytes):
        raise TypeError("Data need to be Bytes")

    _data = data.replace(replace_one_b, b'a').replace(replace_two_b, b'2')

    return base64.decodebytes(_data).decode("utf-8")


if __name__ == '__main__':
    result = encode("Scar")
    print(result)

    new_result = decode(result.encode('utf-8'))
    print(new_result)
