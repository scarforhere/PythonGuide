# Programmed by Scar
"""
prettytable:
    整理表格
"""

import prettytable as pt


# 显示坐席
def show_ticket(row_num):
    tb = pt.PrettyTable()
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(row_num):
        lst = [f'第{i + 1}行', '有票', '有票', '有票', '有票', '有票']
        tb.add_row(lst)
    print(tb)


def order_ticket(row_num, row, colum):
    tb = pt.PrettyTable()
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(row_num):
        if int(row) == i + 1:
            lst = [f'第{i + 1}行', '有票', '有票', '有票', '有票', '有票']
            lst[int(colum)] = '已售'
            tb.add_row(lst)
        else:
            lst = [f'第{i + 1}行', '有票', '有票', '有票', '有票', '有票']
            tb.add_row(lst)
    print(tb)


if __name__ == '__main__':
    row_num = 13
    show_ticket(row_num)
    choose_num = input('请输入选择的座位（13/5表示13排5号座位）')
    try:
        row, colum = choose_num.split('/')
    except:
        print('输入格式有误，请重新输入')
    order_ticket(row_num, row, colum)
