# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set_operations.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1438, 806)
        MainWindow.setStyleSheet("QWidget{\n"
" background-color: rgb(255,246,233);\n"
"}\n"
"\n"
"QLabel{\n"
"    background-color:rgb(73, 133, 168);\n"
"    border-radius: 20%;\n"
"    color: white;\n"
"    font: 26pt \"Verdana\";\n"
"}\n"
"\n"
"QRadioButton{\n"
"    background-color:white;\n"
"    border-radius: 20%;\n"
"    border: 1px solid black;\n"
"    font: 22pt \"Verdana\";\n"
"}\n"
"\n"
"QRadioButton::hover{\n"
"    background-color: rgb(221,221,221);\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"    width: 70px;\n"
"    height: 30px;\n"
"    margin-left: 10px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked{\n"
"    image: url(/Users/adityaparashar/Education/UCL/ENGF0002/Scenario/Code/Practice_setOperations/radio-checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked{\n"
"    image: url(/Users/adityaparashar/Education/UCL/ENGF0002/Scenario/Code/Practice_setOperations/radio-unchecked.png);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:rgb(73,133,168);\n"
"    color:white;\n"
"    border-radius: 30%;\n"
"    font: 20pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color:rgb(93,153,168);\n"
"    border: 2px solid black;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.question = QtWidgets.QLabel(self.centralwidget)
        self.question.setGeometry(QtCore.QRect(170, 40, 1091, 151))
        self.question.setStyleSheet("")
        self.question.setObjectName("question")
        self.option1_button = QtWidgets.QRadioButton(self.centralwidget)
        self.option1_button.setGeometry(QtCore.QRect(200, 230, 881, 81))
        self.option1_button.setStyleSheet("")
        self.option1_button.setObjectName("option1_button")
        self.option2_button = QtWidgets.QRadioButton(self.centralwidget)
        self.option2_button.setGeometry(QtCore.QRect(200, 560, 881, 81))
        self.option2_button.setStyleSheet("")
        self.option2_button.setText("")
        self.option2_button.setObjectName("option2_button")
        self.option3_button = QtWidgets.QRadioButton(self.centralwidget)
        self.option3_button.setGeometry(QtCore.QRect(200, 340, 881, 81))
        self.option3_button.setStyleSheet("")
        self.option3_button.setText("")
        self.option3_button.setObjectName("option3_button")
        self.option4_button = QtWidgets.QRadioButton(self.centralwidget)
        self.option4_button.setGeometry(QtCore.QRect(200, 450, 881, 81))
        self.option4_button.setStyleSheet("")
        self.option4_button.setText("")
        self.option4_button.setObjectName("option4_button")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(1210, 710, 141, 61))
        self.next_button.setStyleSheet("")
        self.next_button.setObjectName("next_button")
        self.mainMenu_button = QtWidgets.QPushButton(self.centralwidget)
        self.mainMenu_button.setGeometry(QtCore.QRect(100, 710, 181, 61))
        self.mainMenu_button.setStyleSheet("")
        self.mainMenu_button.setObjectName("mainMenu_button")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(1000, 710, 161, 61))
        self.submit_button.setStyleSheet("")
        self.submit_button.setObjectName("submit_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.question.setText(_translate("MainWindow", "<html><head/><body><p>&nbsp; &nbsp; c wvjkenvrnwlkvnws</p></body></html>"))
        self.option1_button.setText(_translate("MainWindow", "nfwnvlkwnfwpv"))
        self.next_button.setText(_translate("MainWindow", "Next"))
        self.mainMenu_button.setText(_translate("MainWindow", "Main Menu"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
