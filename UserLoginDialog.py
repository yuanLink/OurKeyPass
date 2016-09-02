from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ui_UserLoginDialog
from MainWindow import MainWindow
import sys


class UserLoginDialog(QDialog, ui_UserLoginDialog.Ui_L):
    def __init__(self, parent=None):
        super(UserLoginDialog, self).__init__(parent)
        self.setupUi(self)
        self.LoginOKButton.setEnabled(False)
        self.LoginOKButton.setFocusPolicy(Qt.NoFocus)
        self.LoginCancelButton.setFocusPolicy(Qt.NoFocus)
        self.setWindowTitle('Login')
        self.updateUi()

    def on_userNameLogin_textEdited(self):
        self.updateUi()

    def on_userPasswordLogin_textEdited(self):
        self.updateUi()

    def on_LoginOKButton_clicked(self):
       self.mainWindow = MainWindow()
       self.mainWindow.show()
       self.accept()

    def updateUi(self):
        enable = (not self.userNameLogin.text() == '') and (not
                                                              self.userPasswordLogin.text() == '')
        self.LoginOKButton.setEnabled(enable)

    def ChargeLogin(self):
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