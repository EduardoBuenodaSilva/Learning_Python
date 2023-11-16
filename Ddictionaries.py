class dictionaries:
    d0 = {'food': 'spam',
         'quantity': 4,
         'color': 'pink'}
    d1 = {}
    d1['name'] = 'bob'
    d1['job'] = 'dev'
    d1['age'] = 40

    d2 = dict(name = 'Bob', job='dev', age=40)

    d3 = dict(zip(['name', 'job', 'age'],['bob','dev',40]))

    d4 = {'name': {'first': 'Bob', 'last': 'Smith'},
          'job': ['dev', 'mgr'],
          'age': 40.5 }

    def indexing(self):
        print(self.d0['food'])
        print(self.d0['quantity'])
        print(self.d0['color'])

    def formats(self):
        print(self.d0)
        print(self.d1)
        print(self.d2)
        print(self.d3)

    #The list nested inside the dictionry is a separetly piece of memory of the dictionary
    def nesting(self):
        print(self.d4['name'])
        print(self.d4['name']['last'])
        self.d4['job'].append('jnt')
        print(self.d4)

    def methods(self):
        value = self.d0.get('x', 0)
        print(value)

        keys = list(self.d1.keys())

        for element in keys:
            print(self.d1[element], ': ', element)