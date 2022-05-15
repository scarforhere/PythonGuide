# coding: utf-8
"""
-------------------------------------------------
   File Name：     RE_mode
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-05 10:55 PM
-------------------------------------------------
Description : 

    0次或多次属于贪婪模式
    通过？组合变成非贪婪模式

"""
import re

url = r'https://www.google.com'


def check_url(url):
    result = re.findall('[a-zA-Z]{4,5}://\w*\.*\w+\.\w+', url)
    if len(result) != 0:
        return True
    else:
        return False


print(check_url(url))


def get_url(url):
    result = re.findall('[https://|http://](\w*\.*\w+\.\w+)', url)
    if len(result) != 0:
        return result[0]
    else:
        return ''


print(get_url(url))


email='scarforhere@gmail.com'

def geg_email(data):
    result=re.findall('[0-9a-zA-Z_]+@[0-9a-zA-Z]+\.[a-zA-Z]+',data)
    # 等效于 '.+@.+\.[a-zA-Z]+'
    return result

print(geg_email(email))


html = ('<dim class="s-top-nav" style="display:none;">'
        '</div><div class="s-center-box"></div>')

def get_html_data(data):
    result = re.findall('style="(.*?)"',data)
    return result

print(get_html_data(html))

def get_all_data_html(data):
    result = re.findall('="(.*?)"',data)
    return result
print(get_all_data_html(html))