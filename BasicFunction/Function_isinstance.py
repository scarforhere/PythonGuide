# Programmed by Scar
"""
isinstance(data,type)可以判断data内存储的数据的类型是否是type类型
如果一致返回True
如果不一致返回False
"""
data = [10, 20, 30]

if isinstance(data, int):
    print(f"Type of data is: int")
elif isinstance(data, float):
    print(f"Type of data is: float")
elif isinstance(data, bool):
    print(f"Type of data is: bool")
elif isinstance(data, list):
    print(f"Type of data is: list")
elif isinstance(data, str):
    print(f"Type of data is: str")
elif isinstance(data, tuple):
    print(f"Type of data is: tuple")
elif isinstance(data, dict):
    print(f"Type of data is: dict")
elif isinstance(data, set):
    print(f"Type of data is: set")
else:
    print("Cannot be recognized!")
