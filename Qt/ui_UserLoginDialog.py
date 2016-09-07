# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserLoginDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_L(object):
    def setupUi(self, L):
        L.setObjectName("L")
        L.resize(320, 240)
        self.layoutWidget = QtWidgets.QWidget(L)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 60, 237, 164))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(50, -1, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.LoginOKButton = QtWidgets.QPushButton(self.layoutWidget)
        self.LoginOKButton.setObjectName("LoginOKButton")
        self.horizontalLayout_5.addWidget(self.LoginOKButton)
        self.LoginCancelButton = QtWidgets.QPushButton(self.layoutWidget)
        self.LoginCancelButton.setObjectName("LoginCancelButton")
        self.horizontalLayout_5.addWidget(self.LoginCancelButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.userNameLogin = QtWidgets.QLineEdit(self.layoutWidget)
        self.userNameLogin.setObjectName("userNameLogin")
        self.horizontalLayout_3.addWidget(self.userNameLogin)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.userPasswordLogin = QtWidgets.QLineEdit(self.layoutWidget)
        self.userPasswordLogin.setObjectName("userPasswordLogin")
        self.horizontalLayout_4.addWidget(self.userPasswordLogin)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.registerButton = QtWidgets.QPushButton(self.layoutWidget)
        self.registerButton.setObjectName("registerButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.registerButton)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_2.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.label_4.setBuddy(self.userNameLogin)
        self.label_3.setBuddy(self.userPasswordLogin)

        self.retranslateUi(L)
        self.LoginCancelButton.clicked.connect(L.reject)
        QtCore.QMetaObject.connectSlotsByName(L)

    def retranslateUi(self, L):
        _translate = QtCore.QCoreApplication.translate
        L.setWindowTitle(_translate("L", "Dialog"))
        self.LoginOKButton.setText(_translate("L", "OK"))
        self.LoginCancelButton.setText(_translate("L", "Cancel"))
        self.label_4.setText(_translate("L", "用户名"))
        self.label_3.setText(_translate("L", "密码  "))
        self.registerButton.setText(_translate("L", "注册"))

