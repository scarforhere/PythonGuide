# Programmed by Scar
"""
datetime模块：
    datetime或                   取当前时间
    timedelta                   或取区时间间隔
    strftime                    将时间对象转化成时间字符串
    strptime                    将 字符串转化成时间对象
    timestamp(time)             转化时间类型为时间戳
    fromtimestamp(timestamp)    将时间按戳转化为时间类型

时间格式符：
    %Y  完成的年份，如2020
    %m  月份（1~12）
    %d  月份中的某一天（01~31）
    %H  一天中的第几个小时（24小时制，00~23）
    %I  一天中的第几个小时（12小时制，01~23）
    %M  当前的第几分（00~89）
    %S  当前的第几秒（00~61）闰年多占2秒
    %f  当前的第几毫秒
    %a  简化的星期（Wed）
    %A  完整的星期（Wednesday）
    %b  简化的月份（Feb）
    %B  完整的月份（February）
    %c  本地时间和日期（Wen Feb 5 10：14：49 2020）
    %p  显示上午或下午（AM，PM）
    %j  一年中的第几天
    %U  一年中的第几周
"""
# 或取当前时间
import datetime

time = datetime.datetime.now()
print(time, type(time))
print()

# 或取区时间间隔
from datetime import datetime
from datetime import timedelta

# 对时间对象进行操作
# timeobj = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
before_one_day = timedelta(days=1)
yestoday = datetime.now() - before_one_day
print(yestoday)
after_three_hours = timedelta(hours=3)
later = datetime.now() + after_three_hours
print(later)
print()

# 时间对象转化为字符串
date = datetime.now()
str_date = date.strftime("%Y-%m-%d %H:%M:%S")
print(str_date, type(str_date))
print()

# 时间字符串转化为事件类型
str_date = "2021-10-10 13:13:13"
date_obj = datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")
print(date_obj, type(date_obj))
print()

# 转化事件类型time为时间戳
now = datetime.now()
now_timestamp = datetime.timestamp(now)
print(now_timestamp)
print()

# 将时间按戳转化为时间类型
fatetime_obj = datetime.fromtimestamp(now_timestamp)
print(date_obj)
print()
