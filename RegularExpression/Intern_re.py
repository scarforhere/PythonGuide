# coding: utf-8
"""
-------------------------------------------------
   File Name：     Intern_re
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-05 11:28 PM
-------------------------------------------------
Description : 

    正则表达式模块 re

    常用方法：
        findall(pattern, string [, flags])  查找字符串中所有非重复出现的正则表达式模式，并返回结果

        searchall(pattern, string, flags)   使用可选标记搜索字符串中第一次出现的正则表达式模式。
                                            如果成功，则返回匹配对象
                                            如果失败，则返回None

        group(num)  返回整个匹配对象，或编号为num的特定子组

        grupps()    返回一个包含所有匹配组的元组（如果没有匹配成功，则返回一个空元组）

        split(pattern, string, max=0)   根据正则表达式的模式分隔符，split函数将字符串分割为列表，然后返回成功匹配的泪飙，
                                        分割最多操作max次（默认分割所有匹配成功的位置）

        compile(pattern, flags=0)   定义一个匹配规则的对象

        match(pattern, string, flags=0)     尝试使用带有可选标记的正则表达式的模式来匹配字符串。
                                            如果成功，返回匹配对象
                                            如果失败，返回None

    re的额外匹配要求
                属性                                  描述
        re.I --> re.IGNORECASE      不区分大小写的匹配
        re.L --> re.LOCALE          根据所以用的本地语言环境通过\w,\W,\s,\S实现匹配
        re.M --> re.MULTILINE       ^和￥分别匹配目标字符串中行的起始和结尾，而不是严格匹配整个字符串本身的起始和结尾
        re.S --> re.DOTALL          “.”(点好)通常匹配除了\n(换行符)之外的所有单个字符
                                    该标记表示'.'(点号)能够匹配全部字符
        re.X --> re.VERBOSE         忽略正则表达式中的空白和注释

"""
import re

url = r'https://www.google.com'


def check_url(url):
    re_g=re.compile('[a-zA-Z]{1,2}://\w*\.*\w+\.\w+')
    result = re.findall(re_g, url)
    print(result)
    if len(result) != 0:
        return True
    else:
        return False


print(check_url(url))


def get_url(url):
    re_g=re.compile('[https://|http://](\w*\.*\w+\.\w+)')
    result = re.findall(re_g, url)
    if len(result) != 0:
        return result[0]
    else:
        return ''


print(get_url(url))


email='scarforhere@gmail.com'

def geg_email(data):
    re_g=re.compile('[0-9a-zA-Z_]+@[0-9a-zA-Z]+\.[a-zA-Z]+')
    re_g= re.compile(re_g)
    result=re.findall(re_g,data)
    # 等效于 '.+@.+\.[a-zA-Z]+'
    return result

print(geg_email(email))


html = ('<dim class="s-top-nav" style="display:none;">'
        '</div><div class="s-center-box"></div>')

def get_html_data(data):
    re_g=re.compile('style="(.*?)"')
    result = re.findall(re_g,data)
    return result

print(get_html_data(html))

def get_all_data_html(data):
    re_g=re.compile('="(.*?)"')
    result = re.findall(re_g,data)
    return result
print(get_all_data_html(html))


re_g=re.compile('<dim class="(.*?)" style="(.*?)">'
        '</div><div class="(.*?)"')
result = re_g.search(html)
print(result.groups())

re_g=re.compile('\s')
result = re_g.split(html)
print(result)

re_g=re.compile('<dim class="(.*?)')
result = re_g.match(html)
if result is None:
    print('aaaa')
else:
    print('1111')
print(result)
print(result.group())
print(html[0:12])
