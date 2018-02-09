from stripper import Stripper

class Puzzle:

    boxSize = 3
    dimension = boxSize * boxSize

    
    def __init__(self,cont):
        self.puzzle = cont


    def checkRow(self,x,val):
        row = (x // 9) * 9
        for i in range(9):
            if (self.puzzle[row + i] == val):
                return False

        return True


    def checkColumn(self,y,val):
        while(y > 9):
            y = y - 9
        column = y
        for i in range(9):
            if(self.puzzle[column + (i * 9)] == val):
                return False

        return True


    def checkBox(self,index,val):
        y = index
        #x = 0
        while(y > 9):
            y = y - 10
        y = (y // 3) * 3
        
        x = (x // 30) * 30
       # if(index > 29 && index < 60):
        #    x = 30
        #elif(index >= 60):
         #   x = 60
        
        newIndex = x + y
        for row in range(3):
            newIndex += 10
            for column in range(3):
                if(self.puzzle[newIndex + column] == val):
                    return False

testList = Stripper.strip("realTest")
puzz = Puzzle(testList)
print(puzz.checkRow(0,2))
print(puzz.checkColumn(0,9))
