# coding: utf-8
"""
-------------------------------------------------
   Project :       Tu
   File Name :     Delete_PNG
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-13 09:40 AM
-------------------------------------------------
Description : 

    Delete all .png files in target folders

"""
import os

path = os.getcwd()
files_walk_list = os.walk(path)

# Put all folders and files into a List
files_list = []

for dirpath, dirname, filename in files_walk_list:
    for item in filename:
        if item.endswith('.png') or item.endswith('.PNG'):
            file_origin_path = ''.join([dirpath, '\\', item])

            os.remove(file_origin_path)
            print(f'Delete Succeeded: {file_origin_path}')

print('\n')
print('------------------------------')
print("Delete Succeeded!".center(30))
print('------------------------------')
