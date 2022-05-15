# Programmed by Scar
'''
os.path模块
操作目录相关函数：
    abspath(path)       用于或取文件或目录的绝对路径
    exists(path)        用于判断文件或目录是否存在，富国存在返回True，否则返回False
    split()             拆分文件路径和文件名
    join(path,name)     将目录与目录或者文件名拼接起来
    splittext()         分离文件们和扩展名
    basename(path)      从一个目录中提取文件名
    dirname(path)       从一个路径中提取文件路径，不包阔文件名
    isdir(path)         用于判断是否是路径
    isabs(path)         判断是否是绝对路径
    isfile(path)        判断文件是否存在
'''
import os.path

# 于或取文件或目录的绝对路径
print(os.path.abspath('demo2.py'))
print()

# 用于判断文件或目录是否存在，富国存在返回True，否则返回False
print(os.path.exists('demo2.py'), os.path.exists('demo3.py'))
print()

# 将目录与目录或者文件名拼接起来
print(os.path.join('/', 'demo12.py'))
print()

# 拆分文件路径和文件名
print(os.path.split('E:\\Die Schulfach im TUD\\Python\\PycharmProjects\pythonProject\\demo3.py'))
print()

# 分离文件名和扩展名
print(os.path.splitext('demo3.py'))
print()

# 从一个目录中提取文件名
print(os.path.basename('E:\\Die Schulfach im TUD\\Python\\PycharmProjects\pythonProject\\demo3.py'))
print()

# 从一个路径中提取文件路径，不包阔文件名
print(os.path.dirname('E:\\Die Schulfach im TUD\\Python\\PycharmProjects\pythonProject\\demo3.py'))
print()

# 用于判断是否是路径
print(os.path.isdir('E:\\Die Schulfach im TUD\\Python\\PycharmProjects\pythonProject\\demo3.py'))
print(os.path.isdir('/'))
print()

# 用于判断是否是绝对路径
print(os.path.isdir('E:\\Die Schulfach im TUD\\Python\\PycharmProjects\pythonProject'))
print(os.path.isdir('Die Schulfach im TUD\\Python\\PycharmProjects\pythonProject'))
print()

# 判断文件是否存在
print(os.path.isfile('E:\Die Schulfach im TUD\Python\PycharmProjects\pythonProject\Module\Intern\__init__.py'))
print(os.path.isfile('E:\Die Schulfach im TUD\Python\PycharmProjects\pythonProject\Module\Intern\init.py'))
print()
