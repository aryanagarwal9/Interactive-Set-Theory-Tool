from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from practice_laws_ui import Ui_MainWindow

import sys
import json


class SetLaw:

    def __init__(self, law_name, question, answer, img):
        self.law_name = law_name
        self.question = question
        self.answer = answer
        self.img = img

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Set Laws")
        self.connectSignalsSlots()
        self.counter = 0
        self.set_laws = add_set_laws('practice_laws/resources/set_laws.json')


    def connectSignalsSlots(self):
        self.next_button.clicked.connect(self.next_pressed)

    def next_pressed(self):
        i = self.counter % len(self.set_laws)
        self.update_ui(self.set_laws[i].law_name, self.set_laws[i].question, self.set_laws[i].answer, self.set_laws[i].img)
        self.counter += 1


    def update_ui(self, law_name, question, answer, img):
        _translate = QCoreApplication.translate
        self.Question_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">According to " + law_name + " :</p><p align=\"center\"> " + question + " = ??? </p></body></html>"))
        self.Answer_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"> " + answer + "</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))


def add_set_laws(file):
    set_laws = []
    with open(file, 'r') as f:
        data = json.load(f)

        for law in data["set_laws"]:
            set_law = SetLaw(law["law_name"], law["question"], law["answer"], law["img"])
            set_laws.append(set_law)

    return set_laws


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
