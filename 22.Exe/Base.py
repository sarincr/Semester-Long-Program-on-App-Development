from tkinter import *
from tkinter import ttk
root = Tk()

frm1 = Frame(master=root, width=200, height=100, bg="red")
frm1.pack(fill=BOTH, side=LEFT, expand=True)

bt1 = Button(frm1,text="Click Me")
bt1.pack()


bt2 = Button(frm1,text="Click Me")
bt2.pack()


frm2 = Frame(master=root, width=100, bg="yellow")
frm2.pack(fill=BOTH, side=LEFT, expand=True)

frm3 = Frame(master=root, width=50, bg="blue")
frm3.pack(fill=BOTH, side=LEFT, expand=True)



bt3 = Button(frm3,text="Click Me")
bt3.pack()

root.mainloop()

