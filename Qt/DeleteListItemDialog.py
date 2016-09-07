from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import ui_DeleteListItemDialog
import MainWindow
import sql_handle

class DeleteListItemDialog(QDialog, ui_DeleteListItemDialog.Ui_DeleteListItemDialog):
    def __init__(self, parent=None ,mainWindow = '', sql = ''):
        super(DeleteListItemDialog, self).__init__(parent)
        self.setupUi(self)
        self.mainWindow = mainWindow
        self.CheckCount = True
        # self.updateUi()

    def on_DeleteOKButton_clicked(self):
        if(self.CheckLoad()):
            # 这里进行数据的删除
            # self.mainWindow.userNameList.row()
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

    def deleteItemAndClose(self):
        """
        点击按钮以后，删除目标item并且关闭当前窗口

        该函数会删除数据在数据库和函数中的相应变量位置
        """

        row = self.mainWindow.row
        # 删除在屏幕上的位置(假如row为-1的时候就不要进行删除)
        if row>=0:  
            temp_item = self.mainWindow.userNameList.takeItem(row)
            self.mainWindow.userPasswordList.takeItem(row)
            self.mainWindow.userRemarkList.takeItem(row)

        # 删除再数据库中的位置
            sql = self.mainWindow.sqlHandle
            sql.delete(temp_item.text())
            
        self.close()

    def closeDialog(self):
        """
        关闭当前对话框
        """

        self.close()

