class iteration:
    dlist = list(range(0,100, 2))
    dtuple = tuple(range(0,50, 3))
    dstring = 'spam'
    dnumber = 10

    def protocol(self):
        lllocal = [self.dlist, self.dtuple, self.dstring, self.dnumber]

        for types in lllocal:
            obj = str(type(types)).replace('<class ', '').replace('>', '')
            try:
                iter(obj)
                for item in types:
                    print(item)
                print('This is a interable object:', obj)
            except:
                print("This is not a interable object", obj)

    def nextop(self):
        generator = (x**2 for x in self.dlist)

        try:
            init = 0
            while(True):
                print(next(generator), self.dlist[init])
                init += 1
        except StopIteration:
            print('We are done')
            