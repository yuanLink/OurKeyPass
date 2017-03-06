from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sql_handle
import ui_MainWindow, NewFileDialog, DeleteListItemDialog
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
        # 这个row表示的是当前选中的item所在的行
        self.row = 0

        # 这里要在数据库中尝试读入数据，然后检查是否有可以添加的部分
        table_name_list = self.sqlHandle.query_all(table_name)
        print('there are %d user in table'%len(table_name_list))

        for name,passwd,remark in table_name_list:
            self.userNameList.addItem(name)
            # # 对密码进行解码
            # decode_passwd =  self.pcfgEncode.pcfg_decode(passwd)
            self.userPasswordList.addItem(passwd)
            self.userRemarkList.addItem(remark)

    def on_AddButton_clicked(self):
        self.NewFile = NewFileDialog.NewFileDialog(mainWindow = self, sql = self.sqlHandle)
        self.NewFile.show()

    # 修改了该函数的功能，转为点击屏幕上的某一行的内容，点击删除后将其删除
    def on_DeleteButton_clicked(self):
        self.DeleteListItemDialog = DeleteListItemDialog.DeleteListItemDialog(mainWindow = self, sql = self.sqlHandle)
        self.DeleteListItemDialog.show()

    def clickedTheUserNameListItem(self):
        """
        检测此时选中的姓名item，并且得到所在行
        """
        temp_item = self.userNameList.currentItem()
        self.row = self.userNameList.row(temp_item)
        print("now the row is %d"%self.row)

    def clickedThePasswordListItem(self):
        """
        检测此时选中的密码item，并且得到所在行
        """
        temp_item = self.userPasswordList.currentItem()
        self.row = self.userPasswordList.row(temp_item)
        print("now the row is %d"%self.row)

    def clickedTheRemarkListItem(self):
        """
        检测此时选中的备注item，并且得到所在行
        """
        temp_item = self.userRemarkList.currentItem()
        self.row = self.userRemarkList.row(temp_item)
        print("now the row is %d"%self.row)

    def UpdateUi(self):
        #TODO
        """
        此处用于读取文件并且更新listwidget中显示的数据
        :return:
        """
