# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Authorisation.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(482, 260)
        MainWindow.setWinowIcon(QtGui.QIcon('safe.png'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.LogInBtn = QtWidgets.QPushButton(self.centralwidget)
        self.LogInBtn.setGeometry(QtCore.QRect(130, 160, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LogInBtn.setFont(font)
        self.LogInBtn.setObjectName("LogInBtn")
        self.LoginFld = QtWidgets.QLineEdit(self.centralwidget)
        self.LoginFld.setGeometry(QtCore.QRect(100, 30, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LoginFld.setFont(font)
        self.LoginFld.setText("")
        self.LoginFld.setObjectName("LoginFld")
        self.passwFld = QtWidgets.QLineEdit(self.centralwidget)
        self.passwFld.setGeometry(QtCore.QRect(100, 90, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.passwFld.setFont(font)
        self.passwFld.setObjectName("passwFld")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 482, 21))
        self.menubar.setObjectName("menubar")

        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.Authorisation = QtWidgets.QAction(MainWindow)
        self.Authorisation.setObjectName("Authorisation")

        self.NewAccount = QtWidgets.QAction(MainWindow)
        self.NewAccount.setObjectName("NewAccount")
        self.menu.addAction(self.Authorisation)
        self.menu.addAction(self.NewAccount)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LogInBtn.setText(_translate("MainWindow", "Log In"))
        self.LoginFld.setPlaceholderText(_translate("MainWindow", "Login"))
        self.passwFld.setPlaceholderText(_translate("MainWindow", "Password"))
        self.menu.setTitle(_translate("MainWindow", "Выберите действие"))
        self.Authorisation.setText(_translate("MainWindow", "Авторизация"))
        self.NewAccount.setText(_translate("MainWindow", "Новый Аккаунт"))

