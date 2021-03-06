# author Cherniakof Vlad
# safe for passwords


import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5 import uic
from cryptography.fernet import Fernet


class Authorization(QMainWindow):  # Creates new Authorization window
    def __init__(self):
        super().__init__()
        uic.loadUi('UIs/Authorisation.ui', self)
        self.LogInBtn.clicked.connect(self.LogIn)  # Reads click
        self.NewAccount.triggered.connect(self.switch)  # Reads menu bar
        self.count = 0

    def LogIn(self):  # Process of log in
        max_mistakes = -1
        try:
            file = open('.max_mistakes.txt', 'r')
            max_mistakes = int(file.readline())
        except FileNotFoundError:
            pass
        try:
            file = open('.Account.txt', 'r')  # Opens file with login + password
        except FileNotFoundError:
            self.ErrorText.setText('Ошибка. Создайте аккаунт')  # Returns Error
        else:
            login = self.LoginFld.text()  # Reads Login
            password = self.passwFld.text()  # Reads password
            try:
                if login != '' and password != '':  # If not filled raises Error
                    pass
                else:
                    raise ValueError
            except ValueError:
                self.ErrorText.setText('Введите логин И (!!!) Пароль')
            else:
                line = file.readline()
                if login + password != line or line == '':
                    self.ErrorText.setText('Ошибка. Введите верные данные')
                    self.count += 1
                else:
                    self.switch_to_main()
        if max_mistakes == self.count:  # Security needs
            self.ErrorText.setText('Вы  превысили лимит: ключи стерты')
            try:
                os.remove('.token.txt')
            except FileNotFoundError:
                pass
            try:
                os.remove('.key.txt')
            except FileNotFoundError:
                pass
            try:
                os.remove('.max_mistakes.txt')
            except FileNotFoundError:
                pass
            try:
                os.remove('.webprog.txt')
            except FileNotFoundError:
                pass

    def switch(self):  # Switches to the new window
        window.close()
        self.new_window = NewAccount()
        self.new_window.show()

    def switch_to_main(self):
        self.close()
        self.new_window = MainPage()
        self.new_window.show()


class NewAccount(QMainWindow):  # Window of creating of a new account
    def __init__(self):
        super().__init__()
        uic.loadUi('UIs/NewAccount.ui', self)
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
            file2 = open('.Account.txt', 'r')
            if login + password == file2.readline():
                self.ErrorText.setText('Ошибка. Аккаунт уже существует')
                file2.close()
            else:
                self.dialog = Dialog()
                self.dialog.show()
        except FileNotFoundError:
            file = open('.Account.txt', 'w')
            file.write(login + password)
            file.close()
            self.switch()

    def switch(self):
        self.close()
        self.new_window = Authorization()
        self.new_window.show()


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('UIs/Dialog.ui', self)
        self.cancel.clicked.connect(self.close)
        self.okey.clicked.connect(self.deletion)

    def deletion(self):
        try:
            os.remove('.Account.txt')
        except FileNotFoundError:
            pass
        try:
            os.remove('.token.txt')
        except FileNotFoundError:
            pass
        try:
            os.remove('.key.txt')
        except FileNotFoundError:
            pass
        try:
            os.remove('.max_mistakes.txt')
        except FileNotFoundError:
            pass
        try:
            os.remove('.webprog.txt')
        except FileNotFoundError:
            pass
        self.close()


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UIs/MainPage.ui', self)
        self.AddPasswd.clicked.connect(self.add_password)
        self.Safe.clicked.connect(self.safe_switch)
        self.Settings.clicked.connect(self.settings)
        self.exit.clicked.connect(self.close)
        self.delete_account.clicked.connect(self.deletion)

    def add_password(self):
        self.dialog = AddPassword()
        self.dialog.show()

    def safe_switch(self):
        self.close()
        self.new_window = Safe()
        self.new_window.show()

    def settings(self):
        self.close()
        self.new_window = Settings()
        self.new_window.show()

    def deletion(self):
        self.dialog = Deletion()
        self.dialog.show()


class Deletion(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('UIs/Deletion.ui', self)
        self.cancel.clicked.connect(self.close)
        self.Okey.clicked.connect(self.deletion_ac)

    def deletion_ac(self):
        try:
            os.remove('.Account.txt')
        except FileNotFoundError:
            pass
        try:
            os.remove('.token.txt')
        except FileNotFoundError:
            pass
        try:
            os.remove('.key.txt')
        except FileNotFoundError:
            pass
        try:
            os.remove('.max_mistakes.txt')
        except FileNotFoundError:
            pass
        try:
            os.remove('.webprog.txt')
        except FileNotFoundError:
            pass
        self.close()


class AddPassword(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('UIs/AddPassword.ui', self)
        self.cancel.clicked.connect(self.close)
        self.okey.clicked.connect(self.addnew)

    def addnew(self):
        try:
            file_prog = open('.webprog.txt', 'a')
            file_keys = open('.key.txt', 'a')
            file_token = open(".token.txt", 'a')
        except FileNotFoundError:
            file_prog = open('.webprog.txt', 'w')
            file_keys = open('.key.txt', 'w')
            file_token = open(".token.txt", 'w')
        login = self.Login.text()
        password = self.Password.text()
        webprog = self.siteprog.text()
        file_prog.write(webprog + '\n')
        key = Fernet.generate_key()
        file_keys.write(key.decode() + '\n')
        fernet = Fernet(key)
        line = login + ' ' + password
        token = fernet.encrypt(line.encode('UTF-8'))
        file_token.write(token.decode() + '\n')
        self.close()


class Safe(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UIs/Safe.ui', self)
        self.exit.clicked.connect(self.switch)
        self.showp.clicked.connect(self.showtime)

    def showtime(self):
        line = ''
        keys = []
        webs = []
        tokens = []
        try:
            file_keys = open('.key.txt', 'r')
            file_token = open('.token.txt', 'r')
            file_prog = open('.webprog.txt', 'r')
            for key in file_keys.readlines():
                keys.append(key)
            for web in file_prog.readlines():
                webs.append(web)
            for token in file_token.readlines():
                tokens.append(token)
            for i in range(len(webs)):
                webp = webs[i]
                webp = webp[:-1]
                key = keys[i]
                key = key[:-1]
                fernet = Fernet(key.encode())
                token = tokens[i]
                token = token[:-1]
                loginpassword = fernet.decrypt(token.encode()).decode('UTF-8').split()
                login = loginpassword[0]
                password = loginpassword[1]
                rline = webp + ': ' + '\t' + 'login: ' + login + '\t' + 'password: ' + password + '\n'
                line += rline
            self.text.setText(line)
        except FileNotFoundError:
            self.text.setText('Вы не добавили еще ни одного аккаунта и пароля в сейф')

    def switch(self):
        self.close()
        self.new_window = MainPage()
        self.new_window.show()


class Settings(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UIs/Settings.ui', self)
        self.cancel.clicked.connect(self.switch)
        self.exit.clicked.connect(self.switch)
        self.save.clicked.connect(self.max_mistakes)

    def max_mistakes(self):
        try:
            mistakes = self.max_num.text()
            file = open('.max_mistakes.txt', 'w')
            file.write(mistakes)
        except ValueError:
            self.ErrorText.setText('Введите корректное число!!!')

    def switch(self):
        self.close()
        self.new_window = MainPage()
        self.new_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Authorization()
    window.show()
    sys.exit(app.exec_())
