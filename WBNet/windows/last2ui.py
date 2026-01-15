# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form7(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.move(750,400)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 40, 171, 81))
        self.label.setStyleSheet("font: 75 12pt \"Agency FB\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 210, 121, 61))
        self.pushButton.setStyleSheet("font: 75 14pt \"Agency FB\";")
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(110, 130, 151, 41))
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "operating"))
        self.label.setText(_translate("Form", "处理成功！"))
        self.pushButton.setText(_translate("Form", "ok"))

