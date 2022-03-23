from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MainScreen_ui import Ui_MainWindow
import sys
from Practice_homepage.selectPracticeQn import MainWindow as Practice_main


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Home Page")
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.practiceButton.clicked.connect(self.redirect_practice)
        # self.createButton.clicked.connect(self.redirect_create)

    def redirect_practice(self):
        self.w = Practice_main()
        self.w.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())