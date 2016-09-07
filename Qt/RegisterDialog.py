from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import ui_RegisterDialog
from UserLoginDialog import UserLoginDialog
from sql_handle import SqlHandle

DATABASE_NAME = "user_data.db"
class RegisterDialog(QDialog, ui_RegisterDialog.Ui_RegisterDialog):
    def __init__(self, parent=None):
        super(RegisterDialog, self).__init__(parent)
        self.setupUi(self)
        self.RegisterOKButton.setEnabled(False)
        self.RegisterOKButton.setFocusPolicy(Qt.NoFocus)
        self.RegisterCancelButton.setFocusPolicy(Qt.NoFocus)
        self.updateUi()
        


    def on_userNameRegister_textEdited(self):
        self.updateUi()


    def on_userPasswordRegister_textEdited(self):
        self.updateUi()

        # def on_LoginOKButton__clicked(self):


    def updateUi(self):
        enable = (not self.userNameRegister.text() == '') and (not
                                                            self.userPasswordRegister.text() == '')
        self.RegisterOKButton.setEnabled(enable)

    def on_RegisterOKButton_clicked(self):
        if(self.ChargeRegister()):
            registName = self.userNameRegister.text()
            self.login = UserLoginDialog()

            # 进行打开数据库并且建表的操作(库的名字就是用户的名字)
            self.sqlHandle = SqlHandle(registName)
            self.sqlHandle.create_tb(registName)

            self.login.show()
            self.accept()
    def on_RegisterCancelButton_clicked(self):
            self.login = UserLoginDialog()
            self.login.show()
            self.accept()

    def ChargeRegister(self):
        return True