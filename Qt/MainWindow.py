from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sql_handle
import ui_MainWindow, NewFileDialog, DeleteFileDialog
# import sys
# sys.path.append("..")
# from pcfg import codec

# import sql_handle

class MainWindow(QMainWindow, ui_MainWindow.Ui_MainWindow):
    def __init__(self, table_name, password, sql = '', parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('OurKeyPass')
        self.sqlHandle = sql
        # self.pcfgEncode = codec.PcfgEncode(password)

        # 这里要在数据库中尝试读入数据，然后检查是否有可以添加的部分
        table_name_list = self.sqlHandle.query(table_name)

        for name,passwd,remark in table_name_list:
            self.userNameList.addItem(name)
            # # 对密码进行解码
            # decode_passwd =  self.pcfgEncode.pcfg_decode(passwd)
            self.userPasswordList.addItem(passwd)
            self.userRemarkList.addItem(remark)

    def on_AddButton_clicked(self):
        self.NewFile = NewFileDialog.NewFileDialog(mainWindow = self, sql = self.sqlHandle)
        self.NewFile.show()

    def on_DeleteButton_clicked(self):
        self.DeleteFile = DeleteFileDialog.DeleteFileDialog(mainWindow = self, sql = self.sqlHandle)
        self.DeleteFile.show()

    def UpdateUi(self):
        #TODO
        """
        此处用于读取文件并且更新listwidget中显示的数据
        :return:
        """
