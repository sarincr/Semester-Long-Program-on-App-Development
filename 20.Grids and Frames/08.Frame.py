
from tkinter import Tk, mainloop, LEFT, TOP
from tkinter.ttk import *
  
root = Tk()
root.geometry('500x500')
 
lf = LabelFrame(root, text = 'This is Label Frame')
lf.pack(expand = 'yes', fill = 'both')


btn1 = Button(lf, text = 'Button 1')
btn1.place(x = 30, y = 10)
btn2 = Button(lf, text = 'Button 2')
btn2.place(x = 230, y = 10)
  

chkbtn1 = Checkbutton(lf, text = 'Checkbutton 1')
chkbtn1.place(x = 30, y = 150)
chkbtn2 = Checkbutton(lf, text = 'Checkbutton 2')
chkbtn2.place(x = 230, y = 150)
  
mainloop()