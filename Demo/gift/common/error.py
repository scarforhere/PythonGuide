# coding: utf-8
"""
-------------------------------------------------
   File Name：     error
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-06 09:42 AM
-------------------------------------------------
Description : 

    

"""


class NotPathError(Exception):
    def __init__(self, message):
        self.message = message


class FormatError(Exception):
    def __init__(self, message):
        self.message = message


class NotFileError(Exception):
    def __init__(self, message):
        self.message = message


class UserExistsError(Exception):
    def __init__(self, message):
        self.message = message


class RoleError(Exception):
    def __init__(self, message):
        self.message = message


class LevelError(Exception):
    def __init__(self, message):
        self.message = message


class NegativeNumerError(Exception):
    def __init__(self, message):
        self.message = message


class NotUserError(Exception):
    def __init__(self, message):
        self.message = message


class UserActiveError(Exception):
    def __init__(self, message):
        self.message = message


class CountError(Exception):
    def __init__(self, message):
        self.message = message
