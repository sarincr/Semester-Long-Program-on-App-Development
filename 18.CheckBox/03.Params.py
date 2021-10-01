from tkinter import *
import tkinter.messagebox as messagebox

root = Tk()

root.geometry('750x700')


chk1 = IntVar()

chk2 = IntVar()

chk3 = IntVar()



chBx1 = Checkbutton(root,text = "Option A", variable=chk1, onvalue = 1, offvalue = 0 )
chBx2 = Checkbutton(root,text = "Option B", variable=chk2, onvalue = 1, offvalue = 0 )
chBx3 = Checkbutton(root,text = "Option C", variable=chk3, onvalue = 1, offvalue = 0 )

chBx1.pack()
chBx2.pack()
chBx3.pack()

root.mainloop()
