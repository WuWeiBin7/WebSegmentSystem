import qtawesome
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox, QStyleOption, QStyle, QToolButton, QTextEdit, QFileDialog
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QPixmap, QFont

from WBNet import wbnet
from spider import *
from last2ui import Ui_Form7


class bookBorrow(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.InternetCut_layout = QGridLayout()
        self.setLayout(self.InternetCut_layout)
        self.returnMain_button = QPushButton('返回主界面')
        self.InternetCut_layout.addWidget(self.returnMain_button, 0, 0, 1, 1)
        # self.returnMain_button.setFixedSize(900,80)
        # self.returnMain_button.setStyleSheet("border:none;")
        self.returnMain_button.setStyleSheet('font-size:20px;color:black;font-family:黑体;border:none; ')


        self.book_number_label = QPushButton('关键字')
        self.InternetCut_layout.addWidget(self.book_number_label, 1, 1, 1, 1)
        self.book_number_label.setObjectName('bookBorrow_label')
        self.book_number_label.setFixedSize(150,100)
        self.book_number_label.setStyleSheet('font-size:30px;font-family:黑体;font-weight: bold;')
        self.book_number_label.setStyleSheet("QPushButton{border:none;color:rgb(0, 0, 0);}"
                                 "border:none;color:rgb(0, 0, 0);}")
        self.book_number_label.setFont(qtawesome.font('fa', 16))
        self.book_number_label.setIcon(QtGui.QIcon('./windows/img/magnifier.png'))

        qfont=QFont()
        qfont.setBold(20)
        qfont.setPixelSize(16)
        self.book_number_label.setFont(qfont)

        #     网络分割口是第一个是关键字，名称
        self.book_number = QLineEdit()
        self.InternetCut_layout.addWidget(self.book_number, 1, 2, 1, 2)
        self.book_number.setObjectName('bookBorrow_edit')
        self.book_number.setFixedSize(400,50)

        # self.book_number.setFixedSize(150,100)


        self.card_number_label = QPushButton('图片数量')
        self.InternetCut_layout.addWidget(self.card_number_label, 2, 1, 1, 1)
        self.card_number_label.setObjectName('bookBorrow_label')
        self.card_number_label.setFixedSize(150,100)
        self.card_number_label.setStyleSheet('font-size:30px;font-family:黑体;font-weight: bold;')
        self.card_number_label.setStyleSheet("QPushButton{border:none;color:rgb(0, 0, 0);}"
                                 "border:none;color:rgb(0, 0, 0);}")
        self.card_number_label.setIcon(QtGui.QIcon('./windows/img/photoNumer.png'))

        self.card_number_label.setFont(qfont)

        #     网络分割口是第2个是关键字 ，mber
        self.card_number = QLineEdit()
        self.InternetCut_layout.addWidget(self.card_number, 2, 2, 1, 2)
        self.card_number.setObjectName('bookBorrow_edit')
        self.card_number.setFixedSize(400,50)


        self.Borrow_button1 = QPushButton('百度')
        self.InternetCut_layout.addWidget(self.Borrow_button1, 3, 1, 1, 1)
        self.Borrow_button1.setObjectName('bookBorrow_button')
        self.Borrow_button1.setIcon(QtGui.QIcon('./windows/img/baidu.png'))

        self.Borrow_button1.setStyleSheet("border:none;")

        # self.Borrow_button1.setFixedSize(150,220)

        self.Borrow_button1.clicked.connect(self.popWindow7)

        self.Borrow_button1.clicked.connect(self.get_baidu)

        self.Borrow_button2 = QPushButton('必应')
        self.InternetCut_layout.addWidget(self.Borrow_button2, 3, 2, 1, 1)
        self.Borrow_button2.setObjectName('bookBorrow_button')
        self.Borrow_button2.setIcon(QtGui.QIcon('./windows/img/bing.png'))
        # self.Borrow_button2.setFixedSize(150,220)
        self.Borrow_button2.clicked.connect(self.popWindow7)

        self.Borrow_button2.clicked.connect(self.get_bing)
        self.Borrow_button2.setStyleSheet("border:none;")


        self.Borrow_button3 = QPushButton('搜狗')
        self.InternetCut_layout.addWidget(self.Borrow_button3, 3, 3, 1, 1)
        self.Borrow_button3.setObjectName('bookBorrow_button')
        self.Borrow_button3.setIcon(QtGui.QIcon('./windows/img/sougou.png'))
        # self.Borrow_button3.setStyleSheet("border:none;")
        self.Borrow_button3.resize(100,100)
        self.Borrow_button3.clicked.connect(self.popWindow7)

        self.Borrow_button3.clicked.connect(self.get_sougou)


        self.Borrow_button3.setStyleSheet('font-size:100px;color:black;font-family:黑体;border:none;font-weight: bold; ')

        self.Borrow_button1.setFont(qfont)
        self.Borrow_button2.setFont(qfont)
        self.Borrow_button3.setFont(qfont)

        self.Borrow_button3.setStyleSheet("QPushButton{border:none;color:rgb(0, 0, 0);}"
                                          "QPushButton:hover{background-color: rgb(171, 233, 245);border:none;color:rgb(0, 0, 0);}")
        self.Borrow_button2.setStyleSheet("QPushButton{border:none;color:rgb(0, 0, 0);}"
                                 "QPushButton:hover{background-color: rgb(171, 233, 245);border:none;color:rgb(0, 0, 0);}")

        self.Borrow_button1.setStyleSheet("QPushButton{border:none;color:rgb(0, 0, 0);}"
                                      "QPushButton:hover{background-color: rgb(171, 233, 245);border:none;color:rgb(0, 0, 0);}")


        self.Borrow_button4 = QPushButton()
        self.InternetCut_layout.addWidget(self.Borrow_button4, 3, 6, 1, 1)
        self.Borrow_button4.setStyleSheet("border:none;")



    def get_baidu(self):
        # name = self.QL.toPlainText()
        name=self.book_number.text()
        num=self.card_number.text()
        # num = int(self.textEdit_2.toPlainText())
        image_path = baidu_main(num,name)  #####
        wbnet(image_path)

    def popWindow7(self):
        self.form7 = QtWidgets.QWidget()
        self.ui7 = Ui_Form7()
        self.ui7.setupUi(self.form7)
        self.form7.show()

    def get_sougou(self):
        name=self.book_number.text()
        num=self.card_number.text()
        image_path = sougo_main(num,name)
        wbnet(image_path)


    def get_bing(self):
        name=self.book_number.text()
        num=self.card_number.text()
        image_path=bing_main(num,name)
        wbnet(image_path)

    def paintEvent(self, event):
        '''
        避免多重传值后的功能失效，从而可以继续使用qss设置样式
        '''
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)


