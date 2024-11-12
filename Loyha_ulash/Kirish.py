from Registratsiya import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json
import os
from test import TestWindow


class Windowe(QWidget):
    def __init__(self, parent=None):
        super(Windowe, self).__init__(parent)
        self.setWindowTitle("Login System")
        self.resize(450, 500)

        self.setStyleSheet("background-color: green;")

        self.label_login = QLabel("Login:       ")
        self.label_login.setStyleSheet("color: red;")
        self.label_login.setFont(QFont("Arial", 15))
        self.line_login = QLineEdit()
        self.line_login.setStyleSheet("border: 2px solid red;")

        font = QFont("Arial", 12)
        self.line_login.setFont(font)

        self.label_password = QLabel("Password:")
        self.label_password.setStyleSheet("color: red;")
        self.label_password.setFont(QFont("Arial", 15))
        self.line_password = QLineEdit()
        self.line_password.setStyleSheet("border: 2px solid red;")
        self.line_password.setEchoMode(QLineEdit.Password)
        font = QFont("Arial", 12)
        self.line_password.setFont(font)

        self.btn_signin = QPushButton("Sign In")  # kirish
        self.btn_signin.setFont(QFont("Arial", 12))
        self.btn_signin.setStyleSheet("background-color: red; color: blue")

        self.btn_signin.clicked.connect(self.sign_in)

        self.btn_signup = QPushButton("Sigin Up")  # royxatdan otish
        self.btn_signup.setStyleSheet("background-color: red; color: blue")
        self.btn_signup.setFont(QFont("Arial", 12))
        self.btn_signup.clicked.connect(self.sign_up)

        login_layout = QHBoxLayout()
        login_layout.addWidget(self.label_login)
        login_layout.addWidget(self.line_login)

        password_layout = QHBoxLayout()
        password_layout.addWidget(self.label_password)
        password_layout.addWidget(self.line_password)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_signin)
        button_layout.addWidget(self.btn_signup)

        main_layout = QVBoxLayout()
        main_layout.addLayout(login_layout)
        main_layout.addLayout(password_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def sign_in(self):

        with open("registration_data.json", "r") as file:
            data = json.load(file)
        lst = data["obyectlar"]
        lampa = 0

        for element in lst:
            print(element)
            if element["Name"] == self.line_login.text():
                if element["Password"] == self.line_password.text():
                    lampa = 1
        if lampa == 1:
            self.hide()
            self.widget = TestWindow()
            self.widget.show()
        else:
            self.line_login.setText("")
            self.line_password.setText("")
            self.line_login.setPlaceholderText("Bunday foydalanuvchi yo'q")
            self.line_password.setPlaceholderText("Bunday foydalanuvchi yo'q")

    def sign_up(self):
        self.hide()
        self.regstr = RegistrationWindow()
        self.regstr.show()



def main():
    app = QApplication(sys.argv)
    ex = Windowe()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()