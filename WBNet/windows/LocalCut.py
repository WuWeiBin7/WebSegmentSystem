from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox, QStyleOption, QStyle, QToolButton, QTextEdit, QFileDialog
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyleOption, QStyle, QWidget, QLabel, QPushButton, QLineEdit, QTableView, QGridLayout, QFileDialog, QMessageBox, QTableWidget, QFrame, QTableWidgetItem
from PyQt5.QtGui import QPainter, QFont

from Get_name_path import Look_Result
from WBNet import wbnet, File_readPath
from last2ui import Ui_Form7


class bookSearch(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.localCut_layout = QGridLayout()
        self.setLayout(self.localCut_layout)



        self.returnMain_button = QPushButton('返回主界面')
        self.localCut_layout.addWidget(self.returnMain_button, 0, 0 ,1, 1)
        self.returnMain_button.setStyleSheet('font-size:20px;color:black;font-family:黑体;border:none; ')

        self.button1 = QToolButton()
        self.button1.setText('选择文件夹')
        self.button1.setObjectName('bookInLibrary')
        self.button1.setIcon(
            QtGui.QIcon('./windows/img/chooseFiledir.png'))
        self.button1.setIconSize(QtCore.QSize(200, 100))
        self.button1.setToolButtonStyle(
            Qt.ToolButtonTextUnderIcon)
        self.localCut_layout.addWidget(self.button1, 1, 0, 1, 1)
        self.button1.clicked.connect(self.search)
        self.button1.setStyleSheet("border:none;")


        qfont=QFont()
        qfont.setBold(20)
        qfont.setPixelSize(16)
        self.button1.setFont(qfont)

        self.filePathlineEdit = QLineEdit()
        self.localCut_layout.addWidget(self.filePathlineEdit, 1, 1, 1, 2)
        self.filePathlineEdit.setFixedSize(120,50)
        self.filePathlineEdit.setObjectName('bookSearch_edit')

        self.button2 = QToolButton()
        self.button2.setText('运行')
        self.button2.setObjectName('bookInLibrary')
        self.button2.setIcon(
            QtGui.QIcon('./windows/img/run.png'))
        self.button2.setIconSize(QtCore.QSize(200, 100))
        self.button2.setToolButtonStyle(
            Qt.ToolButtonTextUnderIcon)
        self.localCut_layout.addWidget(self.button2, 1, 4, 1, 1)

        qfont=QFont()
        qfont.setBold(20)
        qfont.setPixelSize(16)
        self.button2.setFont(qfont)


        self.button3 = QToolButton()
        self.button3.setText('看运行结果')
        self.button3.setObjectName('bookInLibrary')
        self.button3.setIcon(
            QtGui.QIcon('./windows/img/look_file.png'))
        self.button3.setIconSize(QtCore.QSize(200, 100))
        self.button3.setToolButtonStyle(
            Qt.ToolButtonTextUnderIcon)
        self.localCut_layout.addWidget(self.button3, 2, 1, 1, 1)
        self.button3.setStyleSheet("border:none;")


        self.button3.clicked.connect(self.look_local_cut)

        """绑定信号与槽"""
        self.button2.clicked.connect(self.popWindow7)

        self.button2.clicked.connect(self.local_segmentation)
        self.button2.setStyleSheet("border:none;")

            


################################### wbnet localCut##########################################3
    def look_local_cut(self):
        Look_Result.lookresult('./setting/set_result_image_path.txt')



    def local_segmentation(self):
        mdir=self.filePathlineEdit.text()
        wbnet(mdir)
        #return mdir

    def opean_fiel(self):
        path1=File_readPath.read()

    def popWindow7(self):
        self.form7 = QtWidgets.QWidget()
        self.ui7 = Ui_Form7()
        self.ui7.setupUi(self.form7)
        self.form7.show()


    def search(self):
        get_directory_path = QFileDialog.getExistingDirectory(self,
                                                              "选取指定文件夹",
                                                              "C:/")
        self.filePathlineEdit.setText(str(get_directory_path))


    def paintEvent(self, event):
        '''
        避免多重传值后的功能失效，从而可以继续使用qss设置样式
        '''
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
