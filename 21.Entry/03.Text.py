 
from tkinter import Tk, Text

root = Tk()
root.resizable(False, False)
root.title("Hello Text")

text = Text(root, height=8)
text.pack()


root.mainloop()