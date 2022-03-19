class libfunc:
    def __init__(self, myobj):
        myobj = myobj
        
  
    def add(self, first, second):
        return first+second
    def subtract(self, first, second):
        return first-second
    def multiply(self, first, second):
        return first*second
    def divide(self, first, second):
        return first/second
    def isInRange(self, minRange, maxRange, num):
        if num > minRange and num < maxRange:
            return True
        else:
            return False

    def scalc(self, expression):
        thestrings=expression.split(",")
        if thestrings[2]=="+":
            result=self.add(int(thestrings[0]), int(thestrings[1]))
        if thestrings[2]=="-":
            result=self.subtract(int(thestrings[0]), int(thestrings[1]))
        if thestrings[2]=="*":
            result=self.multiply(int(thestrings[0]), int(thestrings[1]))
        if thestrings[2]=="/":
            result=self.divide(int(thestrings[0]), int(thestrings[1]))
        return result

    def allinone(self, first, second):
        self.res={}
        self.res['add']=first+second
        self.res['subtract']=first-second
        self.res['multiply']=first*second
        self.res['divide/scalc']=first/second
        return self.res
