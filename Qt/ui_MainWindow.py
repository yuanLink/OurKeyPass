# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 731, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.userNameList = QtWidgets.QListWidget(self.layoutWidget)
        self.userNameList.setObjectName("userNameList")
        self.verticalLayout.addWidget(self.userNameList)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.userPasswordList = QtWidgets.QListWidget(self.layoutWidget)
        self.userPasswordList.setObjectName("userPasswordList")
        self.verticalLayout_2.addWidget(self.userPasswordList)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.userRemarkList = QtWidgets.QListWidget(self.layoutWidget)
        self.userRemarkList.setObjectName("userRemarkList")
        self.verticalLayout_3.addWidget(self.userRemarkList)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(560, 490, 160, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.AddButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.AddButton.setAutoFillBackground(False)
        self.AddButton.setAutoDefault(False)
        self.AddButton.setObjectName("AddButton")
        self.horizontalLayout_2.addWidget(self.AddButton)
        self.DeleteButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.DeleteButton.setObjectName("DeleteButton")
        self.horizontalLayout_2.addWidget(self.DeleteButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuDasd = QtWidgets.QMenu(self.menubar)
        self.menuDasd.setObjectName("menuDasd")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.save_nemu = QtWidgets.QAction(MainWindow)
        self.save_nemu.setObjectName("save_nemu")
        self.load_nemu = QtWidgets.QAction(MainWindow)
        self.load_nemu.setObjectName("load_nemu")
        self.new_folder_nemu = QtWidgets.QAction(MainWindow)
        self.new_folder_nemu.setObjectName("new_folder_nemu")
        self.new_entry_nemu = QtWidgets.QAction(MainWindow)
        self.new_entry_nemu.setObjectName("new_entry_nemu")
        self.undo_nemu = QtWidgets.QAction(MainWindow)
        self.undo_nemu.setObjectName("undo_nemu")
        self.Redo_nemu = QtWidgets.QAction(MainWindow)
        self.Redo_nemu.setObjectName("Redo_nemu")
        self.cut_nemu = QtWidgets.QAction(MainWindow)
        self.cut_nemu.setObjectName("cut_nemu")
        self.copy_nemu = QtWidgets.QAction(MainWindow)
        self.copy_nemu.setObjectName("copy_nemu")
        self.paste_nemu = QtWidgets.QAction(MainWindow)
        self.paste_nemu.setObjectName("paste_nemu")
        self.rename_nemu = QtWidgets.QAction(MainWindow)
        self.rename_nemu.setObjectName("rename_nemu")
        self.delete_nemu = QtWidgets.QAction(MainWindow)
        self.delete_nemu.setObjectName("delete_nemu")
        self.find_nemu = QtWidgets.QAction(MainWindow)
        self.find_nemu.setObjectName("find_nemu")
        self.find_next_nemu = QtWidgets.QAction(MainWindow)
        self.find_next_nemu.setObjectName("find_next_nemu")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNewfile = QtWidgets.QAction(MainWindow)
        self.actionNewfile.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/yanghuan/.designer/backup/Icon/floder1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewfile.setIcon(icon)
        self.actionNewfile.setObjectName("actionNewfile")
        self.actionSavefile = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/yanghuan/.designer/backup/Icon/f13.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionSavefile.setIcon(icon1)
        self.actionSavefile.setObjectName("actionSavefile")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.menuDasd.addAction(self.new_entry_nemu)
        self.menuDasd.addSeparator()
        self.menuDasd.addAction(self.save_nemu)
        self.menuDasd.addAction(self.actionDelete)
        self.menuDasd.addSeparator()
        self.menuDasd.addAction(self.actionExit)
        self.menubar.addAction(self.menuDasd.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "用户名"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.label_3.setText(_translate("MainWindow", "备注"))
        self.AddButton.setText(_translate("MainWindow", "添加"))
        self.DeleteButton.setText(_translate("MainWindow", "删除"))
        self.menuDasd.setTitle(_translate("MainWindow", "File"))
        self.save_nemu.setText(_translate("MainWindow", "Save"))
        self.save_nemu.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.load_nemu.setText(_translate("MainWindow", "Load"))
        self.load_nemu.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.new_folder_nemu.setText(_translate("MainWindow", "New folder"))
        self.new_folder_nemu.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.new_entry_nemu.setText(_translate("MainWindow", "New entry"))
        self.new_entry_nemu.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.undo_nemu.setText(_translate("MainWindow", "Undo"))
        self.undo_nemu.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.Redo_nemu.setText(_translate("MainWindow", "Redo"))
        self.Redo_nemu.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.cut_nemu.setText(_translate("MainWindow", "Cut"))
        self.cut_nemu.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.copy_nemu.setText(_translate("MainWindow", "Copy"))
        self.paste_nemu.setText(_translate("MainWindow", "Paste"))
        self.paste_nemu.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.rename_nemu.setText(_translate("MainWindow", "Rename"))
        self.rename_nemu.setShortcut(_translate("MainWindow", "F2"))
        self.delete_nemu.setText(_translate("MainWindow", "Delete"))
        self.find_nemu.setText(_translate("MainWindow", "Find"))
        self.find_nemu.setShortcut(_translate("MainWindow", "F3"))
        self.find_next_nemu.setText(_translate("MainWindow", "Find next"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionNewfile.setText(_translate("MainWindow", "newfile"))
        self.actionNewfile.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSavefile.setText(_translate("MainWindow", "savefile"))
        self.actionSavefile.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))

