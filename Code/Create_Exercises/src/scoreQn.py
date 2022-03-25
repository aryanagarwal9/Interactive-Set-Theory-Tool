from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Code.Create_Exercises.src.scoreQn_ui import Ui_MainWindow

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, score, answers):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Final Score")
        self.setFixedWidth(1500)
        self.setFixedHeight(800)
        self.connectSignalsSlots()
        self.displayAllScores(score, answers)
    
    def connectSignalsSlots(self):
        self.mainMenu_Button.clicked.connect(self.mainMenu_pressed)
        
    def displayAllScores(self, score, answers):
        _translate = QCoreApplication.translate
        
        self.resultLabel.setText(_translate("MainWindow","<html><head/><body><p align=\"center\"> Your Score: " + str(score) + "</p></body></html>"))
        self.q1.setText(_translate("MainWindow",'Q1: '+answers[0]))
        self.q2.setText(_translate("MainWindow",'Q2: '+answers[1]))
        self.q3.setText(_translate("MainWindow",'Q3: '+answers[2]))
    
    def mainMenu_pressed(self):
        import Code.Main_Screen.MainScreen as Main
        self.window = Main.MainWindow()
        self.window.show()
        self.hide()