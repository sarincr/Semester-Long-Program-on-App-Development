from tkinter import *

root = Tk()

cn1 = Canvas(root, width=600, height=600) 
cn1.pack()

cn1.create_arc(10, 50, 240, 210, start=0, extent=150, fill="blue")

root.mainloop()

