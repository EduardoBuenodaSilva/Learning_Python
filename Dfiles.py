class findprimes:
    limit = 20
    primes = []
    multiple = []

    def prime(self, start = 2, limit= 100):
        numbers = list(range(2,limit))
        self.multiple = numbers.copy()

        for tester in numbers:
            index = numbers.index(tester)
            for element in numbers[index:]:
                if element%tester == 0 and element != tester:
                    numbers.remove(element)

        self.primes = numbers.copy()        
        for element in numbers:
            self.multiple.remove(element)

        if start > 2:
            i = 0
            while self.multiple[i] < start or self.primes[i] < start:
                self.multiple.remove(self.multiple[i])
                self.primes.remove(self.primes[i])
            i+=1

class files:
    obj = findprimes()
    obj.prime(limit = 1000)
    pnumbers = obj.primes
    file = open('output.txt', 'w')

    def output(self):
        self.file.write("-----------------Number primes-----------------\n")
        self.file.write("--------------Begin: 0, end = 1000 ------------\n\n")
        i = 0
        while i <= len(self.pnumbers):
            self.file.write(str(self.pnumbers[i:i+9]) + '\n')
            i += 10

        self.file.close()

    def inputs(self):
        for line in open('output.txt'): print(line)

