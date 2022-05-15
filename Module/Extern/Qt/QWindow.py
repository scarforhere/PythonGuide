# coding: utf-8
"""
-------------------------------------------------
   File Name:      QWindow
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-05-21 11:19 PM
-------------------------------------------------
Description :

    PyQt5 Übersicht:
        http://pyqt.sourceforge.net/Docs/PyQt5/index.html
    PyQt5 Module:
        http://pyqt.sourceforge.net/Docs/PyQt5/modules.html
    PyQt5 Widgets-Modul (das wichtigste Modul):
        http://pyqt.sourceforge.net/Docs/PyQt5/QtWidgets.html
    PyQtGraph-Projekt-Webseite:
        https://github.com/pyqtgraph/pyqtgraph

"""
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore

class Gui(QtWidgets.QMainWindow):
    """
    Eigene Klasse (abgeleitet von QMainWindow)
    Diese Klasse tut (erstmal) noch nichts.
    """
    def __init__(self):
        # Konstruktor der Basis-Klass aufrufen
        QtWidgets.QMainWindow.__init__(self)

        # # 设置执行功能
        self.act_exit = QtWidgets.QAction(self)
        # 设置鼠标常驻文字说明
        self.act_exit.setText('关闭')
        # 设置图标
        self.act_exit.setIcon(QtGui.QIcon('./data/exit.png'))
        # 链接执行功能
        self.act_exit.triggered.connect(self.close)
        # 设置快捷键 （快捷键在添加进菜单栏后才有效）
        self.act_exit.setShortcut('Ctrl+Q')

        # # self.menuBar 设置菜单栏
        self.menu_file = self.menuBar().addMenu('&菜单栏')
        # 添加菜单栏子菜单
        self.menu_recent = self.menu_file.addMenu('Zuletzt geöffnet...')
        # 将执行功能添加进菜单栏
        self.menu_file.addAction(self.act_exit)

        # # 设置Toolbar
        self.toolbar = QtWidgets.QToolBar('这是Toolbar')
        self.toolbar.setIconSize(QtCore.QSize(24, 24))
        # 添加Toolbar
        self.addToolBar(self.toolbar)
        # 添加Toolbar栏功能
        self.toolbar.addAction(self.act_exit)

        # # 添加Widget栏
        self.cw = QtWidgets.QWidget()
        self.setCentralWidget(self.cw)
        self.vBox = QtWidgets.QVBoxLayout(self.cw)
        # 添加Widget栏文本说明
        self.label = QtWidgets.QLabel('Klick mich mit rechts!')
        self.label.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        # 显示Widget栏
        self.vBox.addWidget(self.label)
        # 添加Widget栏功能
        self.label.addAction(self.act_exit)


        # # 添加滑块
        self.slider = QtWidgets.QSlider(self)
        self.slider.setMinimum(-10)
        self.slider.setMaximum(10)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.vBox.addWidget(self.slider)
        # 滑块数值改变时功能
        self.slider.valueChanged.connect(self.label.setNum)
        self.slider.valueChanged.connect(self.print_value)


    def print_value(self, x):
        print(x)


app = QtWidgets.QApplication([])

gui = Gui() # Instanz von obiger Klasse anlegen
gui.show()
app.exec_()

"""
Plot-Bibliothek (= matplotlib), gut in Qt-Anwendungen integrierbar + deutlich schneller
    -->Bei interaktiven Plot-Anwendungen von Vorteil
Nachteil: Einarbeitungsaufwand
Installation (im PC-Pool evtl. nicht notwendig): pip install --user pyqtgraph
Demo-Anzeige: python -m pyqtgraph.examples
"""
