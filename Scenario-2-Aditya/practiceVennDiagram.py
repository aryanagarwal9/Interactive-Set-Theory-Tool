import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from practiceVennDiagram_ui import Ui_MainWindow
import matplotlib.pyplot as plt
from matplotlib_venn import venn2_unweighted, venn3_unweighted
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Venn_data():

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, num_sets):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Venn Diagrams")
        self.num_sets = num_sets
        self.unshaded_color = "#aed7ff"
        self.shaded_color = "#3598ff"
        self.checkboxes = {self.Area1: ["10", "100", 0], self.Area2: ["01", "010", 0], self.Area3: ["11", "001", 0], self.Area4: ["00", "110", 0], self.Area5: ["00", "101", 0], self.Area6: ["00", "011", 0], self.Area7: ["00", "111", 0]}
        self.setupPlotSpace()
        self.setupLayout()
        self.plotUnshaded()
        self.connectSignalSlots()

    def setupPlotSpace(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.A = set()
        self.B = set()
        self.C = set()
        self.setupLayout()

    def setupLayout(self):
        self.diagramLayout = QHBoxLayout(self.DiagramFrame)
        self.diagramLayout.setObjectName("diagramLayout")
        self.diagramLayout.addWidget(self.canvas)
        self.diagramLayout.setGeometry(QRect(0, 0, 600, 400))

    def connectSignalSlots(self):
        # self.nextButton.clicked.connect(self.nextPressed)
        # self.submitButton.clicked.connect(self.submitPressed)
        self.Area1.stateChanged.connect(lambda: self.shadeArea1(self.Area1))
        self.Area2.stateChanged.connect(lambda: self.shadeArea2(self.Area2))
        self.Area3.stateChanged.connect(lambda: self.shadeArea3(self.Area3))
        self.Area4.stateChanged.connect(lambda: self.shadeArea_3sets(self.Area4))
        self.Area5.stateChanged.connect(lambda: self.shadeArea_3sets(self.Area5))
        self.Area6.stateChanged.connect(lambda: self.shadeArea_3sets(self.Area6))
        self.Area7.stateChanged.connect(lambda: self.shadeArea_3sets(self.Area7))

    def submitPressed(self):
        pass

    def nextPressed(self):
        pass

    def shadeArea1(self, area):
        if self.num_sets == 2:
            self.shadeArea1_2sets()
        else:
            self.shadeArea_3sets(area)

    def shadeArea1_2sets(self):
        self.figure.clear()

        diagram = venn2_unweighted([self.A, self.B], set_labels=("A", "B"))
        diagram.get_label_by_id("10").set_text("1")
        diagram.get_label_by_id("01").set_text("2")
        diagram.get_label_by_id("11").set_text("3")
        if self.checkboxes[self.Area2][2] == 1:
            diagram.get_patch_by_id(self.checkboxes[self.Area2][0]).set_color(self.shaded_color)
        else:
            diagram.get_patch_by_id(self.checkboxes[self.Area2][0]).set_color(self.unshaded_color)

        if self.checkboxes[self.Area3][2] == 1:
            diagram.get_patch_by_id(self.checkboxes[self.Area3][0]).set_color(self.shaded_color)
        else:
            diagram.get_patch_by_id(self.checkboxes[self.Area3][0]).set_color(self.unshaded_color)

        if self.Area1.isChecked():
            diagram.get_patch_by_id(self.checkboxes[self.Area1][0]).set_color(self.shaded_color)
            self.checkboxes[self.Area1][2] = 1
        else:
            diagram.get_patch_by_id(self.checkboxes[self.Area1][0]).set_color(self.unshaded_color)
            self.checkboxes[self.Area1][2] = 0
        self.canvas.draw()

    def shadeArea_3sets(self, area):
        self.figure.clear()
        diagram = venn3_unweighted([self.A, self.B, self.C], set_labels=("A", "B", "C"))
        diagram.get_label_by_id("100").set_text("1")
        diagram.get_label_by_id("010").set_text("2")
        diagram.get_label_by_id("001").set_text("3")
        diagram.get_label_by_id("110").set_text("4")
        diagram.get_label_by_id("101").set_text("5")
        diagram.get_label_by_id("011").set_text("6")
        diagram.get_label_by_id("111").set_text("7")

        for checkbox in self.checkboxes:
            if checkbox == area:
                if checkbox.isChecked():
                    diagram.get_patch_by_id(self.checkboxes[checkbox][1]).set_color(self.shaded_color)
                    self.checkboxes[checkbox][2] = 1
                else:
                    diagram.get_patch_by_id(self.checkboxes[checkbox][1]).set_color(self.unshaded_color)
                    self.checkboxes[checkbox][2] = 0
            else:
                if self.checkboxes[checkbox][2] == 1:
                    diagram.get_patch_by_id(self.checkboxes[checkbox][1]).set_color(self.shaded_color)
                else:
                    diagram.get_patch_by_id(self.checkboxes[checkbox][1]).set_color(self.unshaded_color)
        self.canvas.draw()

    def shadeArea2(self, area):
        if self.num_sets == 2:
            self.shadeArea2_2sets()
        else:
            self.shadeArea_3sets(area)

    def shadeArea2_2sets(self):
        self.figure.clear()
        diagram = venn2_unweighted([self.A, self.B], set_labels=("A", "B"))
        diagram.get_label_by_id("10").set_text("1")
        diagram.get_label_by_id("01").set_text("2")
        diagram.get_label_by_id("11").set_text("3")
        if self.checkboxes[self.Area1][2] == 1:
            diagram.get_patch_by_id(self.checkboxes[self.Area1][0]).set_color(self.shaded_color)
        else:
            diagram.get_patch_by_id(self.checkboxes[self.Area1][0]).set_color(self.unshaded_color)

        if self.checkboxes[self.Area3][2] == 1:
            diagram.get_patch_by_id(self.checkboxes[self.Area3][0]).set_color(self.shaded_color)
        else:
            diagram.get_patch_by_id(self.checkboxes[self.Area3][0]).set_color(self.unshaded_color)

        if self.Area2.isChecked():
            diagram.get_patch_by_id(self.checkboxes[self.Area2][0]).set_color(self.shaded_color)
            self.checkboxes[self.Area2][2] = 1
        else:
            diagram.get_patch_by_id(self.checkboxes[self.Area2][0]).set_color(self.unshaded_color)
            self.checkboxes[self.Area2][2] = 0
        self.canvas.draw()


    def shadeArea3(self, area):
        if self.num_sets == 2:
            self.shadeArea3_2sets()
        else:
            self.shadeArea_3sets(area)

    def shadeArea3_2sets(self):
        self.figure.clear()
        diagram = venn2_unweighted([self.A, self.B], set_labels=("A", "B"))
        diagram.get_label_by_id("10").set_text("1")
        diagram.get_label_by_id("01").set_text("2")
        diagram.get_label_by_id("11").set_text("3")
        if self.checkboxes[self.Area1][2] == 1:
            diagram.get_patch_by_id(self.checkboxes[self.Area1][0]).set_color(self.shaded_color)
        else:
            diagram.get_patch_by_id(self.checkboxes[self.Area1][0]).set_color(self.unshaded_color)

        if self.checkboxes[self.Area2][2] == 1:
            diagram.get_patch_by_id(self.checkboxes[self.Area2][0]).set_color(self.shaded_color)
        else:
            diagram.get_patch_by_id(self.checkboxes[self.Area2][0]).set_color(self.unshaded_color)

        if self.Area3.isChecked():
            diagram.get_patch_by_id(self.checkboxes[self.Area3][0]).set_color(self.shaded_color)
            self.checkboxes[self.Area3][2] = 1
        else:
            diagram.get_patch_by_id(self.checkboxes[self.Area3][0]).set_color(self.unshaded_color)
            self.checkboxes[self.Area3][2] = 0
        self.canvas.draw()

    def plotUnshaded(self):
        if self.num_sets == 2:
            self.HiddenFrame.hide()
            self.plotUnshaded_2sets()
        else:
            self.plotUnshaded_3sets()

    def plotUnshaded_2sets(self):
        self.figure.clear()
        diagram = venn2_unweighted([self.A, self.B], set_labels=("A", "B"))
        diagram.get_label_by_id("10").set_text("1")
        diagram.get_label_by_id("01").set_text("2")
        diagram.get_label_by_id("11").set_text("3")
        diagram.get_patch_by_id("10").set_color(self.unshaded_color)
        diagram.get_patch_by_id("01").set_color(self.unshaded_color)
        diagram.get_patch_by_id("11").set_color(self.unshaded_color)

        self.canvas.draw()

    def plotUnshaded_3sets(self):
        self.figure.clear()
        diagram = venn3_unweighted([self.A, self.B, self.C], set_labels=("A", "B", "C"))
        diagram.get_label_by_id("100").set_text("1")
        diagram.get_label_by_id("010").set_text("2")
        diagram.get_label_by_id("001").set_text("3")
        diagram.get_label_by_id("110").set_text("4")
        diagram.get_label_by_id("101").set_text("5")
        diagram.get_label_by_id("011").set_text("6")
        diagram.get_label_by_id("111").set_text("7")
        diagram.get_patch_by_id("100").set_color(self.unshaded_color)
        diagram.get_patch_by_id("010").set_color(self.unshaded_color)
        diagram.get_patch_by_id("001").set_color(self.unshaded_color)
        diagram.get_patch_by_id("110").set_color(self.unshaded_color)
        diagram.get_patch_by_id("101").set_color(self.unshaded_color)
        diagram.get_patch_by_id("011").set_color(self.unshaded_color)
        diagram.get_patch_by_id("111").set_color(self.unshaded_color)

        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow(3)
    win.show()
    sys.exit(app.exec_())

