# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeleteListItemDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeleteListItemDialog(object):
    def setupUi(self, DeleteListItemDialog):
        DeleteListItemDialog.setObjectName("DeleteListItemDialog")
        DeleteListItemDialog.resize(325, 213)
        self.DeleteListItemDialog_label = QtWidgets.QLabel(DeleteListItemDialog)
        self.DeleteListItemDialog_label.setGeometry(QtCore.QRect(110, 50, 131, 41))
        self.DeleteListItemDialog_label.setObjectName("DeleteListItemDialog_label")
        self.OkButton = QtWidgets.QPushButton(DeleteListItemDialog)
        self.OkButton.setGeometry(QtCore.QRect(30, 120, 91, 31))
        self.OkButton.setObjectName("OkButton")
        self.CancelButton = QtWidgets.QPushButton(DeleteListItemDialog)
        self.CancelButton.setGeometry(QtCore.QRect(200, 120, 91, 31))
        self.CancelButton.setObjectName("CancelButton")

        self.retranslateUi(DeleteListItemDialog)
        self.OkButton.clicked.connect(DeleteListItemDialog.deleteItemAndClose)
        self.CancelButton.clicked.connect(DeleteListItemDialog.closeDialog)
        QtCore.QMetaObject.connectSlotsByName(DeleteListItemDialog)

    def retranslateUi(self, DeleteListItemDialog):
        _translate = QtCore.QCoreApplication.translate
        DeleteListItemDialog.setWindowTitle(_translate("DeleteListItemDialog", "删除用户"))
        self.DeleteListItemDialog_label.setText(_translate("DeleteListItemDialog", "是否删除该选中项？\n"
"（默认为第一项）"))
        self.OkButton.setText(_translate("DeleteListItemDialog", "确认"))
        self.CancelButton.setText(_translate("DeleteListItemDialog", "取消"))

