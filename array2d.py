class Array2d:
    
    #constructor
    def __init__(self, height, width):
        self.rows = [None] * width
        i = 0 
        while i < len(self.rows):
            self.column = [None] * height
            self.rows[i] = self.column
            i += 1

    def get(self, x, y):
        return self.rows[x][y]

    def set(self, x, y, val):
        self.rows[x][y] = val

#myArray = Array2d(3,3)
#print(myArray.rows)

#myArray.set(1,1,3)
#print(myArray.get(1,1))
