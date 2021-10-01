from tkinter import *


root= Tk()
root.title("grid() method")
root.geometry("350x275")

button1= Button(root, text="button1")
button1.grid(row=1,column=0)

button2= Button(root, text="button2")
button2.grid(row=2,column=2)

button3=Button(root, text="button3")
button3.grid(row=3,column=3)

button4=Button(root, text="button4")
button4.grid(row=4,column=4)

button5=Button(root, text="button5")
button5.grid(row=5,column=5)


button5=Button(root, text="button5")
button5.grid(row=6
             ,column=5)

root.mainloop()