# author Cherniakof Vlad
# safe for passwords


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic


class Authorisation(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Authorisation.ui' ,self)
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
                self.switc_to_Main()

    def switch(self):
        window.close()
        self.new_window = NewAccount()
        self.new_window.show()

    def switch_to_Main(self):
        self.close()
        self.new_window = MainPage()
        self.new_window.show()


class NewAccount(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('NewAccount.ui', self)
        self.SignUpBtn.clicked.connect(self.SignUp)
        self.Authorisation.triggered.connect(self.switch)

    def SignUp(self):
        file = open('Account.txt', 'w')
        login = self.LoginFld.text()
        password = self.passwFld.text()
        file.write(login + password)
        self.switch()

    def switch(self):
        self.close()
        self.new_window = Authorisation()
        self.new_window.show()


class MainPage(QMainWindow):
    pass


app = QApplication(sys.argv)
window = Authorisation()
window.show()
sys.exit(app.exec_())