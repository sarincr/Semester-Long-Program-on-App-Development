from tkinter import *

root = Tk()

root.geometry('750x700')


chk1 = IntVar()



chBx = Checkbutton(root,text = "Option A", variable=chk1)

chBx.pack()


root.mainloop()
