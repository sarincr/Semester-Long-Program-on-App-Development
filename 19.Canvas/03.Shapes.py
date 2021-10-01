from tkinter import *

root = Tk()

cn1 = Canvas(root, width=600, height=600) 
cn1.pack()



cn1.create_rectangle(50, 20, 150, 80, fill="#476042")

cn1.create_oval(50,50,100,100)

cn1.create_polygon(0,0,100,50, 0, 50, outline="red",   fill='blue', width=10)




root.mainloop()

