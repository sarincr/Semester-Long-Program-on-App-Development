from tkinter import *

from tkinter.ttk import *

def CommonFunct():
   filewin = Toplevel(root)
   button = Button(filewin, text="Add your commands")
   button.pack()
   
root = Tk()
menubar = Menu(root)
MainMenu = Menu(menubar, tearoff=0)
MainMenu.add_command(label="New", command=CommonFunct)
MainMenu.add_command(label="Open", command=CommonFunct)
MainMenu.add_command(label="Save", command=CommonFunct)
MainMenu.add_command(label="Save as...", command=CommonFunct)
MainMenu.add_command(label="Close", command=CommonFunct)

MainMenu.add_separator()

MainMenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=MainMenu)
EditMenu = Menu(menubar, tearoff=0)
EditMenu.add_command(label="Undo", command=CommonFunct)

EditMenu.add_separator()

EditMenu.add_command(label="Cut", command=CommonFunct)
EditMenu.add_command(label="Copy", command=CommonFunct)
EditMenu.add_command(label="Paste", command=CommonFunct)
EditMenu.add_command(label="Delete", command=CommonFunct)
EditMenu.add_command(label="Select All", command=CommonFunct)
menubar.add_cascade(label="Edit", menu=EditMenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=CommonFunct)
helpmenu.add_command(label="About...", command=CommonFunct)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()

