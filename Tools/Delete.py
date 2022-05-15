# coding: utf-8
"""
-------------------------------------------------
   File Name：     Delete_new.py
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-02 05:22 PM
-------------------------------------------------
Description : 

    Delete by program created files\n
    Delete.execute() first time for record (create 'Record.txt')\n
    Delete.execute() later for reset the folder back to the record time point\n
    "Reload from disk" to check by program created new files and folders\n\n

    Delete Record.txt to reset record time point\n\n

    Usage:
        Begin of code:
            import Delete\n
            import os\n
            dir_path = r'E:\Python_Code\Piggy\DataSource\'\n
            os.chdir(dir_path)\n

        End of Code:
            input("Press Enter To Delete")\n
            Delete.execute(path=os.getcwd())\n

"""
import os
import shutil
import json
from TimeRecord import TimeMonitor

g_mode = False


def record_data(path):
    """
    Record source files
    """
    t = TimeMonitor('Record Time', 25)

    file_datasource_path = path

    name_txt = 'Record.txt'
    path_full = ''.join([file_datasource_path, '\\', name_txt])

    with open(path_full, 'w'):
        pass

    files_walk_list = os.walk(file_datasource_path)

    # Put all folders and files into a List
    files_list = []

    for dirpath, dirname, filename in files_walk_list:
        for item in filename:
            file_origin_path = ''.join([dirpath, '\\', item])
            files_list.append(file_origin_path)
        for item in dirname:
            dir_origin_path = ''.join([dirpath, '\\', item])
            files_list.append(dir_origin_path)

    # Write List  in json Type into Record.txt
    json_write(path_full, files_list)
    if __name__ == '__main__':
        t.show()

        print('\n')
        print('------------------------------')
        print("Record Succeeded!".center(30))
        print('------------------------------')


def delete_data(path):
    """
    Delete by program created files
    """
    t = TimeMonitor('Delete Time', 25)

    file_datasource_path = path

    name_txt = 'Record.txt'
    path_full = ''.join([file_datasource_path, '\\', name_txt])

    # Read List from Record.txt in json Type
    # Convert it to Set Type
    file_origin_set = json_read(path_full)

    # Put all folders and files into a List
    files_walk_list = os.walk(file_datasource_path)
    files_list = []

    for dirpath, dirname, filename in files_walk_list:
        for item in filename:
            file_origin_path = ''.join([dirpath, '\\', item])
            files_list.append(file_origin_path)
        for item in dirname:
            dir_origin_path = ''.join([dirpath, '\\', item])
            files_list.append(dir_origin_path)

    file_now_set = set(files_list)

    # Get Set of by program created files and folders
    file_new_set = file_now_set.difference(file_origin_set)

    for item in file_new_set:
        # Avoid files in already deleted folders
        try:
            # Avoid files in ...\.git denied delete action
            if item.count('.git') != 0:
                continue
            elif os.path.isdir(item):
                shutil.rmtree(item)
            else:
                os.remove(item)

            if __name__ == '__main__':
                print(f'Delete Succeeded: {item}')
            else:
                print(f'\tDelete Succeeded: {item}')
        except FileNotFoundError:
            continue

    if __name__ == '__main__':
        t.show()

        print('\n')
        print('------------------------------')
        print("Delete Succeeded!".center(30))
        print('------------------------------')


def json_write(path, data):
    """
    Write list data in to txt with json format

    :param path: Full path of txt
    :param data: Data in List type
    :return: True --> WriteIn Seccessed!
    """
    with open(path, 'w') as f:

        if isinstance(data, list):
            _data = json.dumps(data)
            f.write(_data)

            if __name__ == '__main__':
                print("WriteIn Succeeded!")

        else:
            if __name__ == '__main__':
                print("WriteIn Failed!")

            raise TypeError("Data should be list")

    return True


def json_read(path):
    """
    Read a txt with json format

    :param path: Full path of txt
    :return: Data from txt in origin type
    """
    with open(path, "r") as f:
        data = f.read()
    return json.loads(data)


# noinspection PyGlobalUndefined
def execute(path=None):
    """
    Delete.execute() first time for set a record time point (create 'Record.txt')\n
    Delete.execute() later for reset the folder back to the record time point.\n

    Delete Record.txt to reset record time point.

    :param path: Path of program worked on File
    """
    global g_mode
    if not path:
        path = os.getcwd()

    dlist = os.listdir(path)
    for item in dlist:
        if item == 'Record.txt':
            g_mode = True
            break
        else:
            g_mode = False

    if g_mode:
        delete_data(path)

    else:
        record_data(path)


def main():
    execute()


if __name__ == '__main__':
    main()
