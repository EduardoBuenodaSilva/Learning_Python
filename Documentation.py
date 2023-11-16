if __name__ == "__main__":
    choice = 'dict'

    if choice == 'string':
        import Dstrings
        obj = Dstrings.string()
        obj.indexing()
        obj.repconc(3)
        obj.immutability(' Lets change a string ')
        
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

