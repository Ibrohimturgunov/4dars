import sys
import json
import os
from PyQt5.QtWidgets import *

 # ============================================================
def show_test_button(self):
        # Test boshlash tugmasini yaratish va maketga qo'shish
    self.start_test_button = QPushButton("Testni boshlash", self)
    self.start_test_button.clicked.connect(self.start_test)
    self.layout().addWidget(self.start_test_button)

def start_test(self):
    # Test oynasini ochish va hozirgi oynani yopish
    self.test_window = TestWindow()
    self.test_window.show()
    self.close()


class TestWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Test oynasining nomi va hajmini o'rnatadi
        self.setWindowTitle("Python Testi")
        self.resize(450, 350)

        # Savollarni fayldan yuklash va boshlang'ich qiymatlarni o'rnatish
        self.questions = self.load_questions_from_file("python_test.txt")
        self.current_question = 0
        self.score = 0

        # Savollarni ko'rsatish uchun maket yaratish va o'rnatish
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.show_question()

    def load_questions_from_file(self, filename):
        # Fayldan savollarni yuklaydi va formatlaydi
        questions = []
        try:
            with open(filename, "r") as file:
                content = file.read().split("---")  # Har bir savolni ajratish
                for question_block in content:
                    lines = question_block.strip().split("\n")
                    if len(lines) >= 2:
                        savol = lines[0]
                        variantlar = lines[1:]
                        questions.append({"savol": savol, "variantlar": variantlar})
        except FileNotFoundError:
            # Fayl topilmasa, ogohlantirish xabari
            QMessageBox.warning(self, "Xato", f"{filename} fayli topilmadi.")
        return questions

    def show_question(self):
        # Hozirgi savolni ko'rsatish uchun funksiya
        question_data = self.questions[self.current_question]

        # Savol yozuvini yaratish va maketga qo'shish
        self.question_label = QLabel(question_data["savol"], self)
        self.layout.addWidget(self.question_label)

        # Variantlar uchun tugmalar guruhi yaratish
        self.button_group = QButtonGroup(self)
        self.option_buttons = []
        for i, option in enumerate(question_data["variantlar"]):
            option_button = QRadioButton(option, self)
            self.button_group.addButton(option_button)
            self.option_buttons.append(option_button)
            self.layout.addWidget(option_button)

        # Keyingi tugmasini yaratish va maketga qo'shish
        self.next_button = QPushButton("Keyingi", self)
        self.next_button.clicked.connect(self.next_question)
        self.layout.addWidget(self.next_button)

    def next_question(self):
        # Foydalanuvchi tanlagan variantni tekshirish
        selected_button = self.button_group.checkedButton()
        if selected_button:
            answer_text = selected_button.text()
            # To'g'ri javob bilan solishtirish
            correct_answers = ["C) Har xil dasturlarni yaratish", "B) .py", "B) [ ]", "A) print()", "B) #"]
            if answer_text == correct_answers[self.current_question]:
                self.score += 1

        # Keyingi savolga o'tish yoki yakunlash
        self.clear_layout()
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self): 
        # Yakuniy natijani ko'rsatish
        QMessageBox.information(self, "Test Yakuni", f"Sizning natijangiz: {self.score}/{len(self.questions)}")
        self.close()

    def clear_layout(self):
        # Maketni tozalash, eski elementlarni o'chirish
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()


if __name__=="__main__":
    app=QApplication([])
    win=TestWindow()
    win.show()
    sys.exit(app.exec_())