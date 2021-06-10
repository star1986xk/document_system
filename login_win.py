import sys
from UI.ui_login import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal
from settings import USERNAME, PASSWORD


class LoginWin(Ui_Dialog, QDialog):
    Sig_login = pyqtSignal()

    def __init__(self, parent=None):
        '''
        程序初始化
        :param parent:
        '''
        super().__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)  # 窗口无边框

        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_close.clicked.connect(self.quit)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False

    # 登陆
    def login(self):
        username = self.lineEdit_username.text().strip()
        password = self.lineEdit_password.text().strip()
        if username and password:

            if username == USERNAME and password == PASSWORD:
                self.Sig_login.emit()
                self.hide()
            else:
                QMessageBox.about(self, '提示', '账号或密码错误！')

    # 关闭
    def quit(self):
        sys.exit(0)
