# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_AddPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_addplayer(object):
    def setupUi(self, Dialog_addplayer):
        Dialog_addplayer.setObjectName("Dialog_addplayer")
        Dialog_addplayer.resize(321, 165)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_addplayer)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_addplayer = QtWidgets.QGroupBox(Dialog_addplayer)
        self.groupBox_addplayer.setMinimumSize(QtCore.QSize(303, 118))
        self.groupBox_addplayer.setMaximumSize(QtCore.QSize(337, 150))
        self.groupBox_addplayer.setObjectName("groupBox_addplayer")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_addplayer)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_addplayer)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)
        self.textEdit_fname = QtWidgets.QTextEdit(self.groupBox_addplayer)
        self.textEdit_fname.setMaximumSize(QtCore.QSize(16777215, 25))
        self.textEdit_fname.setAcceptRichText(False)
        self.textEdit_fname.setPlaceholderText("")
        self.textEdit_fname.setObjectName("textEdit_fname")
        self.gridLayout_5.addWidget(self.textEdit_fname, 0, 1, 1, 1)
        self.textEdit_lname = QtWidgets.QTextEdit(self.groupBox_addplayer)
        self.textEdit_lname.setMaximumSize(QtCore.QSize(16777215, 25))
        self.textEdit_lname.setAcceptRichText(False)
        self.textEdit_lname.setObjectName("textEdit_lname")
        self.gridLayout_5.addWidget(self.textEdit_lname, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_addplayer)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_addplayer, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_addplayer)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog_addplayer)
        self.buttonBox.accepted.connect(Dialog_addplayer.accept)
        self.buttonBox.rejected.connect(Dialog_addplayer.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_addplayer)

    def retranslateUi(self, Dialog_addplayer):
        _translate = QtCore.QCoreApplication.translate
        Dialog_addplayer.setWindowTitle(_translate("Dialog_addplayer", "Dialog"))
        self.groupBox_addplayer.setTitle(_translate("Dialog_addplayer", "Add player"))
        self.label_4.setText(_translate("Dialog_addplayer", "first name :"))
        self.label_5.setText(_translate("Dialog_addplayer", "last name :"))
