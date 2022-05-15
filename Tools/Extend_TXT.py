# coding: utf-8
"""
-------------------------------------------------
   File Name:      Extend_TXT
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-06-26 09:36 PM
-------------------------------------------------
Description : 

    Add .txt in the end of the file

"""
import os


def test():
    path = os.getcwd()
    files_walk_list = os.walk(path)

    # Put all folders and files into a List
    for dirpath, dirname, filename in files_walk_list:
        for item in filename:
            file_origin_path = ''.join([dirpath, '\\', item])
            file_new_path = ''.join([dirpath, '\\', item, '.txt'])

            with open(file_origin_path, 'rb') as fr:
                with open(file_new_path, 'wb') as fw:
                    fw.write(fr.read())

            os.remove(file_origin_path)
            print(f'Rename Succeeded: {file_origin_path}')

    print('\n')
    print('------------------------------')
    print("Rename Succeeded!".center(30))
    print('------------------------------')


if __name__ == '__main__':
    _path = r'E:\Python_Code\Tu\Data\Menze'
    os.chdir(_path)
    test()
