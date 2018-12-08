# author Cherniakof Vlad
# safe for passwords


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic


class Authorisation(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Authorisation.ui',self)
        self.LogInBtn.clicked.connect(self.LogIn)
        self.NewAccount.triggered.connect(self.switch)

    def LogIn(self):
        try:
            file = open('Account.txt', 'r')
        except FileNotFoundError:
            self.ErrorText.setText('Ошибка. Создайте аккаунт')
        else:
            login = self.LoginFld.text()
            password = self.passwFld.text()
            if login + password != file.readline():
                self.ErrorText.setText('Ошибка. Создайте аккаунт')
            else:
                pass

    def switch(self):
        window.close()
        new_window = NewAccount()
        new_window.show()


class NewAccount(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Authorisation.ui',self)
        self.SignUpBtn.clicked.connect(self.LogIn)
        self.Authorisation.triggered.connect(self.switch)


app = QApplication(sys.argv)
window = Authorisation()
window.show()
sys.exit(app.exec_())