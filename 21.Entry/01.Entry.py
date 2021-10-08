from tkinter import * 

root= Tk()
name = StringVar(root, value='not available')
nameTf = Entry(root, textvariable=name).pack()

root.mainloop()