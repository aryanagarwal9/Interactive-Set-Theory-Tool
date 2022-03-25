import sys
import json
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Code.Create_Exercises.src.CreateExercises_ui import Ui_MainWindow

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Create Exercises")
        self.setFixedWidth(1500)
        self.setFixedHeight(800)
        self.connectSignalsSlots()
        self.qnList=[]
        self.errorLabel.hide()
        
    def connectSignalsSlots(self):
        translate=QtCore.QCoreApplication.translate
        self.A.clicked.connect(lambda:self.whenAisClicked(translate))
        self.B.clicked.connect(lambda:self.whenBisClicked(translate))
        self.C.clicked.connect(lambda:self.whenCisClicked(translate))
        self.AND.clicked.connect(lambda:self.whenANDisClicked(translate))
        self.OR.clicked.connect(lambda:self.whenORisClicked(translate))
        self.minus.clicked.connect(lambda:self.whenMinusisClicked(translate))
        self.compliment.clicked.connect(lambda:self.whenComplimentisClicked(translate))
        self.submitButton.clicked.connect(lambda:self.whenNextisClicked(translate))
        self.finishButton.clicked.connect(lambda:self.whenSubmitisClicked(translate))
        self.homeButton.clicked.connect(lambda: self.homeButtonClicked(translate))
        
    def homeButtonClicked(self, translate):
        import Code.Main_Screen.MainScreen as Main
        self.window1 = Main.MainWindow()
        self.window1.show()
        self.hide()

    def whenAisClicked(self,translate):
            self.eqn_input.setText(translate("MainWindow",self.eqn_input.toPlainText()+"A"))
    
    def whenBisClicked(self,translate):
            self.eqn_input.setText(translate("MainWindow",self.eqn_input.toPlainText()+"B"))
    
    def whenCisClicked(self,translate):
            self.eqn_input.setText(translate("MainWindow",self.eqn_input.toPlainText()+"C"))
    
    def whenANDisClicked(self,translate):
            self.eqn_input.setText(translate("MainWindow",self.eqn_input.toPlainText()+"∩"))
        
    def whenORisClicked(self,translate):
            self.eqn_input.setText(translate("MainWindow",self.eqn_input.toPlainText()+"∪"))
    
    def whenMinusisClicked(self,translate):
            self.eqn_input.setText(translate("MainWindow",self.eqn_input.toPlainText()+"\\"))

    def whenComplimentisClicked(self,translate):
            self.eqn_input.setText(translate("MainWindow",self.eqn_input.toPlainText()+"'"))
    
    
    def checkRadioButton(self):
            noOfSets=''
            if self.no2.isChecked():
                    noOfSets='2'
            
            if self.no3.isChecked():
                    noOfSets='3'
            
            return noOfSets
    
    def detectWrongInput(self,input):
        correct_string='ABC\'(){}\u2229\u222a'
        res=True
        for c in input:
            if c not in correct_string:
                res=False
        
        return res
    
    def whenNextisClicked(self,translate):
        
        inputString=self.eqn_input.toPlainText()
        res=self.detectWrongInput(inputString)
        
        if res:
           self.errorLabel.hide()
           datastring={
              'NumberOfSets':self.checkRadioButton(),
              'Set Equation':inputString,
              'A':self.elem_input1.toPlainText(),
              'B':self.elem_input2.toPlainText(),
              'C':self.elem_input3.toPlainText()
                      }
        
           self.qnList.append(datastring)
        
           with open('../Create_Exercises/resources/createData.json','w') as out:
               json.dump(self.qnList,out)
        
           self.eqn_input.setText(translate("MainWindow",""))
           self.elem_input1.setText(translate("MainWindow",""))
           self.elem_input2.setText(translate("MainWindow",""))
           self.elem_input3.setText(translate("MainWindow",""))
           
        
        else:
                self.errorLabel.show()
    
    def whenSubmitisClicked(self,translate):
        import Code.Main_Screen.MainScreen as Main
        self.window = Main.MainWindow()
        self.window.show()
        self.hide()
