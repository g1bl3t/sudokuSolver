from array2d import Array2d


class Puzzle:

    boxSize = 3

    def __init__(self,cont):
        self.matrix = Array2d(len(cont)//2, len(cont)//2)

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
lst = [0,1,2,3,4,5,6,7,8]
puzz = Puzzle(lst)
