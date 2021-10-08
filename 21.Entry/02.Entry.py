from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry('200x200')

def welcomeMessage():
    name = X.get()
    return messagebox.showinfo('message',f'Hi! {name} ')
    

Label(root, text="Enter Name").pack()
X= Entry(root)
X.pack()

Button(root, text="Click Here", command=welcomeMessage).pack()

root.mainloop()