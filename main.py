# author Cherniakof Vlad
# safe for passwords


import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5 import uic

max = 100000000000000000000000000000000000000000000000000


class Authorisation(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Authorisation.ui', self)
        self.LogInBtn.clicked.connect(self.LogIn)
        self.NewAccount.triggered.connect(self.switch)
        #self.max = 100000000000000000000000000000000000000000000000000000000000000000000000

    def LogIn(self):
        count = 0
        try:
            file = open('Account.txt', 'r')
        except FileNotFoundError:
            self.ErrorText.setText('Ошибка. Создайте аккаунт')
        else:
            login = self.LoginFld.text()
            password = self.passwFld.text()
            try:
                if login != '' and password != '':
                    pass
                else:
                    raise ValueError
            except ValueError:
                self.ErrorText.setText('Введите логин И (!!!) Пароль')
            else:
                line = file.readline()
                if login + password != line or line == '':
                    self.ErrorText.setText('Ошибка. Создайте аккаунт')
                    count += 1
                else:
                    self.switch_to_main()
        if max == count:
            try:
                os.remove('Safe.txt')
            except FileNotFoundError:
                self.ErrorText.setText('Вы  превысили лимит: пароли стерты')
                try:
                    os.remove('Passwords.txt')
                except FileNotFoundError:
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
            if login != '' and password != '':
                pass
            else:
                raise ValueError
        except ValueError:
            self.ErrorText.setText('Введите логин И (!!!) Пароль')
        try:
            file2 = open('Account.txt', 'r')
            if login + password == file2.readline():
                self.ErrorText.setText('Ошибка. Аккаунт уже существует')
                file2.close()
            else:
                self.dialog = Dialog()
                self.dialog.show()
        except FileNotFoundError:
            file = open('Account.txt', 'w')
            file.write(login + password)
            file.close()
            self.switch()

    def switch(self):
        self.close()
        self.new_window = Authorisation()
        self.new_window.show()


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('Dialog.ui', self)
        self.cancel.clicked.connect(self.close)
        self.okey.clicked.connect(self.deletion)

    def deletion(self):
        os.remove('Account.txt')
        try:
            os.remove('Passwords.txt')
        except FileNotFoundError:
            pass


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainPage.ui', self)



app = QApplication(sys.argv)
window = Authorisation()
window.show()
sys.exit(app.exec_())