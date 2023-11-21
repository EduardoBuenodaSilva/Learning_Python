#Sets are neither mappings not sequences; they are unordered 
#Collections of unique an immutable objects.

class sets:
    X = set('spam')
    Y = {'h','a','m'}

    def opertations(self):
        print('Intersection:')
        print('X&Y:', self.X&self.Y)
        print('Union:')
        print('X|Y:', self.X|self.Y)
        print('Difference')
        print('X-Y', self.X-self.Y)
        print('superset')
        print('X>Y',self.X>self.Y)
        x = {n**2 for n in [1,2,3,4,5]}
        print(x)
        print(x)
    
    def membership(self):
        print("'p' in self.X")
        print('p' in self.X)