# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterDialog.ui'
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

class Ui_RegisterDialog(object):
    def setupUi(self, RegisterDialog):
        RegisterDialog.setObjectName(_fromUtf8("RegisterDialog"))
        RegisterDialog.resize(320, 240)
        self.widget = QtGui.QWidget(RegisterDialog)
        self.widget.setGeometry(QtCore.QRect(70, 70, 235, 133))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout_2 = QtGui.QFormLayout(self.widget)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.userNameRegister = QtGui.QLineEdit(self.widget)
        self.userNameRegister.setObjectName(_fromUtf8("userNameRegister"))
        self.horizontalLayout.addWidget(self.userNameRegister)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.userPasswordRegister = QtGui.QLineEdit(self.widget)
        self.userPasswordRegister.setObjectName(_fromUtf8("userPasswordRegister"))
        self.horizontalLayout_2.addWidget(self.userPasswordRegister)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout.setItem(0, QtGui.QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtGui.QFormLayout.LabelRole, spacerItem1)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.LabelRole, self.formLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(70, -1, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.RegisterOKButton = QtGui.QPushButton(self.widget)
        self.RegisterOKButton.setObjectName(_fromUtf8("RegisterOKButton"))
        self.horizontalLayout_3.addWidget(self.RegisterOKButton)
        self.RegisterCancelButton = QtGui.QPushButton(self.widget)
        self.RegisterCancelButton.setObjectName(_fromUtf8("RegisterCancelButton"))
        self.horizontalLayout_3.addWidget(self.RegisterCancelButton)
        self.formLayout_2.setLayout(1, QtGui.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.label.setBuddy(self.userNameRegister)
        self.label_2.setBuddy(self.userPasswordRegister)

        self.retranslateUi(RegisterDialog)
        QtCore.QObject.connect(self.RegisterCancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), RegisterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RegisterDialog)

    def retranslateUi(self, RegisterDialog):
        RegisterDialog.setWindowTitle(_translate("RegisterDialog", "Register", None))
        self.label.setText(_translate("RegisterDialog", "用户名", None))
        self.label_2.setText(_translate("RegisterDialog", "密码  ", None))
        self.RegisterOKButton.setText(_translate("RegisterDialog", "OK", None))
        self.RegisterCancelButton.setText(_translate("RegisterDialog", "Cancel", None))

