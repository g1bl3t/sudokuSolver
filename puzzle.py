from array2d import Array2d


class Puzzle:

    boxSize = 9

    def __init__(self,cont):
        self.matrix = Array2d(self.boxSize, self.boxSize)

        for x in range(len(cont)//self.boxSize):
            for y in range(len(cont)//self.boxSize):
                self.matrix.set(x,y,cont[y + (self.boxSize * x)])

        print(self.matrix.get(0,0))
        print(self.matrix.get(0,1))
        
        print(self.matrix.get(1,0))
        print(self.matrix.get(1,1))
        print(self.matrix.get(1,2))
        print(self.matrix.get(2,0))
        print(self.matrix.get(2,1))
        print(self.matrix.get(2,2))

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
            if sum == 45:
                return True
            else:
                return False

    def checkColumns(self):
        numsFound = [0 for zero in range(10)]
        sum = 0

        #check for dupes
        for y in range(9):
            for x in range(9):
                thisNum = self.matrix.get(x,y)

                if numsFound[thisNum] == 1:
                    numsFound = [0 for zero in range(10)]
                    return False
                else:
                    numsFound[thisNum] = 1
                    sum += thisNum

                numsFound = [0 for zero in range(10)]
                #Check sum, solved == 45
                if sum == 45:
                    return True
                else:
                    return False

#lst = [0,1,2,3,4,5,6,7,8]
#puzz = Puzzle(lst)
testList = Puzzle.fileToList("testPuzz")
print(testList)
puzz = Puzzle(testList)
print(puzz.checkRows())
print(puzz.checkColumns())
