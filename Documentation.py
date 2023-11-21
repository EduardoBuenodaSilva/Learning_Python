if __name__ == "__main__":
    choice = 'sets'

    if choice == 'number':
        import Dnumber
        obj = Dnumber.numbers()
        print(obj.adition())
        print(obj.multiplication())
        print(obj.exponentiation())
        obj.mathematical()
        obj.random()

    elif choice == 'string':
        import Dstrings
        obj = Dstrings.string()
        obj.indexing()
        obj.repconc(3)
        obj.immutability(' 0Lets change a string ')
        
    elif choice == 'lists':
        import Dlist
        obj = Dlist.lists()
        obj.indexing()
        obj.methods()
        obj.boundcheck()
        obj.nesting()
        obj.comprehensions()

    elif choice == 'dict':
        import Ddictionaries
        obj = Ddictionaries.dictionaries()
        obj.indexing()
        obj.formats()
        obj.nesting()
        obj.methods()

    elif choice == 'iter':
        import Diter
        obj = Diter.iteration()
        obj.protocol()
        obj.nextop()
    
    elif choice == 'tuples':
        import Dtuple
        obj = Dtuple.tuple()
        obj.indexing()
        obj.slicing()

    elif choice == 'files':
        import Dfiles
        obj = Dfiles.files()
        obj.output()
        obj.inputs()
        obj.unicodeTfiles()

    elif choice == 'sets':
        import Dsets
        obj = Dsets.sets()
        obj.opertations()
        obj.membership()

