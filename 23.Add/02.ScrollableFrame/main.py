 
from tkinter import *
from ScrollableFrame import *

root = Tk()

sf = ScrollableFrame(root, orient = 2 , height=180, width=360) # :-)
Label(sf.frame, text=("Hello World")).pack()
sf.pack()
root.mainloop()