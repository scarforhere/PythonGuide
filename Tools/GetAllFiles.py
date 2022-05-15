# coding: utf-8
"""
-------------------------------------------------
   File Name：     get_all_files
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-04 11:42 PM
-------------------------------------------------
Description :

    Get all file path

"""
import os


def get_all_files(path, fileType=''):
    """
    Get all file path in target folder

    :param path: Path of target folder
    :param fileType: Filetype to be checked
    :return: List of path and name of Files
    """
    os.chdir(path)

    lst = []

    fileAppendix = ''.join(['.', fileType])

    file_list = os.walk(path)

    for dirpath, dirname, filename in file_list:
        for filename_item in filename:
            if filename_item.endswith(fileAppendix) or fileType == '':
                path_full = "".join([dirpath, '\\', filename_item])
                lst.append(path_full)
            else:
                continue
    return lst


def get_all_csv(path):
    """
    Get all file path in target folder

    :param path: Path of target folder
    :return: List of all target .CSV
    """
    os.chdir(path)

    lst = []

    file_list = os.walk(path)

    for dirpath, dirname, filename in file_list:
        for filename_item in filename:
            if filename_item.endswith(".csv"):
                path_full = "".join([dirpath, '\\', filename_item])
                lst.append(path_full)
            else:
                continue
    return lst
