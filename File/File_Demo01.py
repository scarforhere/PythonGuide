# Programmed by Scar
"""

    要求列出指定目录下的所有python文件

"""
# 使用os.walk(path)遍历
import os

Path_Root = '/'

lst_file = os.walk(Path_Root)
for dirpath, dirfile, filename in lst_file:
    for item in filename:
        if item.endswith('.py'):
            print(os.path.join(dirpath, item))

# 旧方法
'''
import os.path as iP
import os as iO

def Dir_Print(Root, mode=0, ResultPath=''):
    iO.chdir(Root)  # 设置根目录Path
    Child_list = iO.listdir()  # 返回根目录Path下的文件和目录信息

    if ResultPath == '':  # 如果模有指定ResultPath则输出txt文档至根目录
        ResultPath = Root

    for Child in Child_list:  # 遍历Path的目录信息
        Path = Root + '\\' + Child
        if not iP.isdir(Path):  # 如果是文件，进行打印输出路径和文件名
            if Child.endswith('.py'):  # 当文件类型为.py时输出路径和文件名
                if mode == 0:  # 当模式为0时，在程序内打印结果，默认mode为0
                    print(Root, '\t:', Child)
                elif mode == 1:  # 当模式为1时，打印结果至Path路径下Result.txt文件，默认路径为根目录
                    with open(ResultPath + '\\Result.txt', 'a+') as Fp:
                        Fp.write(Root + '\t:' + Child + '\n')
                else:  # 当模式为其他时，报错
                    print('Please choose a right print mode')

        else:  # 如果是目录进行嵌套循环
            try:
                Dir_Print(Path, mode, ResultPath)
            except BaseException as e:
                print('Problem:', e)


Path_Root = input('Please input the Path:')
try:
    mode = int(input('Please input print mode:'))
except:
    mode = 0
ResultPath = input('Please input Result Path:')

Dir_Print(Path_Root, mode, ResultPath)
'''