from array2d import Array2d
from stripper import Stripper 

class Puzzle:

    boxSize = 3
    dimension = boxSize * boxSize


    def __init__(self,cont):
        self.matrix = Array2d(self.dimension, self.dimension)

        for x in range(len(cont)//self.dimension):
            for y in range(len(cont)//self.dimension):
                self.matrix.set(x,y,cont[y + (self.dimension * x)])

        print(self.matrix.get(0,0))
        print(self.matrix.get(0,1))
        print(self.matrix.get(0,2))
        print(self.matrix.get(0,3))
        print(self.matrix.get(0,4))
        print(self.matrix.get(0,5))        
        print("---")
        print(self.matrix.get(0,0))
        print(self.matrix.get(1,0))
        print(self.matrix.get(2,0))
        print(self.matrix.get(3,0))
        print(self.matrix.get(4,0))
        print(self.matrix.get(5,0))

    @staticmethod
    def fileToList(file):
        with open(file) as f:
            contents = f.read()
            print(contents)
            l = list(contents)
            l = l[:-1]
            intList = [int(i) for i in l]
            return intList
    
    def checkRows(self):
        numsFound = [0 for zero in range(10)]
        #print("numsFound init={}".format(numsFound))
        sum = 0
        
        #Check for dupes
        for x in range(9):
            for y in range(9):
                thisNum = self.matrix.get(x,y)
                #print("x:{}y:{}".format(x,y))
                #print("thisNum = {}".format(thisNum))
                if numsFound[thisNum] == 1:
                    #print("thisNum={}numsFound[]={}".format(thisNum,numsFound[thisNum]))
                    numsFound = [0 for zero in range(10)]
                    #print("numsFound again{}".format(numsFound))
                    return False
                else:
                    numsFound[thisNum] = 1
                    sum += thisNum
        
            numsFound = [0 for zero in range(10)]
            #Check sum, solved = 45
            if sum != 45:
                return False

        print("checkRows:")
        return True

    def checkColumns(self):
        numsFound = [0 for zero in range(10)]
        sum = 0

        #check for dupes
        for y in range(9):
            for x in range(9):
                thisNum = self.matrix.get(x,y)

                #print("x:{}y:{}".format(x,y))
                #print("thisNum:{}".format(thisNum))
                
                if numsFound[thisNum] == 1:
                    numsFound = [0 for zero in range(10)]
                    return False
                else:
                    numsFound[thisNum] = 1
                    sum += thisNum

            numsFound = [0 for zero in range(10)]
            #Check sum, solved == 45
            if sum != 45:
                return False
        print("checkColumns:")    
        return True



    def checkBoxes(self):
        numsFound = [0 for zero in range(10)]
        sum = 0
        
        #check for dupes
        offset
        for x in range(9):
            xoffset = 0
            
            #check 1 box
            for y in range(9):
                thisNum = self.matrix.get(x, y % boxSize)
        return False            

    def checkBox(self,x,y):
        numsFound = [0 for zer in range(10)]
        self.x = (x // self.boxSize) * self.boxSize
        self.y = (y // self.boxSize) * self.boxSize

        for row in range(3):
            for column in range(3):
                thisNum = self.matrix.get(self.x + row, self.y + column)
                print("thisNum= {}".format(thisNum))
                print("numsFound= {}".format(numsFound[thisNum]))
                if numsFound[thisNum] == 1:
                    numsFound = [0 for zero in range(10)]
                    return False
                else:
                    numsFound[thisNum] = 1

        print("checkBox")
        return True
#lst = [0,1,2,3,4,5,6,7,8]
#puzz = Puzzle(lst)
#testList = Puzzle.fileToList("testPuzz2")
testList = Stripper.strip("testPuzz")
print(testList)
puzz = Puzzle(testList)
print(puzz.checkRows())
print(puzz.checkColumns())
print(puzz.checkBox(0,0))
print(puzz.checkBox(3,3))
