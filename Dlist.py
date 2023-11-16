class lists:
    a = [1,2,3,4,5,6,7,8]
    b = [1,'eduardo', 9, [1,2,3], (2,3)]
    matrix =[[0,1,2],
            [4,5,6],
            [7,8,9]]
    matrix_coluns = []

    def indexing(self):
        print(self.a[:-1])
        print(self.b + [',2',3])
        print(self.a*3)

    def methods(self):
        self.a.append('NI')
        print(self.a)
        self.a.pop(4)
        print(self.a)
        self.a.insert(4, 'hehe')
        print(self.a)
        self.a.extend([1,2,3,4,5])
        print(self.a)

    def nesting(self):
        print(self.matrix[1])
        print(self.matrix[1][2])

    def boundcheck(self):
        #pyhton does not allow us to index a non existing item
        try:
            self.a[99]
        except:
            print("we cannot index a non existing item")

    def comprehensions(self):
        for i in range(len(self.matrix[1])):
            self.matrix_coluns.append([row[i] for row in self.matrix])
            print(self.matrix_coluns[i])
        
        
