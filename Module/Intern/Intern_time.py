# Programmed by Scar
"""
time模块:
    事件处理，转换时间格式
    time        生成时间戳函数
    localtime   或取本地时间函数
    sleep       暂停函数
    strftime    将时间对象转化成时间字符串
    strptime    将字符串转化成时间对象

时间戳：
    1970年01月01日00时00分00秒至今的总毫秒（秒）数
    timestamp或取时间戳
    float数据类型

localtime对应字段介绍：
    tm_year     四位数年（2020）
    tm_mon      月（01~12）
    tm_mday     日（01~31）
    tm_hour     小时（00~23）
    tm_min      分钟（00~59）
    tm_sec      秒（00~61）闰月
    tm_wday     一周第几天（0~6，0是周一）
    tm_yday     一年第几日（1~366，儒略历）
    tm_isdst    夏令时（-1，0，1）
"""
import time

# 或取本地时间函数
now = time.time()
print(now, type(now))
print()

# 将时间戳转化为可读模式
time_obj = time.localtime(now)
print(time_obj, type(time_obj))
time.sleep(5)
print()

# 或取本地时间函数
current_time_obj = time.localtime()
print(current_time_obj, type(current_time_obj))
print()

# 读取一段时间之前的时间戳
before = now - 100000  # 100000秒
before_time_obj = time.localtime(before)
print(before_time_obj, type(before_time_obj))
print()

# 返回毫秒级时间戳
print(time.time() * 1000)
print(time.time())
print()

# 暂停函数
for i in range(5):
    print(i)
    time.sleep(1)  # 暂停1秒
print()

# 时间对象转化为字符串
date = time.time()
str_date = time.strftime("%Y-%m-%d %H:%M:%S")
print(str_date, type(str_date))
print()

# 时间字符串转化为事件类型
str_date = "2021-10-10 13:13:13"
date_obj = time.strptime(str_date, "%Y-%m-%d %H:%M:%S")
print(date_obj, type(date_obj))
print()
