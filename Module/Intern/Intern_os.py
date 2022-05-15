# Programmed by Scar
'''
os模块：
是Python内置的与操作系统功能和文件系统相关的模块
该模块的语句的执行结果通常与操作系统有关，
在不同的操作系统上运行，得到的结果可能不一样

os模块与os.path模块用于对目录或文件进行操作

os模块操作目录相关函数
    文件操作：
        rename(name,new_name)       重命名文件
        remove(name)                删除文件
    目录操作：
        getcwd()                            返回当前工作目录
        listdir(path)                       返回指定路径下的文件和目录信息
        mkdir(path[,mode])                  创建目录
        makedirs(path1/path2...[,mode])     创建多级目录
        rmdir(path)                         删除目录
        removedirs(path1/path2...)          删除多级目录
        chdir(path)                         将path设置为当前工作目录
        walk(path)                          遍历path目录及其子目录，输出所有文件夹路径、及所含文件夹名和文件名
        path.isdir(path)                    判断是否是文件
'''
import os

# 打开应用程序
# os.system('notepad.exe')
# os.system('calc.exe')

# 直接调用可执行文件
# os.startfile('D:\\Tencent QQ\\Tencent\\QQ\\Bin\\qq.exe')

# getcwd() 返回当前工作目录
print(os.getcwd())
print()

# listdir(path) 返回指定路径下的文件和目录信息
print(os.listdir('../..'))
print()

# mkdir(path[,mode]) 创建目录
# os.mkdir('newdir')

# makedirs(path1/path2...[,mode]) 创建多级目录
# os.makedirs('A/B/C')

# rmdir(path) 删除目录（只能删除空文件）
# os.rmdir('A')

# removedirs(path1/path2...) 删除多级目录
# os.removedirs('A/B/C')

# chdir(path) 将path设置为当前工作目录
os.chdir('E:\\Die Schulfach im TUD\\Python')
print(os.getcwd())
print()

# walk(path) 遍历path目录及其子目录，输出所有文件夹路径、及所含文件夹名和文件名
path = os.getcwd()
lst_files = os.walk(path)
print(lst_files)
print(type(lst_files))
for dirpath, dirname, filename in lst_files:
    print(dirpath)
    print(dirname)
    print(filename)
    print('-----------------------------------------------')
    '''
    for dir in dirname:                     # 查询子目录
        print(os.path.join(dirpath,dir))
        print('-------------------------------------------')
    for file in filename:                     # 查询子目录
        print(os.path.join(dirpath,file))
        print('-------------------------------------------')
    '''
