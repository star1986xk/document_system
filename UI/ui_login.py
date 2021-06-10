# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(436, 261)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/word.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("#widget{\n"
"    border-image: url(:/newPrefix/img/bp.png);\n"
"}\n"
"#widget_2{\n"
"    border-image: url(:/newPrefix/img/bp2.jpg);\n"
"}\n"
"#label{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"#tableWidget{\n"
"    background-color: rgb(255, 255, 255,150);\n"
"}\n"
"QPushButton{\n"
"color:rgb(255, 255, 255);\n"
"border-style:none;border-radius: 5px;\n"
"background-color:rgb(55, 100, 111);\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(255, 255, 255);\n"
"background-color: rgb(158, 200, 205);\n"
"}\n"
"QPushButton:pressed {  \n"
"    /* 改变背景色 */  \n"
"    background-color:rgb(55, 100, 111);\n"
"    /* 改变边框风格 */  \n"
"    border-style:inset;  \n"
"    /* 使文字有一点移动 */  \n"
"    padding-left:1px;  \n"
"    padding-top:1px;  \n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(75, 115, 140);\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setMinimumSize(QtCore.QSize(80, 30))
        self.label_2.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_username = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_username.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_username.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.horizontalLayout.addWidget(self.lineEdit_username)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setMinimumSize(QtCore.QSize(80, 30))
        self.label_3.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_password.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_3.addWidget(self.lineEdit_password)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_login = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_login.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_login.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout_4.addWidget(self.pushButton_login)
        self.pushButton_close = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_close.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_close.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_4.addWidget(self.pushButton_close)
        self.verticalLayout.addWidget(self.widget_5)
        self.verticalLayout_2.addWidget(self.widget_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "登陆"))
        self.label.setText(_translate("Dialog", "档案文件系统"))
        self.label_2.setText(_translate("Dialog", "用户名"))
        self.label_3.setText(_translate("Dialog", "密  码"))
        self.pushButton_login.setText(_translate("Dialog", "登  陆"))
        self.pushButton_close.setText(_translate("Dialog", "关  闭"))
import image_rc
