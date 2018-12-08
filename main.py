# author Cherniakof Vlad
# safe for passwords


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Authorisation.ui',self)
        self.LogInBtn.clicked.connect(self.LogIn)

    def LogIn(self):
        try:
            file = open('Account.txt', 'r')
        except FileNotFoundError:
            self.ErrorText.setText('Ошибка. Создайте аккаунт')
        login = self.LoginFld.text()
        password = self.passwrdFld.text()
        if login + password != file.readline()

app = QApplication(sys.argv)
window = MyWidget()
window.show()
sys.exit(app.exec_())