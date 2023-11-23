import tkinter as tk
from tkinter import ttk
from tkinter import Menu
import text

class docs:
    win = tk.Tk()
    win.title("Python documentation")
    tabControl = ttk.Notebook(win)

    def addtab(self, name, tabControl):
        tab1 = ttk.Frame(tabControl)
        self.tabControl.add(tab1, text = name)
        self.tabControl.pack(expand =0, fill ='both')
        return tab1
    
    def addlabel(self, tab, x, y, text, just ='ew', bg = 'white', rp = 1):
        label = ttk.Label(tab, text = text)
        label.grid(column = x, row = y, sticky = just, rowspan = rp)
        label.configure(background = bg)

    def addFrame(self, window, text, x, y, bg='white', rp = 1):
        style = ttk.Style()
        style.configure('My.TFrame', foreground = bg, background = bg)
        bFrame = ttk.LabelFrame(window, text = text, style = 'My.TFrame')
        bFrame.grid(column = x, row =y, columnspan = rp, sticky = 'ew', padx = 2.5, pady = 2.5)
        return bFrame

    def scrollbar(self, win, x, y, just = 'ns', rp =2):
        scroll = ttk.Scrollbar(win)
        scroll.grid(row = x, column = y, sticky = just, rowspan = rp)

    def text(self, win, x, y, text):
        text = tk.Text(win, height = 25)
        text.grid(column =  y, row = x)
        text.insert(text = text)

    def __init__(self):
        tab = self.addtab(tabControl = self.tabControl, name = 'Numbers')
        tab2 = self.addtab(tabControl = self.tabControl, name = 'Tuples')

        bframex = self.addFrame(tab, text = 'Notes', x = 0, y=1, rp = 3)
        self.addlabel(tab=bframex, text = text.explanation, x=1, y=1, rp=2)
        
        bframe1 = self.addFrame(tab, text='Literals', x=0,y=2)
        bframe2 = self.addFrame(tab, text= 'Interpretations', x=1,y=2)  
        bframe3 = self.addFrame(tab, text='Operators', x=0,y=3)
        bframe4 = self.addFrame(tab, text= 'Description', x=1,y=3)

        for row in range(len(text.texts)):
            number = text.texts[row][0]
            num = text.texts[row][1]
            self.addlabel(tab = bframe1, x=0, y=row, text = number)
            self.addlabel(tab = bframe2, x=0, y=row, text = num)

        for row in range(len(text.table)):
            number = text.table[row][0]
            num = text.table[row][1]
            self.addlabel(tab = bframe3, x=0, y=row, text = number)
            self.addlabel(tab = bframe4, x=0, y=row, text = num)
        

        

        self.win.mainloop()


if __name__ == '__main__':
    obj = docs()
    
