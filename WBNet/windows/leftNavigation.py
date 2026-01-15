from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QStyleOption, QStyle
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QFont


class leftNavigation(QWidget):
    '''
    左侧导航栏
    '''

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.left_layout = QGridLayout()  # 创建网格布局对象
        self.setLayout(self.left_layout)  # 将左侧部件设置为网格布局

        # 初始化创建左侧标签和按钮
        self.init_left_close_mini_visit()
        self.init_left_label()
        self.init_left_Book_operation()

        # 将初始化完成的左侧标签、按钮添加进左侧网格布局
        # 最小化、放大还原、关闭部分按钮
        self.left_layout.addWidget(self.left_close, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_mini, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 2, 1, 1)
        # 图书操作部分的标签和按钮
        self.left_layout.addWidget(self.left_label1, 1, 0, 1, 3 )
        self.left_layout.addWidget(self.left_button1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button3, 4, 0, 1, 3)
        # 图书管理部分的标签和按钮
        self.left_layout.addWidget(self.left_label2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button4, 6, 0, 1, 3)

        self.left_layout.addWidget(self.left_button5, 7, 0, 1, 3)
        """tudo:把后面的依次-1，"""
        # 帮助
        # self.left_layout.addWidget(self.left_button6, 8, 0, 1, 3)

    def init_left_close_mini_visit(self):
        '''
        创建关闭、最小化、放大还原按钮
        '''
        self.left_close = QPushButton("")  # 关闭按钮
        self.left_close.setObjectName('left_close')
        self.left_mini = QPushButton("")  # 最小化按钮
        self.left_mini.setObjectName('left_mini')
        self.left_visit = QPushButton("")  # 空白按钮
        self.left_visit.setObjectName('left_visit')

        # self.left_close.clicked.connect(self.closeWindow)
        # self.left_mini.clicked.connect(self.minimizeWindow)
        # self.visitFlag = False
        # self.left_visit.clicked.connect(self.visitWindow)

    def init_left_label(self):
        '''
        左侧标题栏
        '''
        self.left_label1 = QPushButton('图像分割')
        self.left_label1.setObjectName('left_label')
        self.left_label2 = QPushButton('图像融合')
        self.left_label2.setObjectName('left_label')

        """可以删去"""

        # self.left_label3 = QPushButton('联系与帮助')
        # self.left_label3.setObjectName('left_label')

    def init_left_Book_operation(self):
        '''
        左侧图书操作按钮
        '''
        self.left_button1 = QPushButton('本地分割')
        self.left_button1.setObjectName('left_button')
        self.left_button1.setIcon(QtGui.QIcon('./windows/img/localCut.png'))
        qfont=QFont()
        qfont.setBold(20)
        qfont.setPixelSize(16)
        self.left_button1.setFont(qfont)
        # self.left_button1.setFixedSize(60,60)
        self.left_button1.setFixedHeight(80)

        self.left_button2 = QPushButton('网络分割')
        self.left_button2.setObjectName('left_button')
        self.left_button2.setIcon(QtGui.QIcon('./windows/img/InternetCut.png'))
        self.left_button3 = QPushButton('视频分割')
        self.left_button3.setObjectName('left_button')
        self.left_button3.setIcon(QtGui.QIcon('./windows/img/videoCut.png'))

        self.left_button4 = QPushButton('本地融合')
        self.left_button4.setObjectName('left_button')
        self.left_button4.setIcon(QtGui.QIcon('./windows/img/localFuse.png'))

        self.left_button5 = QPushButton('设置')
        self.left_button5.setObjectName('left_button')
        self.left_button5.setIcon(QtGui.QIcon('./windows/img/help.png'))
        #
        # self.left_button6=QPushButton("设置")
        # self.left_button6.setObjectName("left_button")
        # self.left_button6.setIcon(QtGui.QIcon('./img/help.png'))

        self.left_button2.setFont(qfont)
        self.left_button3.setFont(qfont)
        self.left_button4.setFont(qfont)
        self.left_button5.setFont(qfont)


        self.left_button2.setFixedHeight(80)
        self.left_button3.setFixedHeight(80)
        self.left_button4.setFixedHeight(80)
        self.left_button5.setFixedHeight(80)

    def paintEvent(self, event):
        '''
        避免多重传值后的功能失效，从而可以继续使用qss设置样式
        '''
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
