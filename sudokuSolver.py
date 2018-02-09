from stripper import Stripper
from puzzle import Puzzle

class sudokuSolver:
    
    #initial setup
    puzFile = input("Enter puzzle file: ")
    puzList = Stripper.strip("testPuzz")
    puzz = Puzzle(puzList)

    def backtracker(self,i):
        #solve the puzzle using a backtracking algo
        if(i == len(puzz)):
            if(puzz.iSolved()):
                return true

        num = 1
        while(num < 10):
            puzz[i] = num
            if(puzz.isSolved()):
               backtracker(i+1) 
            else:
                i += 1
                    



    def isSolved(self,x,y):
        if(puzz.checkRow(x,y) && puzz.checkColumn(x,y) && puzz.checkBox(x,y):
            return True
        else:
            return False

