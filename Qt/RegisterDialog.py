from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ui_RegisterDialog
from UserLoginDialog import UserLoginDialog

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
            self.login = UserLoginDialog()
            self.login.show()
            self.accept()
    def on_RegisterCancelButton_clicked(self):
            self.login = UserLoginDialog()
            self.login.show()
            self.accept()

    def ChargeRegister(self):
        return True