from tkinter import *

root = Tk()
for r in range(3):
   for c in range(4):
      Label(root, text='R%s/C%s'%(r,c)).grid(row=r,column=c)
root.mainloop(  )


root.mainloop()
