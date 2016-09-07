# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeleteDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeleteDialog(object):
    def setupUi(self, DeleteDialog):
        DeleteDialog.setObjectName("DeleteDialog")
        DeleteDialog.resize(320, 240)
        self.layoutWidget = QtWidgets.QWidget(DeleteDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 60, 187, 85))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.DeleteUserNameEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.DeleteUserNameEdit.setObjectName("DeleteUserNameEdit")
        self.horizontalLayout.addWidget(self.DeleteUserNameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.DeleteUserPasswordEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.DeleteUserPasswordEdit.setObjectName("DeleteUserPasswordEdit")
        self.horizontalLayout_2.addWidget(self.DeleteUserPasswordEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.DeleteOKButton = QtWidgets.QPushButton(self.layoutWidget)
        self.DeleteOKButton.setObjectName("DeleteOKButton")
        self.horizontalLayout_3.addWidget(self.DeleteOKButton)
        self.DeleteCancelButton = QtWidgets.QPushButton(self.layoutWidget)
        self.DeleteCancelButton.setObjectName("DeleteCancelButton")
        self.horizontalLayout_3.addWidget(self.DeleteCancelButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.label.setBuddy(self.DeleteUserNameEdit)
        self.label_2.setBuddy(self.DeleteUserPasswordEdit)

        self.retranslateUi(DeleteDialog)
        QtCore.QMetaObject.connectSlotsByName(DeleteDialog)

    def retranslateUi(self, DeleteDialog):
        _translate = QtCore.QCoreApplication.translate
        DeleteDialog.setWindowTitle(_translate("DeleteDialog", "删除窗口"))
        self.label.setText(_translate("DeleteDialog", "用户名"))
        self.label_2.setText(_translate("DeleteDialog", "密码  "))
        self.DeleteOKButton.setText(_translate("DeleteDialog", "确认删除"))
        self.DeleteCancelButton.setText(_translate("DeleteDialog", "取消"))

