# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(614, 374)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/word.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#Form{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"#widget{\n"
"    border-image: url(:/newPrefix/img/bp.png);\n"
"}\n"
"#widget_2{\n"
"    border-image: url(:/newPrefix/img/bp2.jpg);\n"
"}\n"
"#label{\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton{\n"
"border-style:none;border-radius: 10px;\n"
"/*background-color: rgb(200, 200, 200,220);*/\n"
"}\n"
"QToolButton:hover{\n"
"color:rgb(255, 255, 255);\n"
"/*background-color: rgb(150, 150, 150,120);*/\n"
"}\n"
"QToolButton:pressed {  \n"
"    /* 改变背景色 */  \n"
"    /*background-color:rgb(180, 180, 180,120);*/\n"
"    /* 改变边框风格 */  \n"
"    border-style:inset;  \n"
"    /* 使文字有一点移动 */  \n"
"    padding-left:1px;  \n"
"    padding-top:1px;  \n"
"}\n"
"\n"
"QPushButton{\n"
"border-style:none;border-radius: 10px;\n"
"/*background-color: rgb(200, 200, 200,220);*/\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(255, 255, 255);\n"
"/*background-color: rgb(150, 150, 150,120);*/\n"
"}\n"
"QPushButton:pressed {  \n"
"    /* 改变背景色 */  \n"
"    /*background-color:rgb(180, 180, 180,120);*/\n"
"    /* 改变边框风格 */  \n"
"    border-style:inset;  \n"
"    /* 使文字有一点移动 */  \n"
"    padding-left:1px;  \n"
"    padding-top:1px;  \n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius: 5px;\n"
"border: 1px solid #00aaff;\n"
"background-color:rgb(230, 230, 230);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(0, 100))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButton_word = QtWidgets.QToolButton(self.widget_3)
        self.toolButton_word.setMinimumSize(QtCore.QSize(70, 70))
        self.toolButton_word.setMaximumSize(QtCore.QSize(70, 70))
        self.toolButton_word.setIcon(icon)
        self.toolButton_word.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_word.setAutoRepeatDelay(300)
        self.toolButton_word.setAutoRepeatInterval(100)
        self.toolButton_word.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_word.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_word.setObjectName("toolButton_word")
        self.horizontalLayout_2.addWidget(self.toolButton_word)
        self.lineEdit_word = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_word.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_word.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_word.setFont(font)
        self.lineEdit_word.setReadOnly(True)
        self.lineEdit_word.setObjectName("lineEdit_word")
        self.horizontalLayout_2.addWidget(self.lineEdit_word)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toolButton_excel = QtWidgets.QToolButton(self.widget_4)
        self.toolButton_excel.setMinimumSize(QtCore.QSize(70, 70))
        self.toolButton_excel.setMaximumSize(QtCore.QSize(70, 70))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/img/Excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_excel.setIcon(icon1)
        self.toolButton_excel.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_excel.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_excel.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_excel.setObjectName("toolButton_excel")
        self.horizontalLayout_3.addWidget(self.toolButton_excel)
        self.lineEdit_excel = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_excel.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_excel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_excel.setFont(font)
        self.lineEdit_excel.setReadOnly(True)
        self.lineEdit_excel.setObjectName("lineEdit_excel")
        self.horizontalLayout_3.addWidget(self.lineEdit_excel)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.toolButton_run = QtWidgets.QToolButton(self.widget_5)
        self.toolButton_run.setMinimumSize(QtCore.QSize(80, 80))
        self.toolButton_run.setMaximumSize(QtCore.QSize(80, 80))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/img/运行.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_run.setIcon(icon2)
        self.toolButton_run.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_run.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_run.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_run.setObjectName("toolButton_run")
        self.horizontalLayout_4.addWidget(self.toolButton_run)
        self.toolButton_close = QtWidgets.QToolButton(self.widget_5)
        self.toolButton_close.setMinimumSize(QtCore.QSize(80, 80))
        self.toolButton_close.setMaximumSize(QtCore.QSize(80, 80))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/img/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_close.setIcon(icon3)
        self.toolButton_close.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_close.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_close.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_close.setObjectName("toolButton_close")
        self.horizontalLayout_4.addWidget(self.toolButton_close)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "档案文件系统"))
        self.label.setText(_translate("Form", "档案文件系统"))
        self.toolButton_word.setText(_translate("Form", "导入Word"))
        self.toolButton_excel.setText(_translate("Form", "导出Excel"))
        self.toolButton_run.setText(_translate("Form", "运  行"))
        self.toolButton_close.setText(_translate("Form", "退  出"))
import image_rc
