from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from set_operations_ui import Ui_MainWindow

import json

class SetQuestions:
    def __init__(self, ques_num, question, option1, option2, option3, option4, answer):
        self.ques_num = ques_num
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.answer = answer


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Set Operation")
        self.connectSignalsSlots()
        self.counter = 0
        self.set_questions = add_set_questions('../resources/set_questions.json')

    def connectSignalsSlots(self):
        self.next_button.clicked.connect(self.next_pressed)
        self.submit_button.clicked.connect(self.submit_pressed)


    def next_pressed(self):
        i = self.counter % len(self.set_laws)
        self.update_ui(self.set_laws[i].law_name, self.set_laws[i].question, self.set_laws[i].answer, self.set_laws[i].img)
        self.counter += 1


    def update_ui(self, quesNum, question, option1, option2, option3, option4):
        _translate = QCoreApplication.translate

        self.question_label.setText(_translate("MainWindow", question))
        self.option1_button.setText(_translate("MainWindow", option1))
        self.option2_button.setText(_translate("MainWindow", option2))
        self.option3_button.setText(_translate("MainWindow", option3))
        self.option4_button.setText(_translate("MainWindow", option4))


def add_set_questions(file):
    set_questions = []
    with open(file, 'r') as f:
        data = json.load(f)

        for ques in data["set_questions"]:
            set_question = SetQuestions(ques["ques_num"], ques["question"], ques["option1"], ques["option2"], ques["option3"], ques["option4"], ques["answer"])
            set_questions.append(set_question)

    return set_questions


def get_selected_option():
    pass

