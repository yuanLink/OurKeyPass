# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewFileDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_new_file_dialog(object):
    def setupUi(self, new_file_dialog):
        new_file_dialog.setObjectName("new_file_dialog")
        new_file_dialog.resize(320, 240)
        self.layoutWidget = QtWidgets.QWidget(new_file_dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(61, 52, 207, 115))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.userNameInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.userNameInput.setObjectName("userNameInput")
        self.horizontalLayout.addWidget(self.userNameInput)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.userPasswordInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.userPasswordInput.setObjectName("userPasswordInput")
        self.horizontalLayout_2.addWidget(self.userPasswordInput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.userRemarkInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.userRemarkInput.setObjectName("userRemarkInput")
        self.horizontalLayout_4.addWidget(self.userRemarkInput)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.NewFileOKButton = QtWidgets.QPushButton(self.layoutWidget)
        self.NewFileOKButton.setObjectName("NewFileOKButton")
        self.horizontalLayout_3.addWidget(self.NewFileOKButton)
        self.NewFileCancelButton = QtWidgets.QPushButton(self.layoutWidget)
        self.NewFileCancelButton.setObjectName("NewFileCancelButton")
        self.horizontalLayout_3.addWidget(self.NewFileCancelButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.label_2.setBuddy(self.userNameInput)
        self.label.setBuddy(self.userPasswordInput)
        self.label_3.setBuddy(self.userRemarkInput)

        self.retranslateUi(new_file_dialog)
        self.NewFileCancelButton.clicked.connect(new_file_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(new_file_dialog)

    def retranslateUi(self, new_file_dialog):
        _translate = QtCore.QCoreApplication.translate
        new_file_dialog.setWindowTitle(_translate("new_file_dialog", "new file"))
        self.label_2.setText(_translate("new_file_dialog", "username:"))
        self.label.setText(_translate("new_file_dialog", "password:"))
        self.label_3.setText(_translate("new_file_dialog", "备注"))
        self.NewFileOKButton.setText(_translate("new_file_dialog", "OK"))
        self.NewFileCancelButton.setText(_translate("new_file_dialog", "Cancel"))

