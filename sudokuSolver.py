from stripper import Stripper
from newPuzzle import Puzzle
import time

class SudokuSolver:
    puzz = None
    #initial setup
    solution = []
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
            print("Solution: {}".format(self.solution))
            print("length: {} ".format(len(self.solution)))
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
                    #store this digit of the solution
                    self.solution.append(num)
                    solved = self.backtracker(i+1)
                    
                    #check if puzzle has been solved
                    if(solved):
                        return True
                    else:
                        self.puzz.setItem(i,temp)
                        self.solution = self.solution[:-1]
                num += 1
            print("unsolved")
        else:
            solved = self.backtracker(i+1)
            if(solved):
                return True
            else:
                return False


    def printSolvedPuzzle(self):
        i = 0
        for integer in self.puzz.puzzle:
            if(integer == 0):
                integer = self.solution[i]
                i += 1
        print("Solved Puzzle:\n")
        print(self.puzz.puzzle)

solver = SudokuSolver()
startTime = time.time()

puzzleSolved = solver.backtracker(0)
timeSolved = time.time() - startTime
if(puzzleSolved):
    print("This puzzle was solved in {} seconds".format(timeSolved))
    solver.printSolvedPuzzle()
else:
    print("This puzzle is unsolvable")

