import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Practice_homepage.selectPracticeQn_ui import Ui_MainWindow

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Practice Modes")
        self.connectSignalSlots()

    def connectSignalSlots(self):
        self.HomeButton.clicked.connect(self.redirect_HomePage)
        # self.TeacherSheets.clicked.connect(self.redirect_TeacherSheets)
        # self.SetLaws.clicked.connect(self.redirect_SetLaws)
        # self.SetOperations.clicked.connect(self.redirect_SetOperations)
        # self.VennDiagrams.clicked.connect(self.redirect_VennDiagrams)
        pass

    def redirect_HomePage(self):
        import Main_Screen.MainScreen as Main
        self.w = Main.MainWindow()
        self.w.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())