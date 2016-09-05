# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeleteDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DeleteDialog(object):
    def setupUi(self, DeleteDialog):
        DeleteDialog.setObjectName(_fromUtf8("DeleteDialog"))
        DeleteDialog.resize(320, 240)
        self.layoutWidget = QtGui.QWidget(DeleteDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 60, 187, 85))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.DeleteUserNameEdit = QtGui.QLineEdit(self.layoutWidget)
        self.DeleteUserNameEdit.setObjectName(_fromUtf8("DeleteUserNameEdit"))
        self.horizontalLayout.addWidget(self.DeleteUserNameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.DeleteUserPasswordEdit = QtGui.QLineEdit(self.layoutWidget)
        self.DeleteUserPasswordEdit.setObjectName(_fromUtf8("DeleteUserPasswordEdit"))
        self.horizontalLayout_2.addWidget(self.DeleteUserPasswordEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.verticalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.DeleteOKButton = QtGui.QPushButton(self.layoutWidget)
        self.DeleteOKButton.setObjectName(_fromUtf8("DeleteOKButton"))
        self.horizontalLayout_3.addWidget(self.DeleteOKButton)
        self.DeleteCancelButton = QtGui.QPushButton(self.layoutWidget)
        self.DeleteCancelButton.setObjectName(_fromUtf8("DeleteCancelButton"))
        self.horizontalLayout_3.addWidget(self.DeleteCancelButton)
        self.formLayout.setLayout(1, QtGui.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.label.setBuddy(self.DeleteUserNameEdit)
        self.label_2.setBuddy(self.DeleteUserPasswordEdit)

        self.retranslateUi(DeleteDialog)
        QtCore.QMetaObject.connectSlotsByName(DeleteDialog)

    def retranslateUi(self, DeleteDialog):
        DeleteDialog.setWindowTitle(_translate("DeleteDialog", "删除窗口", None))
        self.label.setText(_translate("DeleteDialog", "用户名", None))
        self.label_2.setText(_translate("DeleteDialog", "密码  ", None))
        self.DeleteOKButton.setText(_translate("DeleteDialog", "确认删除", None))
        self.DeleteCancelButton.setText(_translate("DeleteDialog", "取消", None))

