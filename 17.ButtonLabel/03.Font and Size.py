from tkinter import *

root = Tk()

l1 = Label(root,text = "Hello World" , fg='red' , bg='green', font=("Courier", 44))
l1.pack()
l2 = Label(root,text = "Hello World" , fg='red' , bg='green', font=("Courier", 88))
l2.pack()

root.geometry('750x700')
root.mainloop()
