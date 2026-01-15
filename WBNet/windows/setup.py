from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox, QStyleOption, QStyle, QToolButton, QTextEdit, QFileDialog
from PyQt5.QtGui import QPainter, QFont
from qtpy import QtWidgets
from set_ui import Ui_Form7


class cardManage(QWidget):
    def __init__(self):
        super().__init__()
        self.init()


    def init(self):
        self.cardManage_layout = QGridLayout()
        self.setLayout(self.cardManage_layout)

        self.returnMain_button = QPushButton('返回主界面')
        self.cardManage_layout.addWidget(self.returnMain_button, 0, 0, 1, 1)
        self.returnMain_button.setStyleSheet("border:none;")
        self.returnMain_button.setStyleSheet('font-size:20px;color:black;font-family:黑体;border:none; ')


        self.card_number_label = QLabel('原图保存地址')
        self.cardManage_layout.addWidget(self.card_number_label, 3, 1, 1, 1)
        self.card_number_label.setObjectName('cardManage_label')
        self.card_number_label.setStyleSheet('font-size:20px;color:red;font-family:黑体 ')
        self.card_number_label.setFixedSize(200,56)

        with open('./setting/set_original_image_path.txt') as file1:
            path1=file1.read()

        self.filePathlineEdit1 = QLineEdit(str(path1))
        self.cardManage_layout.addWidget(self.filePathlineEdit1, 3, 2, 1, 3)
        self.filePathlineEdit1.setObjectName('cardManage_edit')

        self.filePathlineEdit1.setFixedSize(400,35)

        # self.card_buttom1=QPushButton("设置")
        # self.cardManage_layout.addWidget(self.card_buttom1,3,5,1,2)
        # self.card_buttom1.setObjectName('cardManage_edit')

        self.card_buttom11 = QPushButton('设置')
        self.cardManage_layout.addWidget(self.card_buttom11,3,5,1,1)
        self.card_buttom11.setStyleSheet("border:none;")
        self.card_buttom11.setStyleSheet('font-size:20px;color:red;font-family:黑体 ')

        self.card_buttom11.clicked.connect(self.search1)

        self.card_buttom12 = QPushButton('保存')
        self.cardManage_layout.addWidget(self.card_buttom12, 3, 6, 1, 1)
        self.card_buttom12.setStyleSheet("border:none;")
        self.card_buttom12.setStyleSheet('font-size:20px;color:red;font-family:黑体 ')
        self.card_buttom12.clicked.connect(self.set_original_image_path)

        qfont=QFont()
        qfont.setBold(20)
        qfont.setPixelSize(16)
        self.card_buttom11.setFont(qfont)
        self.card_buttom11.setFixedSize(100,35)
        self.card_buttom12.setFont(qfont)
        self.card_buttom12.setFixedSize(100,35)



        self.card_number_label2 = QLabel('分割结果保存路径')
        self.cardManage_layout.addWidget(self.card_number_label2, 4, 1, 1, 1)
        self.card_number_label2.setObjectName('cardManage_label')
        self.card_number_label2.setStyleSheet('font-size:20px;color:red;font-family:黑体 ')
        self.card_number_label2.setFixedSize(200,56)


        with open('./setting/set_result_image_path.txt') as file1:
            path2=file1.read()
        self.filePathlineEdit2 = QLineEdit(path2)
        self.cardManage_layout.addWidget(self.filePathlineEdit2, 4, 2, 1, 3)
        self.filePathlineEdit2.setObjectName('cardManage_edit')
        self.filePathlineEdit2.setFixedSize(400,35)


        self.card_buttom21=QPushButton("设置")
        self.cardManage_layout.addWidget(self.card_buttom21,4,5,1,1)
        self.card_buttom21.setObjectName('cardManage_edit')
        self.card_buttom21.clicked.connect(self.search2)
        self.card_buttom21.setStyleSheet("border:none;")

        self.card_buttom22 = QPushButton('保存')
        self.cardManage_layout.addWidget(self.card_buttom22, 4, 6, 1, 1)
        self.card_buttom22.setStyleSheet("border:none;")
        self.card_buttom22.setStyleSheet('font-size:20px;color:red;font-family:黑体 ')

        qfont=QFont()
        qfont.setBold(20)
        qfont.setPixelSize(16)
        self.card_buttom21.setFont(qfont)
        self.card_buttom21.setFixedSize(100,35)

        self.card_buttom22.setFont(qfont)
        self.card_buttom22.setFixedSize(100,35)

        self.card_number_label3 = QLabel('图像融合路径')
        self.cardManage_layout.addWidget(self.card_number_label3, 5, 1, 1, 1)
        self.card_number_label3.setObjectName('cardManage_label')
        self.card_number_label3.setStyleSheet('font-size:20px;color:red;font-family:黑体 ')
        self.card_number_label3.setFixedSize(200,56)

        with open('./setting/image_fuse_path.txt') as file1:
            path3=file1.read()
        self.filePathlineEdit3 = QLineEdit(path3)
        self.cardManage_layout.addWidget(self.filePathlineEdit3, 5, 2, 1, 3)
        self.filePathlineEdit3.setObjectName('cardManage_edit')
        self.filePathlineEdit3.setFixedSize(400,35)

        self.card_buttom31=QPushButton("设置")
        self.cardManage_layout.addWidget(self.card_buttom31,5,5,1,1)
        self.card_buttom31.setObjectName('cardManage_edit')
        self.card_buttom31.clicked.connect(self.search3)
        self.card_buttom31.setStyleSheet("border:none;")

        self.card_buttom32 = QPushButton('保存')
        self.cardManage_layout.addWidget(self.card_buttom32, 5, 6, 1, 1)
        self.card_buttom32.setStyleSheet("border:none;")
        self.card_buttom32.setStyleSheet('font-size:20px;color:red;font-family:黑体 ')

        qfont=QFont()
        qfont.setBold(20)
        qfont.setPixelSize(16)
        self.card_buttom31.setFont(qfont)
        self.card_buttom31.setFixedSize(100,35)

        self.card_buttom32.setFont(qfont)
        self.card_buttom32.setFixedSize(100,35)

        self.card_number_label4 = QLabel('视频分割结果路径')
        self.cardManage_layout.addWidget(self.card_number_label4, 6, 1, 1, 1)
        self.card_number_label4.setObjectName('cardManage_label')
        self.card_number_label4.setStyleSheet('font-size:20px;color:red;font-family:黑体 ')
        self.card_number_label4.setFixedSize(200,56)

        with open('./setting/video_sagement_outcome_path.txt') as file1:
            path4=file1.read()

        self.filePathlineEdit4 = QLineEdit(path4)
        self.cardManage_layout.addWidget(self.filePathlineEdit4, 6, 2, 1, 3)
        self.filePathlineEdit4.setObjectName('cardManage_edit')
        self.filePathlineEdit4.setFixedSize(400,35)


        self.card_buttom41=QPushButton("设置")
        self.cardManage_layout.addWidget(self.card_buttom41,6,5,1,1)
        self.card_buttom41.setObjectName('cardManage_edit')
        qfont=QFont()
        qfont.setBold(20)
        qfont.setPixelSize(16)
        self.card_buttom41.setFont(qfont)
        self.card_buttom41.setFixedSize(100,35)


        self.card_buttom42 = QPushButton('保存')
        self.cardManage_layout.addWidget(self.card_buttom42, 6, 6, 1, 1)
        self.card_buttom42.setStyleSheet("border:none;")
        self.card_buttom42.setStyleSheet('font-size:20px;color:red;font-family:黑体 ')

        self.card_buttom42.setFont(qfont)
        self.card_buttom42.setFixedSize(100,35)

        self.card_buttom41.clicked.connect(self.search4)
        self.card_buttom41.setStyleSheet("border:none;")
        self.card_buttom41.setStyleSheet("QPushButton{border:none;color:rgb(0, 0, 0);}"
                                 "QPushButton:hover{background-color: rgb(171, 233, 245);border:none;color:rgb(0, 0, 0);}")
        self.card_buttom31.setStyleSheet("QPushButton{border:none;color:rgb(0, 0, 0);}"
                                 "QPushButton:hover{background-color: rgb(171, 233, 245);border:none;color:rgb(0, 0, 0);}")
        self.card_buttom21.setStyleSheet("QPushButton{border:none;color:rgb(0, 0, 0);}"
                                 "QPushButton:hover{background-color: rgb(171, 233, 245);border:none;color:rgb(0, 0, 0);}")
        self.card_buttom11.setStyleSheet("QPushButton{border:none;color:rgb(0, 0, 0);}"
                                 "QPushButton:hover{background-color: rgb(171, 233, 245);border:none;color:rgb(0, 0, 0);}")
        self.card_buttom42.setStyleSheet("QPushButton{border:none;color:rgb(0, 0, 0);}"
                                 "QPushButton:hover{background-color: rgb(255, 131, 131);border:none;color:rgb(0, 0, 0);}")
        self.card_buttom32.setStyleSheet("QPushButton{border:none;color:rgb(0, 0, 0);}"
                                 "QPushButton:hover{background-color: rgb(255, 131, 131);border:none;color:rgb(0, 0, 0);}")
        self.card_buttom22.setStyleSheet("QPushButton{border:none;color:rgb(0, 0, 0);}"
                                 "QPushButton:hover{background-color: rgb(255, 131, 131);border:none;color:rgb(0, 0, 0);}")
        self.card_buttom12.setStyleSheet("QPushButton{border:none;color:rgb(0, 0, 0);}"
                                 "QPushButton:hover{background-color: rgb(255, 131, 131);border:none;color:rgb(0, 0, 0);}")
        self.card_buttom22.clicked.connect(self.set_result_image_path)
        self.card_buttom32.clicked.connect(self.set_image_fuse_path)
        self.card_buttom42.clicked.connect(self.set_video_sagement_outcome_path)


        self.card_buttom12.clicked.connect(self.popWindow7)

        self.card_buttom22.clicked.connect(self.popWindow7)
        self.card_buttom32.clicked.connect(self.popWindow7)
        self.card_buttom42.clicked.connect(self.popWindow7)

    def popWindow7(self):
        self.form7 = QtWidgets.QWidget()
        self.ui7 = Ui_Form7()
        self.ui7.setupUi(self.form7)
        self.form7.show()

    def search1(self):
        get_directory_path = QFileDialog.getExistingDirectory(self,
                                                              "选取指定文件夹",
                                                              "C:/")
        self.filePathlineEdit1.setText(str(get_directory_path))
    def search2(self):
        get_directory_path = QFileDialog.getExistingDirectory(self,
                                                              "选取指定文件夹",
                                                              "C:/")
        self.filePathlineEdit2.setText(str(get_directory_path))
    def search3(self):
        get_directory_path = QFileDialog.getExistingDirectory(self,
                                                              "选取指定文件夹",
                                                              "C:/")
        self.filePathlineEdit3.setText(str(get_directory_path))
    def search4(self):
        get_directory_path = QFileDialog.getExistingDirectory(self,
                                                              "选取指定文件夹",
                                                              "C:/")
        self.filePathlineEdit4.setText(str(get_directory_path))


    def set_original_image_path(self):
        original_image_path=self.filePathlineEdit1.text()
        with open('./setting/set_original_image_path.txt','w') as file1:
            file1.write(original_image_path)

    def set_result_image_path(self):
        result_image_path=self.filePathlineEdit2.text()
        with open('./setting/set_result_image_path.txt','w') as file1:
            file1.write(result_image_path)

    def set_image_fuse_path(self):
        fuse_path=self.filePathlineEdit3.text()
        with open('./setting/image_fuse_path.txt','w') as file1:
            file1.write(fuse_path)

    def set_video_sagement_outcome_path(self):
        video_sagement_outcome_path=self.filePathlineEdit4.text()
        with open('./setting/video_sagement_outcome_path.txt','w') as file1:
            file1.write(video_sagement_outcome_path)



    def paintEvent(self, event):
        '''
        避免多重传值后的功能失效，从而可以继续使用qss设置样式
        '''
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
