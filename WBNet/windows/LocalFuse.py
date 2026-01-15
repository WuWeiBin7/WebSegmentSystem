from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox, QStyleOption, QStyle, QToolButton, QTextEdit, QFileDialog
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QFont
from PyQt5.QtCore import Qt

from Get_name_path import Look_Result
from last2ui import Ui_Form7

import FuseMain


class bookIn(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.bookIn_layout = QGridLayout()  # 创建网格布局对象2
        self.setLayout(self.bookIn_layout)  # 设置右侧界面2的布局为网格布局
        self.returnMain_button = QPushButton()  # 加一个用来界面跳转的returnMain_button
        self.returnMain_button.setText('返回主界面')
        self.returnMain_button.setStyleSheet('font-size:20px')
        self.bookIn_layout.addWidget(self.returnMain_button, 0, 0, 1, 1)
        self.returnMain_button.setStyleSheet('font-size:20px;color:black;font-family:黑体;border:none; ')

        self.bookIn_single = QToolButton()
        self.bookIn_single.setText('选择图片')
        self.bookIn_single.setObjectName('bookInLibrary')
        self.bookIn_single.setIcon(
            QtGui.QIcon('./windows/img/choosePhoto.png'))
        self.bookIn_single.setIconSize(QtCore.QSize(200, 100))
        self.bookIn_single.setToolButtonStyle(
            Qt.ToolButtonTextUnderIcon)
        self.bookIn_layout.addWidget(self.bookIn_single,1,0,1,3)
        self.bookIn_single.setStyleSheet("border:none;")

        qfont=QFont()
        qfont.setBold(20)
        qfont.setPixelSize(16)
        self.bookIn_single.setFont(qfont)

        self.filePathlineEdit1 = QLineEdit()
        self.bookIn_layout.addWidget(self.filePathlineEdit1, 1, 1, 1, 3)
        self.filePathlineEdit1.setFixedSize(400,50)
        self.filePathlineEdit1.setObjectName('bookSearch_edit')

        self.bookIn_multi = QToolButton()
        self.bookIn_multi.setText('选择修改文件的文件夹')
        self.bookIn_multi.setObjectName('bookInLibrary')
        self.bookIn_multi.setIcon(
            QtGui.QIcon('./windows/img/chooseFiledir.png'))
        self.bookIn_multi.setIconSize(QtCore.QSize(200, 100))
        self.bookIn_multi.setToolButtonStyle(
            Qt.ToolButtonTextUnderIcon)
        self.bookIn_layout.addWidget(self.bookIn_multi, 2, 0, 1, 1)
        self.bookIn_multi.setStyleSheet("border:none;")

        qfont=QFont()
        qfont.setBold(20)
        qfont.setPixelSize(16)
        self.bookIn_multi.setFont(qfont)

        self.filePathlineEdit2 = QLineEdit()
        self.bookIn_layout.addWidget(self.filePathlineEdit2, 2, 1, 1, 3)
        self.filePathlineEdit2.setFixedSize(400,50)
        self.filePathlineEdit2.setObjectName('bookSearch_edit')

        self.bookIn_single.clicked.connect(
            self.searchFileName)
        # 把切换到多书入库的界面与该按钮绑定
        self.bookIn_multi.clicked.connect(
            self.searchdir)



        # ----------------------------------------------------------------

        """绑定信号与槽"""
        self.button1 = QToolButton()
        self.button1.setText('运行')
        self.button1.setObjectName('bookin_button')
        self.button1.setIcon(
            QtGui.QIcon('./windows/img/run.png'))
        self.button1.setIconSize(QtCore.QSize(200, 100))
        self.button1.setToolButtonStyle(
            Qt.ToolButtonTextUnderIcon)
        self.bookIn_layout.addWidget(self.button1, 6, 1, 1, 1)
        """绑定信号与槽"""
        # self.button2.clicked.connect(self.Return_mdir)
        self.button1.setStyleSheet("border:none;")
        self.button1.clicked.connect(self.fuce_opening)
        # self.button1.clicked.connect(self.searchdir)

        qfont=QFont()
        qfont.setBold(20)
        qfont.setPixelSize(16)
        self.button1.setFont(qfont)
        self.button1.clicked.connect(self.popWindow7)

        self.button3 = QToolButton()
        self.button3.setText('看运行结果')
        self.button3.setObjectName('bookInLibrary')
        self.button3.setIcon(
            QtGui.QIcon('./windows/img/look_file.png'))
        self.button3.setIconSize(QtCore.QSize(200, 100))
        self.button3.setToolButtonStyle(
            Qt.ToolButtonTextUnderIcon)
        self.bookIn_layout.addWidget(self.button3, 6, 2, 1, 1)
        self.button3.setStyleSheet("border:none;")
        self.button3.clicked.connect(self.look_local_fuse)

    def look_local_fuse(self):
        Look_Result.lookresult('./setting/image_fuse_path.txt')####


    def popWindow7(self):
        self.form7 = QtWidgets.QWidget()
        self.ui7 = Ui_Form7()
        self.ui7.setupUi(self.form7)
        self.form7.show()

    def fuce_opening(self):
        background_image_path=self.filePathlineEdit1.text()
        file_path=self.filePathlineEdit2.text()
        FuseMain.fusemain(background_image_path,file_path)

    def searchdir(self):
        get_directory_path = QFileDialog.getExistingDirectory(self,
                                                              "选取指定文件夹",
                                                              "C:/")
        self.filePathlineEdit2.setText(str(get_directory_path))

    def searchFileName(self):
        get_filename_path, ok = QFileDialog.getOpenFileName(self,
                                                            "选取单个文件",
                                                            "C:/",
                                                            "All Files (*);;Text Files (*.txt)")
        if ok:
            self.filePathlineEdit1.setText(str(get_filename_path))

    def paintEvent(self, event):
        '''
        避免多重传值后的功能失效，从而可以继续使用qss设置样式
        '''
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)

