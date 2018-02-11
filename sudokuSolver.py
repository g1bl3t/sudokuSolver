from stripper import Stripper
from newPuzzle import Puzzle
import time

class SudokuSolver:
    puzz = None
    #initial setup
    def __init__(self):
        puzFile = input("Enter puzzle file: ")
        puzList = Stripper.strip(puzFile)
        print(puzList)
        self.puzz = Puzzle(puzList)
    
    def backtracker(self,i):
        #solve the puzzle using a backtracking algo
        print("called at {}".format(i))
        if(i == len(self.puzz) - 1):
            print("~~~~~SOLVED~~~~~")
            return True
        
        #if spot is empty
        elif(self.puzz.getItem(i) == 0):
            num = 1
            while(num < 10):
                print("loop: {} for {}".format(i,num))
                print(self.puzz.isSolved(i,num))
                if(self.puzz.isSolved(i, num)):
                    temp = self.puzz.getItem(i)
                    self.puzz.setItem(i,num)
                    solved = self.backtracker(i+1)
                    
                    #check if puzzle has been solved
                    if(solved):
                        return True
                    else:
                        self.puzz.setItem(i,temp)

                num += 1
            print("unsolved")
        else:
            solved = self.backtracker(i+1)
            if(solved):
                return True
            else:
                return False

solver = SudokuSolver()
startTime = time.time()

puzzleSolved = solver.backtracker(0)
timeSolved = time.time() - startTime
if(puzzleSolved):
    print("This puzzle was solved in {} seconds".format(timeSolved))
else:
    print("This puzzle is unsolvable")

