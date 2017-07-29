# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'germaniumsb/MainWindow.ui'
#
# Created: Sat Jul 29 23:19:50 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.browserLabel = QtGui.QLabel(self.centralwidget)
        self.browserLabel.setObjectName("browserLabel")
        self.horizontalLayout.addWidget(self.browserLabel)
        self.browserCombo = QtGui.QComboBox(self.centralwidget)
        self.browserCombo.setObjectName("browserCombo")
        self.horizontalLayout.addWidget(self.browserCombo)
        self.startBrowserButton = QtGui.QPushButton(self.centralwidget)
        self.startBrowserButton.setObjectName("startBrowserButton")
        self.horizontalLayout.addWidget(self.startBrowserButton)
        self.stopBrowserButton = QtGui.QPushButton(self.centralwidget)
        self.stopBrowserButton.setObjectName("stopBrowserButton")
        self.horizontalLayout.addWidget(self.stopBrowserButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.liveButton = QtGui.QPushButton(self.centralwidget)
        self.liveButton.setCheckable(True)
        self.liveButton.setChecked(True)
        self.liveButton.setObjectName("liveButton")
        self.horizontalLayout.addWidget(self.liveButton)
        self.highlightElementButton = QtGui.QPushButton(self.centralwidget)
        self.highlightElementButton.setObjectName("highlightElementButton")
        self.horizontalLayout.addWidget(self.highlightElementButton)
        self.pickElementButton = QtGui.QPushButton(self.centralwidget)
        self.pickElementButton.setObjectName("pickElementButton")
        self.horizontalLayout.addWidget(self.pickElementButton)
        self.cancelPickButton = QtGui.QPushButton(self.centralwidget)
        self.cancelPickButton.setObjectName("cancelPickButton")
        self.horizontalLayout.addWidget(self.cancelPickButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.codeEdit = QtGui.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.codeEdit.setFont(font)
        self.codeEdit.setPlainText("")
        self.codeEdit.setObjectName("codeEdit")
        self.gridLayout.addWidget(self.codeEdit, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuExecute = QtGui.QMenu(self.menubar)
        self.menuExecute.setObjectName("menuExecute")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.actionHighlight = QtGui.QAction(MainWindow)
        self.actionHighlight.setObjectName("actionHighlight")
        self.actionPick = QtGui.QAction(MainWindow)
        self.actionPick.setObjectName("actionPick")
        self.actionAbout_QT = QtGui.QAction(MainWindow)
        self.actionAbout_QT.setObjectName("actionAbout_QT")
        self.menuHelp.addAction(self.action_About)
        self.menuHelp.addAction(self.actionAbout_QT)
        self.menuExecute.addAction(self.actionHighlight)
        self.menuExecute.addAction(self.actionPick)
        self.menubar.addAction(self.menuExecute.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Germanium Selector Builder v2.0.5", None, QtGui.QApplication.UnicodeUTF8))
        self.browserLabel.setText(QtGui.QApplication.translate("MainWindow", "Browser:", None, QtGui.QApplication.UnicodeUTF8))
        self.startBrowserButton.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.stopBrowserButton.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.liveButton.setText(QtGui.QApplication.translate("MainWindow", "Live", None, QtGui.QApplication.UnicodeUTF8))
        self.highlightElementButton.setText(QtGui.QApplication.translate("MainWindow", "Highlight", None, QtGui.QApplication.UnicodeUTF8))
        self.pickElementButton.setText(QtGui.QApplication.translate("MainWindow", "Pick", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelPickButton.setText(QtGui.QApplication.translate("MainWindow", "Cancel Pick", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExecute.setTitle(QtGui.QApplication.translate("MainWindow", "Execute", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHighlight.setText(QtGui.QApplication.translate("MainWindow", "Highlight", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPick.setText(QtGui.QApplication.translate("MainWindow", "Pick", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_QT.setText(QtGui.QApplication.translate("MainWindow", "About QT", None, QtGui.QApplication.UnicodeUTF8))

