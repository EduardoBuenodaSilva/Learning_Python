#Tuples are sequences, like lists, but they are immutable like strings 
#they are used to represent fixed collection of items.
class tuple:
    t1 = (1,2,3,4,5)

    def indexing(self):
        t2 = self.t1 + (6,7)
        print('t2:', t2, 'len(t2):', len(t2), 't2[2]=', t2[2])

    def slicing(self):
        try:
            self.t1[0] = 2
        except:
            print("tuples are immutable objects, so we cannot change once defined in-place")
            print("Tuples don't grow and shirink")
