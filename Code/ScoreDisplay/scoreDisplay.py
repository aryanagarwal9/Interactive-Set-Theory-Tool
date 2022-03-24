import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Code.ScoreDisplay.scoreDisplay_ui import Ui_MainWindow

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, score, total_questions):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setFixedWidth(1500)
        self.setFixedHeight(800)
        self.setWindowTitle("Score")
        self.connectSignalsSlots()
        self.score = score
        self.total_questions = total_questions
        self.display_score()

    def connectSignalsSlots(self):
        self.mainMenu_Button.clicked.connect(self.mainMenu_pressed)

    def mainMenu_pressed(self):
        import Code.Main_Screen.MainScreen as Main
        self.window = Main.MainWindow()
        self.window.show()
        self.hide()

    def display_score(self):
        _translate = QCoreApplication.translate
        self.resultLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">" + "Your Score: " + str(self.score) + " / " + str(self.total_questions) + "</p></body></html>"))
