import json
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Code.Practice_VennDiagrams.practiceVennDiagram_ui import Ui_MainWindow
import matplotlib.pyplot as plt
from matplotlib_venn import venn2_unweighted, venn3_unweighted
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Venn_data:
    def __init__(self, question_id, question, num_sets, answer):
        self.question_id = question_id
        self.question = question
        self.num_sets = num_sets
        self.answer = answer


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Venn Diagrams")
        self.setFixedWidth(1500)
        self.setFixedHeight(800)
        self.unshaded_color = "#aed7ff"
        self.shaded_color = "#3598ff"
        self.checkboxes = {self.Area1: ["10", "100", 0], self.Area2: ["01", "010", 0], self.Area3: ["11", "001", 0],
                           self.Area4: ["00", "110", 0], self.Area5: ["00", "101", 0], self.Area6: ["00", "011", 0],
                           self.Area7: ["00", "111", 0]}
        self.patches = {1: ["10", "100"], 2: ["01", "010"], 3: ['11', '001'], 4: ["00", '110'], 5: ["00", '101'],
                        6: ['00', '011'], 7: ['00', '111']}
        self.setupPlotSpace()
        self.setupLayout()
        self.venn_diagram_data = add_venn_data('../Practice_VennDiagrams/vennDiagram.json')
        self.counter = 0
        self.score = 0
        self.num_sets = self.venn_diagram_data[self.counter].num_sets
        self.plotUnshaded()
        self.connectSignalSlots()
        self.display_first_question()
        self.buttonFrame.hide()

    def setupPlotSpace(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.A = set()
        self.B = set()
        self.C = set()

    def setupLayout(self):
        self.diagramLayout = QHBoxLayout(self.DiagramFrame)
        self.diagramLayout.setObjectName("diagramLayout")
        self.diagramLayout.addWidget(self.canvas)

    def connectSignalSlots(self):
        self.nextButton.clicked.connect(self.nextPressed)
        self.submitButton.clicked.connect(self.submitPressed)
        self.yourAnswer.clicked.connect(self.show_myAnswer)
        self.mainMenu.clicked.connect(self.mainMenu_pressed)
        self.Area1.stateChanged.connect(lambda: self.shadeArea1(self.Area1))
        self.Area2.stateChanged.connect(lambda: self.shadeArea2(self.Area2))
        self.Area3.stateChanged.connect(lambda: self.shadeArea3(self.Area3))
        self.Area4.stateChanged.connect(lambda: self.shadeArea_3sets(self.Area4))
        self.Area5.stateChanged.connect(lambda: self.shadeArea_3sets(self.Area5))
        self.Area6.stateChanged.connect(lambda: self.shadeArea_3sets(self.Area6))
        self.Area7.stateChanged.connect(lambda: self.shadeArea_3sets(self.Area7))

    def mainMenu_pressed(self):
        import Code.Main_Screen.MainScreen as Main
        self.window = Main.MainWindow()
        self.window.show()
        self.hide()

    def display_first_question(self):
        _translate = QCoreApplication.translate
        question_label = "<html><head/><body><p>&nbsp; &nbsp;" + str(self.venn_diagram_data[self.counter].question_id) + ". " + self.venn_diagram_data[self.counter].question + "</p></body></html>"
        self.Question.setText(_translate("MainWindow", question_label))

    def submitPressed(self):
        _translate = QCoreApplication.translate
        if self.counter == len(self.venn_diagram_data) - 1:
            self.nextButton.setText(_translate("MainWindow", "Finish"))
            self.submitButton.hide()

        result = self.verify_answer(self.venn_diagram_data[self.counter].question_id,
                                    self.venn_diagram_data[self.counter].question,
                                    self.venn_diagram_data[self.counter].num_sets,
                                    self.venn_diagram_data[self.counter].answer)
        self.plot_answer(self.venn_diagram_data[self.counter].answer)
        self.Answer.show()
        self.display_answerLabel()
        self.buttonFrame.show()
        self.show_result(result)
        self.setEnabledFalse()

    def show_myAnswer(self):
        myAnswer = self.storeAnswer()
        self.plot_answer(myAnswer)
        self.Answer.hide()

    def storeAnswer(self):
        ans_string = ""
        for checkbox in self.checkboxes:
            ans_string += str(self.checkboxes[checkbox][2])
        return ans_string

    def display_answerLabel(self):
        _translate = QCoreApplication.translate
        self.Answer.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ANSWER -&gt; </p></body></html>"))
        self.Answer.raise_()

    def nextPressed(self):
        _translate = QCoreApplication.translate
        self.counter += 1
        if self.counter == len(self.venn_diagram_data):
            self.display_scorePage()

        else:
            self.update_ui(self.venn_diagram_data[self.counter].question_id,
                                    self.venn_diagram_data[self.counter].question,
                                    self.venn_diagram_data[self.counter].num_sets,
                                    self.venn_diagram_data[self.counter].answer)

            self.clear_checkboxes()
            self.clear_result()
            self.setEnabledTrue()
            self.plotUnshaded()

    def display_scorePage(self):
        import Code.ScoreDisplay.scoreDisplay as score
        self.score_window = score.MainWindow(self.score,len(self.venn_diagram_data))
        self.score_window.show()
        self.hide()

    def update_ui(self, question_id, question, num_sets, answer):
        _translate = QCoreApplication.translate
        question_label = "<html><head/><body><p>&nbsp; &nbsp;" + str(question_id) + ". " + question + "</p></body></html>"
        self.Question.setText(_translate("MainWindow", question_label))
        self.num_sets = num_sets
        self.Answer.setText(_translate("MainWindow", ""))

    def setEnabledFalse(self):
        for i in self.checkboxes:
            i.setEnabled(False)

    def setEnabledTrue(self):
        for i in self.checkboxes:
            i.setEnabled(True)

    def clear_plot(self):
        self.figure.clear()
        self.canvas.draw()

    def clear_checkboxes(self):
        for checkbox in self.checkboxes:
            checkbox.setChecked(False)

    def clear_result(self):
        _translate = QCoreApplication.translate
        self.ResultLabel.setText(_translate("MainWindow", ""))

    def show_result(self, result):
        _translate = QCoreApplication.translate
        if result:
            self.score += 1
            self.ResultLabel.setStyleSheet("#ResultLabel{\n"
                                           "color: rgb(58, 142, 52); \n"
                                           "font: bold \"Verdana\"; \n"
                                           "}\n"
                                           "")
            self.ResultLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Correct Answer :)</p></body></html>"))

        else:
            self.ResultLabel.setStyleSheet("#ResultLabel{\n"
                                           "color: rgb(253,109,123); \n"
                                           "font: bold \"Verdana\"; \n"
                                           "}\n"
                                           "")
            self.ResultLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Wrong Answer :(</p></body></html>"))
        self.ResultLabel.raise_()

    def plot_answer(self, answer):
        if self.num_sets == 2:
            self.plotAnswer_2sets(answer)
        else:
            self.plotAnswer_3sets(answer)

    def plotAnswer_2sets(self, answer):
        self.figure.clear()
        diagram = venn2_unweighted([self.A, self.B], set_labels=("A", "B"))
        diagram.get_label_by_id("10").set_text("1")
        diagram.get_label_by_id("01").set_text("2")
        diagram.get_label_by_id("11").set_text("3")

        for i in range(3):
            if answer[i] == '1':
                diagram.get_patch_by_id(self.patches[i + 1][0]).set_color(self.shaded_color)
            else:
                diagram.get_patch_by_id(self.patches[i + 1][0]).set_color(self.unshaded_color)
        self.canvas.draw()

    def plotAnswer_3sets(self, answer):
        self.figure.clear()
        diagram = venn3_unweighted([self.A, self.B, self.C], set_labels=("A", "B", "C"))
        diagram.get_label_by_id("100").set_text("1")
        diagram.get_label_by_id("010").set_text("2")
        diagram.get_label_by_id("001").set_text("3")
        diagram.get_label_by_id("110").set_text("4")
        diagram.get_label_by_id("101").set_text("5")
        diagram.get_label_by_id("011").set_text("6")
        diagram.get_label_by_id("111").set_text("7")

        for i in range(len(self.patches)):
            if answer[i] == '1':
                diagram.get_patch_by_id(self.patches[i + 1][1]).set_color(self.shaded_color)
            else:
                diagram.get_patch_by_id(self.patches[i + 1][1]).set_color(self.unshaded_color)
        self.canvas.draw()

    def verify_answer(self, question_id, question, num_sets, answer):
        i = 0
        for checkbox in self.checkboxes:
            if self.num_sets == 2 and i > 3:
                break
            if self.checkboxes[checkbox][2] != int(answer[i]):
                return False
            i += 1
        return True

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
            self.HiddenFrame.show()
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


def add_venn_data(file):
    venn_data = []
    with open(file, 'r') as f:
        data = json.load(f)

        for ques in data["venn_diagrams"]:
            ques_data = Venn_data(ques["qno"], ques["questions"], ques["num_sets"], ques["answer"])
            venn_data.append(ques_data)
        return venn_data
