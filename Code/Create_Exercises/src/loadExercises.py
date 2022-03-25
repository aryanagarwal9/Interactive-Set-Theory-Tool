import sys
import json

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Code.Create_Exercises.src.loadExercises_ui import Ui_MainWindow
from Code.Create_Exercises.src.ValidateAnswer import ValidateAnswer

class MainWindow(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Load Teacher Exercises")
        self.setFixedWidth(1500)
        self.setFixedHeight(800)
        self.translate=QCoreApplication.translate
        self.qn_no=0
        self.readQn(self.qn_no)
        self.nextButton.clicked.connect(lambda:self.doNext())
        self.userAnswerList=[]
        self.nextButton.clicked.connect(lambda:self.storeUserAnswers())
        self.doneButton.hide()
        self.homeButton.clicked.connect(lambda: self.homeButtonClicked())

    def homeButtonClicked(self):
        import Code.Main_Screen.MainScreen as Main
        self.window1 = Main.MainWindow()
        self.window1.show()
        self.hide()
    # one function to keep track of question number
    # one function to check when next is clicked
    
        
    # a function which starts a loop
    # reads the first question
    # waits for answers
    # once next is clicked 
    # read the next question
    
    # read
    # wait 
    # once clicked loop back
    
    def storeUserAnswers(self):
        user_answer=self.answerInput.toPlainText()
        self.answerInput.setText(self.translate("MainWindow",""))
        self.userAnswerList.append(user_answer)
        
        if self.qn_no == 2:
            self.nextButton.setText(self.translate("MainWindow", "Finish"))
        if self.qn_no == 3:
            self.answerInput.setText(self.translate("MainWindow",""))
            with open('../Create_Exercises/resources/userAnswers.json','w') as out:
                json.dump(self.userAnswerList,out)
        
            validate=ValidateAnswer()
            validate.storeAnswers()
            validate.countScore()
        
            final_answers=[]
            with open('../Create_Exercises/resources/answers.json', 'r') as f:
                final_answers=json.load(f)

            score=final_answers[0]
            answers=final_answers[1]
        
            self.display_scorePage(score, answers)
    
    def getUserAnswers(self):
        return self.userAnswerList
        
    def display_scorePage(self, score, answers):
        import Code.Create_Exercises.src.scoreQn as score1
        self.score_window = score1.MainWindow(score, answers)
        self.score_window.show()
        self.hide()
        
    def convertToSet(self,stringg):
        ns=''
        for c in stringg:
            if c=='{' or c=='}' or c==',':
                pass
            else:
                ns=c+ns
        
        newset=set(ns)
        return newset
        
    def doNext(self):
          self.qn_no+=1
          self.readQn(self.qn_no)  
     
    def readQn(self,qn_no):
        # i is number of questions
        with open('../Create_Exercises/resources/createData.json', 'r') as f:
              qnList=json.load(f)
        
        try:
          qnData=qnList[qn_no]
          if qnData["A"] == "":
              qnData["A"] = "N/A"
          if qnData["B"] == "":
              qnData["B"] = "N/A"
          if qnData["C"] == "":
              qnData["C"] = "N/A"

          self.elem_input1.setText(self.translate("MainWindow","{ "+qnData["A"] + " }"))
          self.elem_input2.setText(self.translate("MainWindow","{ "+qnData["B"] + " }"))
          self.elem_input3.setText(self.translate("MainWindow","{ "+qnData["C"] + " }"))
            
          self.eqn_input.setText(self.translate("MainWindow",qnData["Set Equation"]))
        except IndexError:
            print("End of Number of Questions")
        except UnboundLocalError:
            print("")

    
            
            
            
            
   
            
            
            
    