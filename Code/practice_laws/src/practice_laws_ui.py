# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'practice_laws.ui'
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
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: rgba(255, 246, 233, 168);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(73,133,168);\n"
"    border-radius: 20%;\n"
"    color: white;\n"
"    font: 16pt \"Serif\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(93,153,168);\n"
"    border: 2px solid rgb(53, 54, 90);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.Question_label = QtWidgets.QLabel(self.centralwidget)
        self.Question_label.setGeometry(QtCore.QRect(230, 150, 941, 631))
        self.Question_label.setStyleSheet("#Question_label{\n"
"    background-color: rgb(73, 133, 168);\n"
"    font: italic 26pt \"Serif\";\n"
"    color: white;\n"
"    border-radius: 20%;\n"
"    padding-top: 15%;\n"
"}\n"
"\n"
"#Question_label::hover{\n"
"    background-color:transparent;\n"
"    color: black;\n"
"}")
        self.Question_label.setTextFormat(QtCore.Qt.RichText)
        self.Question_label.setScaledContents(True)
        self.Question_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Question_label.setObjectName("Question_label")
        self.Answer_label = QtWidgets.QLabel(self.centralwidget)
        self.Answer_label.setGeometry(QtCore.QRect(230, 150, 941, 631))
        self.Answer_label.setStyleSheet("#Answer_label{\n"
"    background-color: white;\n"
"    border-radius: 20%;\n"
"    font: bold 32pt \"Serif\";\n"
"}")
        self.Answer_label.setTextFormat(QtCore.Qt.RichText)
        self.Answer_label.setScaledContents(True)
        self.Answer_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Answer_label.setObjectName("Answer_label")
        self.Image_label = QtWidgets.QLabel(self.centralwidget)
        self.Image_label.setGeometry(QtCore.QRect(390, 410, 671, 351))
        self.Image_label.setText("")
        self.Image_label.setPixmap(QtGui.QPixmap("practice_laws/resources/ass_law.png"))
        self.Image_label.setScaledContents(True)
        self.Image_label.setObjectName("Image_label")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(1220, 790, 111, 51))
        self.next_button.setStyleSheet("")
        self.next_button.setObjectName("next_button")
        self.main_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.main_menu_button.setGeometry(QtCore.QRect(50, 790, 131, 51))
        self.main_menu_button.setStyleSheet("")
        self.main_menu_button.setObjectName("main_menu_button")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(40, 30, 1331, 101))
        self.header.setStyleSheet("#header{\n"
"    font: 70pt bold \"Serif\";\n"
"    text-align: center;\n"
"\n"
"}")
        self.header.setObjectName("header")
        self.Answer_label.raise_()
        self.Image_label.raise_()
        self.next_button.raise_()
        self.header.raise_()
        self.Question_label.raise_()
        self.main_menu_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Question_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">According to Associative Law:</p><p align=\"center\">(A|B) | C = ??? </p></body></html>"))
        self.Answer_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\">A | (B|C)</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.next_button.setText(_translate("MainWindow", "Next"))
        self.main_menu_button.setText(_translate("MainWindow", "Main Menu"))
        self.header.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">FUNDAMENTAL SET LAWS</p></body></html>"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
