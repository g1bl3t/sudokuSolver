from stripper import Stripper

class Puzzle:

    boxSize = 3
    dimension = boxSize * boxSize
    puzzle = None
    
    def __init__(self,cont):
        self.puzzle = cont

    def getItem(self,i):
        return self.puzzle[i]
    
    def setItem(self,i,val):
        self.puzzle[i] = val

    def __len__(self):
        return len(self.puzzle)
    
    def checkRow(self,x,val):
        row = (x // 9) * 9
        for i in range(9):
            if (self.puzzle[row + i] == val):
                return False

        return True


    def checkColumn(self,y,val):
        while(y > 8):
            y = y - 9
        column = y
        for i in range(9):
            if(self.puzzle[column + (i * 9)] == val):
                return False

        return True


    def checkBox(self,index,val):
        y = index
        #x = 0
        while(y > 8):
            y = y - 9
        y = (y // 3) * 3
        
        x = (index // 27) * 27
       # if(index > 29 && index < 60):
        #    x = 30
        #elif(index >= 60):
         #   x = 60
        
        newIndex = x + y
        for row in range(3):
            for column in range(3):
                if(self.puzzle[newIndex + column] == val):
                    return False
            newIndex += 9  
        return True


    def isSolved(self,i,val):
        if(self.checkRow(i,val) and self.checkColumn(i,val) and self.checkBox(i,val)):
            return True
        else:
            return False

#testList = Stripper.strip("puzzle1")
#puzz = Puzzle(testList)
#print(puzz.checkRow(0,1))
#print(puzz.checkColumn(0,1))
#print (puzz.checkBox(0,1))
#print(puzz.isSolved(0,1))
