import json

class ValidateAnswer():
    
    def __init__(self):
        self.score=0
        self.answerList=[]
        self.answers=[]    
    # call calculate ans on each json question
    # add it to answerList
    # new method to calculate score by 
    # add to load exercises the feature to store answers entered by the user.
    # use that stored data to validate our answer and calculate score
    
    def storeAnswers(self):
        jsonList=[]
        with open('../Create_Exercises/resources/createData.json', 'r') as inputFile:
            jsonList=json.load(inputFile)
        
        for qnDict in jsonList:
            self.calculateAns(qnDict)
        
        # print("here",self.answerList)
             
    def calculateAns(self,qnDict):
        inter='\u2229'
        union='\u222a'
        try:
            noOfsets=qnDict['NumberOfSets']
            setEqn=qnDict['Set Equation']
            bracket_prior=self.getPriority(setEqn)
            setEqn=self.newSetEqn(setEqn)
            a=qnDict['A']
            b=qnDict['B']
            c=qnDict['C']
        except KeyError:
            print("Corrupted Data")
        
        setA=self.convertToSet(a)
        setB=self.convertToSet(b)
        setC=self.convertToSet(c)
        
        set_exp=None
        if noOfsets=='2':
            
            if union in setEqn:
                set_exp=setA|setB
            
            else:
                set_exp=setA & setB
        
        if noOfsets=='3':
            countUnion=setEqn.count(union)
            countInter=setEqn.count(inter)
            
            if countUnion==2 or countInter==2:
                if countUnion==2:
                    set_exp=setA | setB | setC
                
                if countInter==2:
                    set_exp=setA & setB & setC
            
            else:
                indexOfUnion=setEqn.index(union)
                indexOfInter=setEqn.index(inter)
                
                if indexOfUnion==1 and indexOfInter==3:
                   if bracket_prior==1:
                       set_exp=(setA | setB) &setC
                    
                   else:
                       set_exp=setA | (setB & setC)
                    
                else:
                    if bracket_prior==1:
                        set_exp=(setA & setB) | setC
                    
                    else:
                        set_exp=setA & (setB | setC)
        
        answer=set_exp
        # print(set_exp)
        self.answerList.append(answer)
    
                   
                
                    
    def countScore(self):
        user_answerList=[]
        score=0
        with open('../Create_Exercises/resources/userAnswers.json', 'r') as f:
            user_answers=json.load(f)
            user_answerList=self.createSetList(user_answers)
        
        for i in range(0,len(self.answerList)):
            if user_answerList[i]==self.answerList[i]:
                score+=1
                self.answers.append('Correct')
            
            else:
                self.answers.append('Wrong')
        
        score=str(score)+'/'+str(len(self.answerList))
        final_score=[score,self.answers]   
        with open('../Create_Exercises/resources/answers.json','w') as out:
            json.dump(final_score,out)
        
        return score
    
        
        
    def createSetList(self,mylist):
        newlist=[]
        for item in mylist:
            myset=self.convertToSet(item)
            newlist.append(myset)
        
        return newlist
            
                            
    def getPriority(self,setEqn):
        if setEqn[0]=='(':
            return 1
        
        return 0
    
      
    def newSetEqn(self,setEqn):
        ns=''
        for c in setEqn:
            if c==' ' or c=='(' or c==')':
                pass
            else:
                ns+=c
        
        return ns
    
    def convertToSet(self,stringg):
        ns=''
        for c in stringg:
            if c=='{' or c=='}' or c==',' or c==' ':
                pass
            
            else:
                ns=c+ns
        
        newset=set(ns)
        return newset