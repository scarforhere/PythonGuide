# coding: utf-8
"""
-------------------------------------------------
   File Name：     utils
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-06 09:42 AM
-------------------------------------------------
Description : 

    

"""
import os
import time
from Demo.gift.common.error import NotPathError, FormatError, NotFileError


def check_file(path):
    if not os.path.exists(path):
        raise NotPathError(f'not found {path}')

    if not path.endswith('.json'):
        raise FormatError('need json format')

    if not os.path.isfile(path):
        raise NotFileError('this is not a file')


def timestamp_to_string(timestamp):
    time_obj = time.localtime(timestamp)
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time_obj)
    return time_str
