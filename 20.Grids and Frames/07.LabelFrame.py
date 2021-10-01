from tkinter import Tk, mainloop, LEFT, TOP
from tkinter.ttk import *

root = Tk()
root.geometry('500x500')
  

lf = LabelFrame(root, text = 'Custom label frame')
lf.pack(expand = 'yes', fill = 'both')
  
label1 = Label(lf, text = '1. This is a Label.')
label1.place(x = 0, y = 5)

lf1 = LabelFrame(root, text = 'Custom label frame')
lf1.pack(expand = 'yes', fill = 'both')
  
label1 = Label(lf1, text = '1. This is a Label.')
label1.place(x = 20, y = 5)

mainloop()