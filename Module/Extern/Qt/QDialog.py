# coding: utf-8
"""
-------------------------------------------------
   File Name:      QDialog
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-05-21 10:22 AM
-------------------------------------------------
Description : 

    PyQt5 Übersicht:
        http://pyqt.sourceforge.net/Docs/PyQt5/index.html

    PyQt5 Module:
        http://pyqt.sourceforge.net/Docs/PyQt5/modules.html

    PyQt5 Widgets-Modul (das wichtigste Modul):
        http://pyqt.sourceforge.net/Docs/PyQt5/QtWidgets.html

    verweist auf Referenz des QtWidgets-Moduls (C++):
        https://doc.qt.io/qt-5/qtwidgets-module.html

    Verschiedene kurze Qt5-Tutorials:
        https://pythonspot.com/en/gui/

    Referenz des configparser-Moduls:
        https://docs.python.org/3/library/configparser.html

"""
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui

# 添加程序
app = QtWidgets.QApplication([])
# 添加窗口
dialog = QtWidgets.QDialog()

# 添加标签
mass_label = QtWidgets.QLabel('Masse', dialog)
# 添加输入栏
mass_edit = QtWidgets.QLineEdit('2.5', dialog)
# 添加按钮
exit_button = QtWidgets.QPushButton('Exit', dialog)

len_label = QtWidgets.QLabel('Pendellänge', dialog)
len_edit = QtWidgets.QLineEdit('1', dialog)

# 初始化网格布局
layout = QtWidgets.QGridLayout()
layout.addWidget(mass_label, 0, 0)  # Zeile, Spalte
layout.addWidget(mass_edit, 0, 1)
layout.addWidget(len_label, 1, 0)
layout.addWidget(len_edit, 1, 1)
layout.addWidget(exit_button, 4, 1, QtCore.Qt.AlignRight)

# 设置右对齐
mass_edit.setAlignment(QtCore.Qt.AlignRight)
# 设置只允许输入数字
mass_edit.setValidator(QtGui.QDoubleValidator(mass_edit))
len_edit.setAlignment(QtCore.Qt.AlignRight)


def openfile():
    path, type_filter = QtWidgets.QFileDialog.getOpenFileName()
    print(path, type_filter)


def savefile():
    path, type_filter = QtWidgets.QFileDialog.getSaveFileName()
    print(path, type_filter)


# 添加按钮
open_button = QtWidgets.QPushButton('Öffnen', dialog)
save_button = QtWidgets.QPushButton('Speichern', dialog)

layout.addWidget(open_button, 2, 0,1,2)
layout.addWidget(save_button, 3, 0,1,2)

# 链接按钮功能
open_button.clicked.connect(openfile)
save_button.clicked.connect(savefile)
exit_button.clicked.connect(dialog.close)

# 使用网格布局
dialog.setLayout(layout)
# 显示窗口
dialog.exec()
