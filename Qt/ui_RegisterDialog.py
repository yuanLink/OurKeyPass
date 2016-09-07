# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegisterDialog(object):
    def setupUi(self, RegisterDialog):
        RegisterDialog.setObjectName("RegisterDialog")
        RegisterDialog.resize(320, 240)
        self.widget = QtWidgets.QWidget(RegisterDialog)
        self.widget.setGeometry(QtCore.QRect(70, 70, 235, 133))
        self.widget.setObjectName("widget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.userNameRegister = QtWidgets.QLineEdit(self.widget)
        self.userNameRegister.setObjectName("userNameRegister")
        self.horizontalLayout.addWidget(self.userNameRegister)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.userPasswordRegister = QtWidgets.QLineEdit(self.widget)
        self.userPasswordRegister.setObjectName("userPasswordRegister")
        self.horizontalLayout_2.addWidget(self.userPasswordRegister)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(70, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.RegisterOKButton = QtWidgets.QPushButton(self.widget)
        self.RegisterOKButton.setObjectName("RegisterOKButton")
        self.horizontalLayout_3.addWidget(self.RegisterOKButton)
        self.RegisterCancelButton = QtWidgets.QPushButton(self.widget)
        self.RegisterCancelButton.setObjectName("RegisterCancelButton")
        self.horizontalLayout_3.addWidget(self.RegisterCancelButton)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.label.setBuddy(self.userNameRegister)
        self.label_2.setBuddy(self.userPasswordRegister)

        self.retranslateUi(RegisterDialog)
        self.RegisterCancelButton.clicked.connect(RegisterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RegisterDialog)

    def retranslateUi(self, RegisterDialog):
        _translate = QtCore.QCoreApplication.translate
        RegisterDialog.setWindowTitle(_translate("RegisterDialog", "Register"))
        self.label.setText(_translate("RegisterDialog", "用户名"))
        self.label_2.setText(_translate("RegisterDialog", "密码  "))
        self.RegisterOKButton.setText(_translate("RegisterDialog", "OK"))
        self.RegisterCancelButton.setText(_translate("RegisterDialog", "Cancel"))

