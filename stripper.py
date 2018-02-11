
class Stripper:

    @staticmethod
    def strip(fileName):
        with open(fileName) as f:
            cont = f.read()
    
        cont = cont.strip()
        
        #strip out newline chars
        l = [char for char in cont if '\n' not in char]
        #convert chars to ints
        l = [int(c) for c in l]
        #print(l)
        return l
