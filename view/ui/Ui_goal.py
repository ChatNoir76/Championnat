# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_Goal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_goal(object):
    def setupUi(self, Dialog_goal):
        Dialog_goal.setObjectName("Dialog_goal")
        Dialog_goal.resize(251, 220)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_goal)
        self.buttonBox.setGeometry(QtCore.QRect(20, 180, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox_team = QtWidgets.QComboBox(Dialog_goal)
        self.comboBox_team.setGeometry(QtCore.QRect(10, 40, 231, 22))
        self.comboBox_team.setEditable(False)
        self.comboBox_team.setCurrentText("")
        self.comboBox_team.setModelColumn(0)
        self.comboBox_team.setObjectName("comboBox_team")
        self.label = QtWidgets.QLabel(Dialog_goal)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_goal)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog_goal)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 71, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_goalscorer = QtWidgets.QComboBox(Dialog_goal)
        self.comboBox_goalscorer.setGeometry(QtCore.QRect(10, 100, 231, 22))
        self.comboBox_goalscorer.setEditable(False)
        self.comboBox_goalscorer.setModelColumn(0)
        self.comboBox_goalscorer.setObjectName("comboBox_goalscorer")
        self.comboBox_goalscorer.addItem("")
        self.comboBox_assistance = QtWidgets.QComboBox(Dialog_goal)
        self.comboBox_assistance.setGeometry(QtCore.QRect(10, 150, 231, 22))
        self.comboBox_assistance.setEditable(False)
        self.comboBox_assistance.setModelColumn(0)
        self.comboBox_assistance.setObjectName("comboBox_assistance")
        self.comboBox_assistance.addItem("")

        self.retranslateUi(Dialog_goal)
        self.buttonBox.accepted.connect(Dialog_goal.accept)
        self.buttonBox.rejected.connect(Dialog_goal.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_goal)

    def retranslateUi(self, Dialog_goal):
        _translate = QtCore.QCoreApplication.translate
        Dialog_goal.setWindowTitle(_translate("Dialog_goal", "save goalscorer"))
        self.label.setText(_translate("Dialog_goal", "Goals for team:"))
        self.label_2.setText(_translate("Dialog_goal", "scorer :"))
        self.label_3.setText(_translate("Dialog_goal", "assistance :"))
        self.comboBox_goalscorer.setCurrentText(_translate("Dialog_goal", "Own Goals"))
        self.comboBox_goalscorer.setItemText(0, _translate("Dialog_goal", "Own Goals"))
        self.comboBox_assistance.setCurrentText(_translate("Dialog_goal", "None"))
        self.comboBox_assistance.setItemText(0, _translate("Dialog_goal", "None"))
