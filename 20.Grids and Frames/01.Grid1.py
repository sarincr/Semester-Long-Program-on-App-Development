from tkinter import *
root = Tk()
btn_column = Button(root, text="I'm in column 3")
btn_column.grid(column=3)

btn_columnspan = Button(root, text="I have a columnspan of 3")
btn_columnspan.grid(columnspan=3)


btn_sticky = Button(root, text="I'm stuck to north-east corner of frame")
btn_sticky.grid(sticky=NE)

root.mainloop()