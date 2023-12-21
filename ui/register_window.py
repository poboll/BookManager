# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(418, 366)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.username_lineEdit = QtWidgets.QLineEdit(Form)
        self.username_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.horizontalLayout.addWidget(self.username_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.password_lineEdit = QtWidgets.QLineEdit(Form)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout_2.addWidget(self.password_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.confirm_password_lineEdit = QtWidgets.QLineEdit(Form)
        self.confirm_password_lineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.confirm_password_lineEdit.setObjectName("confirm_password_lineEdit")
        self.horizontalLayout_4.addWidget(self.confirm_password_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.return_pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.return_pushButton.setFont(font)
        self.return_pushButton.setObjectName("return_pushButton")
        self.horizontalLayout_3.addWidget(self.return_pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.register_pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.register_pushButton.setFont(font)
        self.register_pushButton.setObjectName("register_pushButton")
        self.horizontalLayout_3.addWidget(self.register_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(100, 40))
        self.label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 3, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem7, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "用户:"))
        self.label_4.setText(_translate("Form", "密码:"))
        self.label_5.setText(_translate("Form", "确认:"))
        self.return_pushButton.setText(_translate("Form", "返回"))
        self.register_pushButton.setText(_translate("Form", "注册"))
        self.label.setText(_translate("Form", "用户注册"))
