from tkinter import *

root = Tk()

cn1 = Canvas(root, width=600, height=600) 
cn1.pack()

cn1.create_line(0, 80, 80,0, fill="red")

cn1.create_line(0, 0, 80,80, fill="red")

root.mainloop()

