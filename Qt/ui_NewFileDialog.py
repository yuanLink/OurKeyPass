# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewFileDialog.ui'
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

class Ui_new_file_dialog(object):
    def setupUi(self, new_file_dialog):
        new_file_dialog.setObjectName(_fromUtf8("new_file_dialog"))
        new_file_dialog.resize(320, 240)
        self.layoutWidget = QtGui.QWidget(new_file_dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(61, 52, 207, 115))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.userNameInput = QtGui.QLineEdit(self.layoutWidget)
        self.userNameInput.setObjectName(_fromUtf8("userNameInput"))
        self.horizontalLayout.addWidget(self.userNameInput)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.userPasswordInput = QtGui.QLineEdit(self.layoutWidget)
        self.userPasswordInput.setObjectName(_fromUtf8("userPasswordInput"))
        self.horizontalLayout_2.addWidget(self.userPasswordInput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.userRemarkInput = QtGui.QLineEdit(self.layoutWidget)
        self.userRemarkInput.setObjectName(_fromUtf8("userRemarkInput"))
        self.horizontalLayout_4.addWidget(self.userRemarkInput)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.verticalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.NewFileOKButton = QtGui.QPushButton(self.layoutWidget)
        self.NewFileOKButton.setObjectName(_fromUtf8("NewFileOKButton"))
        self.horizontalLayout_3.addWidget(self.NewFileOKButton)
        self.NewFileCancelButton = QtGui.QPushButton(self.layoutWidget)
        self.NewFileCancelButton.setObjectName(_fromUtf8("NewFileCancelButton"))
        self.horizontalLayout_3.addWidget(self.NewFileCancelButton)
        self.formLayout.setLayout(1, QtGui.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.label_2.setBuddy(self.userNameInput)
        self.label.setBuddy(self.userPasswordInput)
        self.label_3.setBuddy(self.userRemarkInput)

        self.retranslateUi(new_file_dialog)
        QtCore.QObject.connect(self.NewFileCancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), new_file_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(new_file_dialog)

    def retranslateUi(self, new_file_dialog):
        new_file_dialog.setWindowTitle(_translate("new_file_dialog", "new file", None))
        self.label_2.setText(_translate("new_file_dialog", "password:", None))
        self.label.setText(_translate("new_file_dialog", "username:", None))
        self.label_3.setText(_translate("new_file_dialog", "备注", None))
        self.NewFileOKButton.setText(_translate("new_file_dialog", "OK", None))
        self.NewFileCancelButton.setText(_translate("new_file_dialog", "Cancel", None))

