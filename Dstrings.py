class string:
    s0 = 'spam'
    s1 = 'Eduardo'

    def indexing(self):
        print(self.s1[1:3])
        print(self.s1[-1], self.s1[len(self.s1)-1])
        print(self.s1[:-1])
        a = self.s0[:]
        b = self.s0[:]
        print(id(a), id(b))
        for i in range(len(self.s0)-1, 0, -1):
            print(self.s0[:i],self.s0[i],self.s0[i:])

    def repconc(self,k):
        print(self.s0+" "+self.s1)
        print(self.s0*k)

    def immutability(self, thing):
    # Every string operation is defined to produce a new string as a result,
    # because strings are immutable in Python, they cannot be changed in place
    # after they are created.

        try:
            print(self.s0[2])
            self.s0[2] = thing
        except:
            print("Strings are immutable objects they cannot be changed in place")
            self.s0 = self.s0[:1] + thing + self.s0[2:]
            print(self.s0)
