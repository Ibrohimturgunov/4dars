import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


def parol_tekshir(parol):
    kichik = katta = son = belgi = False
    if len(parol) < 7:
        return "Parol uzunligi 7 belgidan kam bo'lishi kerak."

    for i in parol:
        if i.islower():
            kichik = True
        elif i.isupper():
            katta = True
        elif i.isdigit():
            son = True
        elif i in "!@#$%^&*()_+-=[]{}|;:'\",.<>?/":
            belgi = True

    if not (kichik and katta and son and belgi):
        return "Parol kamida 4 xil turli xildagi belgilarni o'z ichiga olishi kerak.\nNamuna: A1!b"

    return "Parol muvaffaqiyatli tasdiqlandi!"


class PasswordChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Parolni Tekshirish")
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()
        self.label = QLabel("Parolni kiriting:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.result_label = QLabel("")
        self.check_button = QPushButton("Tekshirish")
        self.check_button.clicked.connect(self.on_check_password)
        layout.addWidget(self.label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.check_button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

    def on_check_password(self):
        parol = self.password_input.text()
        result = parol_tekshir(parol)
        self.result_label.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordChecker()
    window.show()
    sys.exit(app.exec_())
