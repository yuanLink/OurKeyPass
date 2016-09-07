from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import ui_UserLoginDialog
from MainWindow import MainWindow
import sys
import sql_handle


class UserLoginDialog(QDialog, ui_UserLoginDialog.Ui_L):
    def __init__(self, parent=None):
        super(UserLoginDialog, self).__init__(parent)
        self.setupUi(self)
        self.LoginOKButton.setEnabled(False)
        self.LoginCancelButton.setFocusPolicy(Qt.NoFocus)
        self.registerButton.setFocusPolicy(Qt.NoFocus)
        self.setWindowTitle('Login')
        self.updateUi()

    def on_userNameLogin_textEdited(self):
        self.updateUi()

    def on_userPasswordLogin_textEdited(self):
        self.updateUi()

    def on_LoginOKButton_clicked(self):
        name = self.userNameLogin.text()
        passwd = self.userPasswordLogin.text()
        self.sql_handle = sql_handle.SqlHandle(name, key = passwd)
        self.mainWindow = MainWindow(table_name = name, password = passwd, sql = self.sql_handle)
        self.mainWindow.show()
        self.accept()

    def updateUi(self):
        """
        判断是否输入为空
        :return:
        """
        enable = (not self.userNameLogin.text() == '') and (not
                                                              self.userPasswordLogin.text() == '')
        self.LoginOKButton.setEnabled(enable)

    def ChargeLogin(self):
        #TODO 进行登陆判断
        return True

    def on_registerButton_clicked(self):
        from RegisterDialog import RegisterDialog
        self.register = RegisterDialog()
        self.register.show()
        self.accept()



app = QApplication(sys.argv)
loginDialog = UserLoginDialog()
loginDialog.show()
app.exec_()