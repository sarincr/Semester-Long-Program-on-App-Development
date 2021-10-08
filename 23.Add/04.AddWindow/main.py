from tkinter import *

from tkinter import messagebox

root = Tk()
root.geometry("100x100")
def hello():
   messagebox.showinfo("Say Hello", "Hello World")

bt1 = Button(root, text = "Say Hello", command = hello)
bt1.place(x = 35,y = 50)

root.mainloop()
