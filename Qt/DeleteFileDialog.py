from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import ui_DeleteDialog
import MainWindow
import sql_handle

class DeleteFileDialog(QDialog, ui_DeleteDialog.Ui_DeleteDialog):
    def __init__(self, parent=None ,mainWindow=MainWindow, sql = ''):
        super(DeleteFileDialog, self).__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.DeleteOKButton.setEnabled(False)
        self.CheckCount = True
        self.DeleteCancelButton.setFocusPolicy(Qt.NoFocus)
        self.updateUi()

    def on_DeleteUserNameEdit_textEdited(self):
        self.updateUi()

    def on_DeleteUserPasswordEdit_textEdited(self):
        self.updateUi()

    def updateUi(self):
        enable = (not self.DeleteUserNameEdit.text() == '') and (not
                                                               self.DeleteUserPasswordEdit.text() == '')
        self.DeleteOKButton.setEnabled(enable)
    def on_DeleteOKButton_clicked(self):
        if(self.CheckLoad()):
            self.mainWindow
            self.CheckCount = False
            self.accept()
    def CheckLoad(self):
        #TODO
        """"
            此处是向文件搜索对应的用户名和密码，如果存在并且删除成功，则将self.CheckCount的值设为True
            否则设为False
        """
        return self.CheckCount