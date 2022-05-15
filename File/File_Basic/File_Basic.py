# Programmed by Scar
"""
文件读写原理
    文件的读写俗称’IO操作“
    文件读写操作流程
        Python操作文件  -->打开或新建文件  -->读写文件  -->关闭资源

操作文件步骤
    1. 打开文件
    2. 读写文件
    3. 关闭文件

内置函数open()创建文件对象
语法规则
    file = open ( filename [ , mode , encoding ] )
    mode r      以只读模式打开文件，文件的指针将会放在文件开头
    mode w      以只写模式打开文件，如果文件不存在则创建，如果文件存在，则覆盖原有内容，文件指针在文件的开头
    mode a      以追加模式打开文件，如果文件不存在则创建，如果文件存在，则在文件末尾追加内容，文件指针在源文件末尾
    mode b      以二进制打开文件，不能单独使用，需要与其他模式一起使用，如 rb 或 wb
    mode r+     以读写模式打开文件，文件的指针将会放在文件开头
    mode w+     以读写模式打开文件，如果文件不存在则创建，如果文件存在，则覆盖原有内容，文件指针在文件的开头
    mode a+     以读写模式打开文件，如果文件不存在则创建，如果文件存在，则在文件末尾追加内容，文件指针在源文件末尾
    mode wb     二进制模式下以只写模式打开文件，如果文件不存在则创建，如果文件存在，则覆盖原有内容，文件指针在文件的开头
    mode wb+    二进制模式下以读写模式打开文件，如果文件不存在则创建，如果文件存在，则覆盖原有内容，文件指针在文件的开头
    mode ab+    二进制模式下以读写模式打开文件，如果文件不存在则创建，如果文件存在，则在文件末尾追加内容，文件指针在源文件末尾
    mode rb     二进制模式下读取文件
    encoding=   默认文本文件中字符的编写格式为GBK

注意： 以读写模式打开文件会频繁移动文件指针，导致操作变慢

文件的类型
    按文件中数据的组织形式，文件分为以下两大类
        文本文件：
            储存的时普天同“字符”文本，默认为Unicode字符集，可以使用记事本程序打开
        二进制文件：
            把数据内容用“字节”进行存储，无法用记事本打开，必须使用专用软件打开，例如：.mp3  .jpg    .doc

文件对象的常用方法
    read([size])                从文件中读取size个字节或字符的内容返回，若省略[size]，则读取到文件末尾，即一次读取文件所有内容
    readline()                  从文件中读取一行内容，读取完后将指针移动到下一行开头
    readlines()                 把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回
    write(str)                  将字符串str写入文件
    writelines(s_list)          将字符串列表s_list写入文本文件，不添加换行符
    seek(offset[,whence])       把文件指针移动到新的位置，offset标识相对于whence的位置
                                    offset：为正-->往结束方向移动
                                    offset：为负-->往开始方向移动
                                    whence不同时代表不同含义
                                        0：从文件开头开始计算（默认值）
                                        1：从当前位置开始计算
                                        2：从文件尾开始计算
    tell()                      返回文件指针当前位置
    flush()                     把缓冲区的内容写入文件，但不关闭文件
    close()                     把缓冲区的内容写入文件，但同时关闭文件，释放文件对象相关资源
"""
# 只读操作
file=open('a.txt', 'r')
print(file.readlines())
file.close()

# 只写操作
file=open('b', 'w')
file.write('Pythone')
file.close()

# 追加写入
for item in range(3):
    file=open('b', 'a')
    file.write('Pythone')
    file.close()

# 二进模式进行图片复制
src_file=open('Unbenannt.png', 'rb')
target_file=open('copyphoto.png','wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()

print()

'''
文件对象的常用方法
    read([size])                从文件中读取size个字节或字符的内容返回，若省略[size]，则读取到文件末尾，即一次读取文件所有内容
                                执行完read会将文件的指针移动到文件的末尾
    readline()                  从文件中读取一行内容
                                执行完read会将文件的指针移动到文件的末尾
    readlines()                 把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回
    write(str)                  将字符串str写入文件，
    writelines(s_list)          将字符串列表s_list写入文本文件，不添加换行符
    seek(offset[,whence])       把文件指针移动到新的位置，offset标识相对于whence的位置
                                    offset：为正-->往结束方向移动
                                    offset：为负-->往开始方向移动
                                    whence不同时代表不同含义
                                        0：从文件开头开始计算（默认值）
                                        1：从当前位置开始计算
                                        2：从文件尾开始计算
    tell()                      返回文件指针当前位置
    flush()                     把缓冲区的内容写入文件，但不关闭文件
    close()                     把缓冲区的内容写入文件，但同时关闭文件，释放文件对象相关资源
'''
file=open('a.txt', 'r')
print(file.read(2))
print(file.readline())
file.close()
print()

file=open('c.txt', 'w')
file.write('hallo')
lst=['java','go','python']
file.writelines(lst)
file.close()
print()

file=open('a.txt', 'r')
file.seek(2)            # 一个汉字占3个字节
print(file.read())
print(file.tell() )
file.close()