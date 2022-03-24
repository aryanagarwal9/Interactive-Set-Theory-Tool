import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Code.Practice_homepage.selectPracticeQn_ui import Ui_MainWindow

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Practice Modes")
        self.setFixedWidth(1500)
        self.setFixedHeight(800)
        self.connectSignalSlots()

    def connectSignalSlots(self):
        self.HomeButton.clicked.connect(self.redirect_HomePage)
        # self.TeacherSheets.clicked.connect(self.redirect_TeacherSheets)
        self.SetLaws.clicked.connect(self.redirect_SetLaws)
        self.SetOperations.clicked.connect(self.redirect_SetOperations)
        self.VennDiagrams.clicked.connect(self.redirect_VennDiagrams)

    def redirect_HomePage(self):
        import Code.Main_Screen.MainScreen as Main
        self.window1 = Main.MainWindow()
        self.window1.show()
        self.hide()

    def redirect_SetLaws(self):
        import Code.practice_laws.src.practice_laws as laws
        self.window2 = laws.MainWindow()
        self.window2.show()
        self.hide()

    def redirect_SetOperations(self):
        import Code.Practice_SetOperations.src.set_operations as set_operations
        self.window3 = set_operations.MainWindow()
        self.window3.show()
        self.hide()

    def redirect_VennDiagrams(self):
        import Code.Practice_VennDiagrams.practiceVennDiagram as Venns
        self.window = Venns.MainWindow()
        self.window.show()

        self.w = Main.MainWindow()
        self.w.show()
        main
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())