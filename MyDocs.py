import tkinter as tk
from tkinter import ttk

class docs:
    win = tk.Tk()
    win.title("Python documentation")  

    def tab(self, name):
        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text = name)
        tabControl.pack(expand =1, fill ='both')
        return tab1
    
    def addlabel(self, tab, x, y, text):
        ttk.Label(tab, text = text).grid(column = x, row = y)

    def __init__(self):
        tab = self.tab(name = 'Numbers')
        self.addlabel(tab = tab, x=0, y=0, text = 'A * B + C * D')
        self.addlabel(tab = tab, x=0, y=1, text = '(X + Y) * Z')





if __name__ == '__main__':
    obj = docs()
