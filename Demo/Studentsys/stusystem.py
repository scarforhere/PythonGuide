# Programmed by Scar
"""
学生管理系统应具备的功能
    需求分析：
        添加学生及成绩信息
        将学生信息保存到文件中
        修改和删除学生信息
        查询学生信息
        根据学生成绩进行排序
        统计学生的总分

    学生信息管理系统：
        学生信息维护：
            录入学生信息
            删除学生信息
            修改学生信息
        查询、统计：
            按学生姓名查找
            按学生ID查找
            查询并显示所有学生信息
            统计学生总人数
        排序：
            升序：
                根据英语成绩排序
                根据Python成绩排序
                根据Java程序排序
                根据总成绩排序
            降序：
                根据英语成绩排序
                根据Python成绩排序
                根据Java程序排序
                根据总成绩排序

    实现主函数
        0       推出系统
        1       录入学生信息，调用insert()函数
        2       查找学生信息，调用search()函数
        3       删除学生信息，调用delete()函数
        4       修改学生信息，调用modify()函数
        5       对学生成绩排序，调用sort()函数
        6       统计学生总人数，调用total()函数
        7       显示所有的学生信息，调用show()函数
"""
import os

filename: str = 'student.txt'

def main():
    while True:
        menum()
        choice = int(input('请选择:\t'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您却认定要推出系统么？  Y / N\n')
                if answer == 'y' or answer == 'Y1':
                    print('感谢您的使用')
                    break  # 退出系统
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息
            elif choice == 2:
                search()  # 查找学生信息
            elif choice == 3:
                delete()  # 删除学生信息
            elif choice == 4:
                modify()  # 更改学生信息
            elif choice == 5:
                sort()  # 对学生成绩进行排序
            elif choice == 6:
                total()  # 统计学生总人数
            elif choice == 7:
                show()  # 显示所有学生信息


'''
主菜单
'''
def menum():
    print('==========================学生信息管理系统==========================')
    print('------------------------------功能菜单-----------------------------')
    print('\t\t\t\t\t1.\t\t录入学生信息')
    print('\t\t\t\t\t2.\t\t查找学生信息')
    print('\t\t\t\t\t3.\t\t删除学生信息')
    print('\t\t\t\t\t4.\t\t修改学生信息')
    print('\t\t\t\t\t5.\t\t对学生成绩排序')
    print('\t\t\t\t\t6.\t\t统计学生总人数')
    print('\t\t\t\t\t7.\t\t显示所有的学生信息')
    print('\t\t\t\t\t0.\t\t推出')
    print('------------------------------------------------------------------')



'''
功能子程序
'''
# 录入学生信息
def insert():
    student_list = []
    while True:

        id = input('请输入ID(如1001)：')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入Python成绩：'))
            java = int(input('请输入Java成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue

        # 将录入的学生信息保存到字典
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}

        # 将学生信息添加到列表中
        student_list.append(student)

        answer = input('是否继续添加？  Y / N\n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

    # 调用save()函数
    save(student_list)
    print('学生信息录入完毕！！！')


# 保存函数save()
def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')

    for item in lst:
        stu_txt.write(str(item) + '\n')

    stu_txt.close()


# 查找学生信息
def search():
    studebt_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按ID查询请输入1\t按姓名查询请输入2\n')
            if mode == '1':
                id = input('请输入学生ID：')
            elif mode == '2':
                name = input('请输入学生姓名：')
            else:
                print('输入错误，请重新选择模式:')
                continue

            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            studebt_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            studebt_query.append(d)

                # 显示查询结果
                show_student(studebt_query)
                # 清除列表
                studebt_query.clear()

                answer = input('是否要继续查询?  Y / N\n')
                if answer == 'y' or answer == 'Y':
                    continue
                else:
                    return

        else:
            print('暂未保存学生信息')
            return


# 显示查询结果
def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示')
        return
    # 定义显示格式
    format_title = '{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}'
    print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    # 定义内容的显示格式
    format_data = '{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english')) + int(item.get('python')) + int(item.get('java'))
                                 ))


# 删除学生信息
def delete():
    while True:
        student_id = input('请输入要删除的学生的ID：')
        if student_id != '':

            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []

            flag = False  # 标记是否删除

            # 旧文件全部信息按行读取
            # 按行保存为dict后查找手都有相同id信息
            # 如果本行id不重复则重新写入本行信息
            # 若本行id重复，则跳过不写入
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转换为字典
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True

                    if flag:
                        print('id为{0}的学生信息已被删除'.format(student_id))
                    else:
                        print('无法找到id为id为{0}的学生信息'.format(student_id))
            else:
                print('无法找到学生信息！')
                break

            show()  # 删除之后重新显示所有学生的信息
            answer = input('是否继续删除？  Y / N\n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break


# 修改学生信息
def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return

    student_id = input('请输入要修改的学生ID:')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('招到学生信息，可以修改相关信息！')
                while True:
                    try:
                        d['name'] = input('请输入姓名：')
                        d['english'] = input('请输入英语成绩：')
                        d['python'] = input('请输入Python成绩：')
                        d['java'] = input('请输入Java成绩：')
                    except:
                        print('您的输入有误，请重新输入！！！')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功！！！')
            else:
                wfile.write(str(d) + '\n')
        answer = input('是否继续修改其他学生信息？ Y / N')
        if answer == 'y' or answer == 'Y':
            modify()
        else:
            return

        # 对学生成绩排序

# 将学生信息进行排序
def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_lst = rfile.readlines()
        student_new = []
        for item in student_lst:
            student_new.append(dict(eval(item)))
    else:
        return

    asc_or_desc = input('请选择(0.升序  1.降序）：')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('输入错误，请重新选择')
        sort()
        return

    mode = input('请选择排序方式(1.按英语成绩排序  2.按Python程序排序  3.按Java趁机排序  0.按总成绩排序)')
    if mode == '1':
        student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
    elif mode == '0':
        student_new.sort(key=lambda x: int(x['english']) + int(x['python']) + int(x['english']),
                         reverse=asc_or_desc_bool)
    else:
        print('输入错误，请重新选择')
        sort()
        return

    show_student(student_new)

    answer = input('是否继续排序查询？ Y / N\n')
    if answer == 'y' or answer == 'Y':
        show()
        return
    else:
        return

    # 统计学生总人数

# 显示所有学生信息
def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还未录入学生信息')
    else:
        print('暂未保存数据信息...')


# 显示所有的学生信息
def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
    else:
        print('暂未保存过数据...')


'''
判断是否为最高级程序
    如果是最高级程序则执行主程序
'''
if __name__ == '__main__':
    main()
