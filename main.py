# author Cherniakof Vlad
# safe for passwords


import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5 import uic
from cryptography.fernet import Fernet


maimum_try = 10000000000000000000000000000000000000000000000000000000000000000000000000000000


class Authorisation(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Authorisation.ui', self)
        self.LogInBtn.clicked.connect(self.LogIn)
        self.NewAccount.triggered.connect(self.switch)

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
        if maimum_try == count:
            try:
                os.remove('keys.txt')
            except FileNotFoundError:
                self.ErrorText.setText('Вы  превысили лимит: ключи стерты')
                try:
                    os.remove('token.txt')
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
        self.AddPasswd.clicked.connect(self.add_password)
        self.Safe.clicked.connect(self.safe_switch)
        self.Settings.clicked.connect(self.settings)

    def add_password(self):
        self.dialog = AddPassword()
        self.dialog.show()

    def safe_switch(self):
        self.close()
        self.new_window = Safe()
        self.show()

    def settings(self):
        self.close()
        self.new_window = Settings()
        self.show()


class AddPassword(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('AddPassword.ui', self)
        self.cancel.clicked.connect(self.close)
        self.okey.clicked.connect(self.addnew)

    def addnew(self):
        login = self.Login.text()
        password = self.Password.text()
        webprog = self.siteprog.text()
        sys.stdout = open('webprog', 'w')
        print(webprog)
        key = Fernet.generate_key()
        sys.stdout = open('key.txt', 'w')
        print(key)
        fernet = Fernet(key)
        line = login + ' ' + password
        token = fernet.encrypt(line.encode('UTF-8'))
        sys.stdout = open("token.txt", 'w')
        print(token)



class Safe(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Safe.ui', self)


class Settings(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Settings.ui', self)


app = QApplication(sys.argv)
window = Authorisation()
window.show()
sys.exit(app.exec_())