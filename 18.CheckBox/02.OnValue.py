from tkinter import *

root = Tk()

root.geometry('750x700')


chk1 = IntVar()



chBx = Checkbutton(root,text = "Option A", variable=chk1, onvalue = 1, offvalue = 0 )

chBx.pack()


root.mainloop()
