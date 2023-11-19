class numbers:
    n1 = 123
    n2 = 222
    nf1 = 1.5

    def adition(self):
        return (self.n1 + self.n2, self.nf1 + self.n1)
    
    def multiplication(self):
        return self.nf1 * 4

    def exponentiation(self):
        return self.n2**self.n1

    def mathematical(self):
        import math as m
        print('This method import math modules')
        print(m.pi)

    def random(self):
        import random as ra
        print('This method imports random module')
        print(ra.random())
        print(ra.choice(list(range(1,1000))))
        
