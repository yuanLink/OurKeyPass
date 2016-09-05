from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ui_MainWindow, NewFileDialog, DeleteFileDialog

class MainWindow(QMainWindow, ui_MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('OurKeyPass')

    def on_AddButton_clicked(self):
        self.NewFile = NewFileDialog.NewFileDialog(mainWindow=self)
        self.NewFile.show()
    def on_DeleteButton_clicked(self):
        self.DeleteFile = DeleteFileDialog.DeleteFileDialog(mainWindow=self)
        self.DeleteFile.show()

    def UpdateUi(self):
        #TODO
        """
        此处用于读取文件并且更新listwidget中显示的数据
        :return:
        """