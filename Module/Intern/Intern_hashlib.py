# Programmed by Scar
"""
hashlib模块：
    对信息进行加密
    难破解
    不可逆
常用方法：
    hashlib.md5(b' hello')      MD5算法加密返回Hash对象
    hashlib.sha1(b' hello')     Sha1算法加密返回Hash对象
    hashlib.sha256(b' hello')   Sha256算法加密返回Hash对象
    hashlib.sha512(b' hello')   Sha512算法加密返回Hash对象
注意：传入参数都为Byte
"""
import hashlib
import time

base_sign = 'Scar'


def custom():
    a_timestamp = int(time.time())
    _token = f"{base_sign},{a_timestamp}"
    # 进行加密
    hash_obj = hashlib.sha1(_token.encode("utf-8"))
    a_token = hash_obj.hexdigest()
    return a_token, a_timestamp


def service_check(token, timestamp):
    _token = f"{base_sign},{timestamp}"
    hash_obj = hashlib.sha1(_token.encode("utf-8"))
    b_token = hash_obj.hexdigest()
    if token == b_token:
        return True
    else:
        return False


if __name__ == '__main__':
    need_help_tokeen, timestamp = custom()
    result = service_check(need_help_tokeen, timestamp)
    if result == True:
        print("a合法，b服务可以进行帮助")
    else:
        print("a不合法，b不可以进行帮助")
    print()

    need_help_tokeen, timestamp = custom()
    time.sleep(1)
    result = service_check(need_help_tokeen, time.time())
    if result == True:
        print("a合法，b服务可以进行帮助")
    else:
        print("a不合法，b不可以进行帮助")
