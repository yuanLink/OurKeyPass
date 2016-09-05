# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserLoginDialog.ui'
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

class Ui_L(object):
    def setupUi(self, L):
        L.setObjectName(_fromUtf8("L"))
        L.resize(320, 240)
        self.widget = QtGui.QWidget(L)
        self.widget.setGeometry(QtCore.QRect(60, 60, 237, 164))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(50, -1, -1, -1)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.LoginOKButton = QtGui.QPushButton(self.widget)
        self.LoginOKButton.setObjectName(_fromUtf8("LoginOKButton"))
        self.horizontalLayout_5.addWidget(self.LoginOKButton)
        self.LoginCancelButton = QtGui.QPushButton(self.widget)
        self.LoginCancelButton.setObjectName(_fromUtf8("LoginCancelButton"))
        self.horizontalLayout_5.addWidget(self.LoginCancelButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.userNameLogin = QtGui.QLineEdit(self.widget)
        self.userNameLogin.setObjectName(_fromUtf8("userNameLogin"))
        self.horizontalLayout_3.addWidget(self.userNameLogin)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.userPasswordLogin = QtGui.QLineEdit(self.widget)
        self.userPasswordLogin.setObjectName(_fromUtf8("userPasswordLogin"))
        self.horizontalLayout_4.addWidget(self.userPasswordLogin)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.verticalLayout)
        self.registerButton = QtGui.QPushButton(self.widget)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.registerButton)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.LabelRole, self.formLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_2.setItem(0, QtGui.QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout_2.setItem(1, QtGui.QFormLayout.LabelRole, spacerItem1)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.registerButton.raise_()
        self.label_4.raise_()
        self.userNameLogin.raise_()
        self.label_3.raise_()
        self.userPasswordLogin.raise_()
        self.label_4.setBuddy(L.userNameLogin)
        self.label_3.setBuddy(L.userPasswordLogin)

        self.retranslateUi(L)
        QtCore.QObject.connect(self.LoginCancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), L.reject)
        QtCore.QMetaObject.connectSlotsByName(L)

    def retranslateUi(self, L):
        L.setWindowTitle(_translate("L", "Dialog", None))
        self.LoginOKButton.setText(_translate("L", "OK", None))
        self.LoginCancelButton.setText(_translate("L", "Cancel", None))
        self.label_4.setText(_translate("L", "用户名", None))
        self.label_3.setText(_translate("L", "密码  ", None))
        self.registerButton.setText(_translate("L", "注册", None))

