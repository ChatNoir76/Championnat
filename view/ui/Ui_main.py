# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowsTest001.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(573, 422)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(False)
        self.tabWidget.setMinimumSize(QtCore.QSize(555, 363))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_teampage = QtWidgets.QWidget()
        self.tab_teampage.setObjectName("tab_teampage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_teampage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget_teamslist = QtWidgets.QListWidget(self.tab_teampage)
        self.listWidget_teamslist.setObjectName("listWidget_teamslist")
        self.gridLayout_2.addWidget(self.listWidget_teamslist, 5, 1, 4, 2)
        self.pushButton_deleteteam = QtWidgets.QPushButton(self.tab_teampage)
        self.pushButton_deleteteam.setObjectName("pushButton_deleteteam")
        self.gridLayout_2.addWidget(self.pushButton_deleteteam, 4, 2, 1, 1)
        self.pushButton_addteam = QtWidgets.QPushButton(self.tab_teampage)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../Pictures/icones/team_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_addteam.setIcon(icon)
        self.pushButton_addteam.setObjectName("pushButton_addteam")
        self.gridLayout_2.addWidget(self.pushButton_addteam, 4, 1, 1, 1)
        self.listWidget_playerslist = QtWidgets.QListWidget(self.tab_teampage)
        self.listWidget_playerslist.setObjectName("listWidget_playerslist")
        self.gridLayout_2.addWidget(self.listWidget_playerslist, 5, 3, 1, 2)
        self.pushButton_addplayer = QtWidgets.QPushButton(self.tab_teampage)
        self.pushButton_addplayer.setEnabled(False)
        self.pushButton_addplayer.setObjectName("pushButton_addplayer")
        self.gridLayout_2.addWidget(self.pushButton_addplayer, 6, 3, 1, 1)
        self.pushButton_deleteplayer = QtWidgets.QPushButton(self.tab_teampage)
        self.pushButton_deleteplayer.setEnabled(False)
        self.pushButton_deleteplayer.setObjectName("pushButton_deleteplayer")
        self.gridLayout_2.addWidget(self.pushButton_deleteplayer, 6, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_teampage)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 3, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.tab_teampage)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 2)
        self.tabWidget.addTab(self.tab_teampage, "")
        self.tab_competitionpage = QtWidgets.QWidget()
        self.tab_competitionpage.setMinimumSize(QtCore.QSize(200, 200))
        self.tab_competitionpage.setObjectName("tab_competitionpage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_competitionpage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab_competitionpage)
        self.groupBox.setMinimumSize(QtCore.QSize(325, 50))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.progressBar_competitionlevel = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar_competitionlevel.setMinimumSize(QtCore.QSize(31, 21))
        self.progressBar_competitionlevel.setProperty("value", 0)
        self.progressBar_competitionlevel.setObjectName("progressBar_competitionlevel")
        self.gridLayout_4.addWidget(self.progressBar_competitionlevel, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 7, 0, 1, 1)
        self.tableWidget_competitionresult = QtWidgets.QTableWidget(self.tab_competitionpage)
        self.tableWidget_competitionresult.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget_competitionresult.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget_competitionresult.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_competitionresult.setAutoFillBackground(True)
        self.tableWidget_competitionresult.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_competitionresult.setAlternatingRowColors(True)
        self.tableWidget_competitionresult.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_competitionresult.setRowCount(0)
        self.tableWidget_competitionresult.setColumnCount(0)
        self.tableWidget_competitionresult.setObjectName("tableWidget_competitionresult")
        self.gridLayout_3.addWidget(self.tableWidget_competitionresult, 5, 0, 1, 1)
        self.listWidget_matchslist = QtWidgets.QListWidget(self.tab_competitionpage)
        self.listWidget_matchslist.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget_matchslist.setMaximumSize(QtCore.QSize(256, 16777215))
        self.listWidget_matchslist.setItemAlignment(QtCore.Qt.AlignHCenter)
        self.listWidget_matchslist.setObjectName("listWidget_matchslist")
        self.gridLayout_3.addWidget(self.listWidget_matchslist, 6, 0, 1, 1)
        self.tabWidget.addTab(self.tab_competitionpage, "")
        self.tab_currentmatch = QtWidgets.QWidget()
        self.tab_currentmatch.setObjectName("tab_currentmatch")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_currentmatch)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.textEdit_domscore = QtWidgets.QTextEdit(self.tab_currentmatch)
        self.textEdit_domscore.setMinimumSize(QtCore.QSize(35, 25))
        self.textEdit_domscore.setMaximumSize(QtCore.QSize(35, 25))
        self.textEdit_domscore.setAutoFormatting(QtWidgets.QTextEdit.AutoBulletList)
        self.textEdit_domscore.setReadOnly(True)
        self.textEdit_domscore.setObjectName("textEdit_domscore")
        self.gridLayout_6.addWidget(self.textEdit_domscore, 0, 1, 1, 1)
        self.listWidget_extplayer = QtWidgets.QListWidget(self.tab_currentmatch)
        self.listWidget_extplayer.setObjectName("listWidget_extplayer")
        self.gridLayout_6.addWidget(self.listWidget_extplayer, 4, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_currentmatch)
        self.label.setEnabled(False)
        self.label.setMinimumSize(QtCore.QSize(200, 23))
        self.label.setMaximumSize(QtCore.QSize(200, 23))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 2, 1, 1)
        self.listWidget_domplayer = QtWidgets.QListWidget(self.tab_currentmatch)
        self.listWidget_domplayer.setObjectName("listWidget_domplayer")
        self.gridLayout_6.addWidget(self.listWidget_domplayer, 4, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_currentmatch)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_cm_goal = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_cm_goal.setObjectName("pushButton_cm_goal")
        self.gridLayout_5.addWidget(self.pushButton_cm_goal, 0, 0, 1, 1)
        self.pushButton_cm_endmatch = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_cm_endmatch.setObjectName("pushButton_cm_endmatch")
        self.gridLayout_5.addWidget(self.pushButton_cm_endmatch, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_2, 1, 0, 1, 5)
        self.textEdit_dom = QtWidgets.QTextEdit(self.tab_currentmatch)
        self.textEdit_dom.setEnabled(False)
        self.textEdit_dom.setMinimumSize(QtCore.QSize(90, 25))
        self.textEdit_dom.setMaximumSize(QtCore.QSize(16777215, 25))
        self.textEdit_dom.setAcceptRichText(False)
        self.textEdit_dom.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit_dom.setObjectName("textEdit_dom")
        self.gridLayout_6.addWidget(self.textEdit_dom, 0, 0, 1, 1)
        self.textEdit_extscore = QtWidgets.QTextEdit(self.tab_currentmatch)
        self.textEdit_extscore.setMinimumSize(QtCore.QSize(35, 25))
        self.textEdit_extscore.setMaximumSize(QtCore.QSize(35, 25))
        self.textEdit_extscore.setReadOnly(True)
        self.textEdit_extscore.setObjectName("textEdit_extscore")
        self.gridLayout_6.addWidget(self.textEdit_extscore, 0, 3, 1, 1)
        self.textEdit_vis = QtWidgets.QTextEdit(self.tab_currentmatch)
        self.textEdit_vis.setEnabled(False)
        self.textEdit_vis.setMinimumSize(QtCore.QSize(90, 25))
        self.textEdit_vis.setMaximumSize(QtCore.QSize(16777215, 25))
        self.textEdit_vis.setLineWrapColumnOrWidth(0)
        self.textEdit_vis.setAcceptRichText(False)
        self.textEdit_vis.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit_vis.setPlaceholderText("")
        self.textEdit_vis.setObjectName("textEdit_vis")
        self.gridLayout_6.addWidget(self.textEdit_vis, 0, 4, 1, 1)
        self.listWidget_matchevent = QtWidgets.QListWidget(self.tab_currentmatch)
        self.listWidget_matchevent.setObjectName("listWidget_matchevent")
        self.gridLayout_6.addWidget(self.listWidget_matchevent, 4, 1, 1, 3)
        self.tabWidget.addTab(self.tab_currentmatch, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 573, 21))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuOpen = QtWidgets.QMenu(self.menuFichier)
        self.menuOpen.setObjectName("menuOpen")
        self.menuNew = QtWidgets.QMenu(self.menuFichier)
        self.menuNew.setObjectName("menuNew")
        self.menuEdition = QtWidgets.QMenu(self.menubar)
        self.menuEdition.setObjectName("menuEdition")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionStandard_Competition = QtWidgets.QAction(MainWindow)
        self.actionStandard_Competition.setObjectName("actionStandard_Competition")
        self.menuNew.addAction(self.actionStandard_Competition)
        self.menuFichier.addAction(self.menuNew.menuAction())
        self.menuFichier.addAction(self.menuOpen.menuAction())
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuit)
        self.menuEdition.addAction(self.actionStart)
        self.menuEdition.addSeparator()
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuEdition.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.actionQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_deleteteam.setText(_translate("MainWindow", "Delete team"))
        self.pushButton_addteam.setText(_translate("MainWindow", "Add team"))
        self.pushButton_addplayer.setText(_translate("MainWindow", "Add player"))
        self.pushButton_deleteplayer.setText(_translate("MainWindow", "Delete player"))
        self.label_2.setText(_translate("MainWindow", "<h2><strong>Players list</strong></h2>"))
        self.label_3.setText(_translate("MainWindow", "<h1><strong>Teams list</strong></h1>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_teampage), _translate("MainWindow", "Teams List"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_competitionpage), _translate("MainWindow", "ChampionShip"))
        self.textEdit_domscore.setPlaceholderText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "VS"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Game events"))
        self.pushButton_cm_goal.setText(_translate("MainWindow", "Goal"))
        self.pushButton_cm_endmatch.setText(_translate("MainWindow", "End of the match"))
        self.textEdit_extscore.setPlaceholderText(_translate("MainWindow", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_currentmatch), _translate("MainWindow", "Current match"))
        self.menuFichier.setTitle(_translate("MainWindow", "File"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.menuEdition.setTitle(_translate("MainWindow", "Editor"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionStart.setText(_translate("MainWindow", "Start Competition"))
        self.actionStandard_Competition.setText(_translate("MainWindow", "Standard Competition"))
