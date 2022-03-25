from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Code.Main_Screen.MainScreen_ui import Ui_MainWindow
import sys


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Home Page")
        self.setFixedWidth(1500)
        self.setFixedHeight(800)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.practiceButton.clicked.connect(self.redirect_practice)
        self.createButton.clicked.connect(self.redirect_create)

    def redirect_practice(self):
        from Code.Practice_homepage.selectPracticeQn import MainWindow as Practice_main
        self.window1 = Practice_main()
        self.window1.show()
        self.hide()

    def redirect_create(self):
        from Code.Create_Exercises.src.CreateExercises import MainWindow as Create
        self.window2 = Create()
        self.window2.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())