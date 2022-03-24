from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from set_operations_ui import Ui_MainWindow

import json
import sys


class SetQuestions:
    def __init__(self, ques_num, question, option1, option2, option3, option4, answer):
        self.ques_num = ques_num
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.answer = answer


def add_set_questions(file):
    set_questions = []
    with open(file, 'r') as f:
        data = json.load(f)

        for ques in data["set_questions"]:
            set_question = SetQuestions(ques["ques_num"], ques["question"], ques["option1"], ques["option2"],
                                        ques["option3"], ques["option4"], ques["answer"])
            set_questions.append(set_question)

    return set_questions


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Set Operation")
        self.setFixedWidth(1500)
        self.setFixedHeight(800)

        self.connectSignalsSlots()

        self.set_questions = add_set_questions('../resources/set_questions.json')
        self.option_buttons = [self.option1_button, self.option2_button, self.option3_button, self.option4_button]

        # To Get 1st Question
        self.counter = -1
        self.next_pressed()

    def connectSignalsSlots(self):
        self.next_button.clicked.connect(self.next_pressed)
        self.submit_button.clicked.connect(self.submit_pressed)

    def next_pressed(self):
        i = self.counter
        self.update_ui(self.set_questions[i].question, self.set_questions[i].option1, self.set_questions[i].option2,
                       self.set_questions[i].option3, self.set_questions[i].option4)
        self.counter += 1
        self.counter %= len(self.set_questions)

    def submit_pressed(self):
        selected_option = self.get_selected_option()
        if selected_option is not None:
            self.show_answer()
            for button in self.option_buttons:
                button.setEnabled(False)

    def update_ui(self, question, option1, option2, option3, option4):
        _translate = QCoreApplication.translate

        self.reset_option_button_states()
        self.question.setText(_translate("MainWindow", "    " + question))
        self.option1_button.setText(_translate("MainWindow", option1))
        self.option2_button.setText(_translate("MainWindow", option2))
        self.option3_button.setText(_translate("MainWindow", option3))
        self.option4_button.setText(_translate("MainWindow", option4))

    def reset_option_button_states(self):
        for button in self.option_buttons:
            button.setAutoExclusive(False)
            button.setChecked(False)
            button.setAutoExclusive(True)
            button.setStyleSheet("background-color: white;")
            button.setEnabled(True)

    def get_selected_option(self):
        for i in range(4):
            if self.option_buttons[i].isChecked():
                return i + 1

    def is_answer_correct(self):
        selected_option = self.get_selected_option()
        answer = self.set_questions[self.counter].answer
        if selected_option == answer:
            return True
        else:
            return False

    def show_answer(self):
        selected_option = self.get_selected_option()
        answer = self.set_questions[self.counter].answer
        self.option_buttons[answer - 1].setStyleSheet("background-color: rgb(72, 169, 108);")
        if not self.is_answer_correct():
            self.option_buttons[selected_option - 1].setStyleSheet("background-color: rgb(169, 72, 72);")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
