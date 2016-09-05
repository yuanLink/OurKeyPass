from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ui_NewFileDialog
import MainWindow

class NewFileDialog(QDialog, ui_NewFileDialog.Ui_new_file_dialog):
    def __init__(self, parent=None ,mainWindow=MainWindow):
        super(NewFileDialog, self).__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.NewFileOKButton.setEnabled(False)
        self.CheckCount = True
        self.NewFileCancelButton.setFocusPolicy(Qt.NoFocus)
        self.updateUi()

    def on_userNameInput_textEdited(self):
        self.updateUi()

    def on_userPasswordInput_textEdited(self):
        self.updateUi()

    def updateUi(self):
        enable = (not self.userNameInput.text() == '') and (not
                                                               self.userPasswordInput.text() == '')
        self.NewFileOKButton.setEnabled(enable)
    def on_NewFileOKButton_clicked(self):
        if(self.CheckSave()):
            self.mainWindow.userNameList.addItem(self.userNameInput.text())
            self.mainWindow.userPasswordList.addItem(self.userPasswordInput.text())
            self.mainWindow.userRemarkList.addItem(self.userRemarkInput.text())
            self.CheckCount = False
            self.accept()
    def on_NewFileCancelButton_clicked(self):
        self.accept()
    def CheckSave(self):
        #TODO
        """
        进行密码存储和加密，成功返回True,失败返回False，注意 是self.CheckCount
        :return:
        """
        return self.CheckCount
