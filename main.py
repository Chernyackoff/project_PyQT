# author Cherniakof Vlad
# safe for passwords


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic


class Authorisation(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Authorisation.ui', self)
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
            line = file.readline()
            max = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
            count = 0
            if login + password != line or line == '':
                self.ErrorText.setText('Ошибка. Создайте аккаунт')
                count += 1
            else:
                self.switch_to_main()
            if max == count:
                pass

    def switch(self):
        window.close()
        self.new_window = NewAccount()
        self.new_window.show()

    def switch_to_main(self):
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
        login = self.LoginFld.text()
        password = self.passwFld.text()
        try:
            file2 = open('Account.txt', 'r')
            if login + password == file2.readline():
                self.ErrorText.setText('Ошибка. Аккаунт уже существует')
                file2.close()
            else:
                file = open('Account.txt', 'w')
                file.write(login + password)
                file.close()
                self.switch()
        except FileNotFoundError:
            pass

    def switch(self):
        self.close()
        self.new_window = Authorisation()
        self.new_window.show()


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainPage.ui', self)


app = QApplication(sys.argv)
window = Authorisation()
window.show()
sys.exit(app.exec_())