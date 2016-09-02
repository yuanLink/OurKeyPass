from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ui_NewFileDialog
import MainWindow

class NewFileDialog(QDialog, ui_NewFileDialog.Ui_new_file_dialog, mainWindow = MainWindow.MainWindow):
    def __init__(self, parent=None):
        super(NewFileDialog, self).__init__(parent)
        self.setupUi(self)
        self.NewFileOKButton.setEnabled(False)
        self.NewFileOKButton.setFocusPolicy(Qt.NoFocus)
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
            self.userNameList.addItem(self.userNameInput.text())
            self.userPasswordList.addItem(self.userPasswordInput.text())
            self.userMemorandumList.addItem(self.userMemoryInput.text())
            self.accept()
    def CheckSave(self):
        return True
