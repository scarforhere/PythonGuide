# coding: utf-8
"""
-------------------------------------------------
   File Name:      Delete_TXT
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-06-28 11:14 PM
-------------------------------------------------
Description : 

    Delete all .txt files in target folders

"""
import os

path = os.getcwd()
files_walk_list = os.walk(path)

# Put all folders and files into a List
files_list = []

for dirpath, dirname, filename in files_walk_list:
    for item in filename:
        if item.endswith('.txt') or item.endswith('.TXT'):
            file_origin_path = ''.join([dirpath, '\\', item])

            os.remove(file_origin_path)
            print(f'Delete Succeeded: {file_origin_path}')

print('\n')
print('------------------------------')
print("Delete Succeeded!".center(30))
print('------------------------------')
