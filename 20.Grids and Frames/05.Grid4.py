from tkinter import *


root= Tk()
root.title("grid() method")
root.geometry("350x275")


button0= Button(root, text="button0")
button0.grid(row=0,column=0)

button1= Button(root, text="button10")
button1.grid(row=1,column=0)

buttonx= Button(root, text="button11")
buttonx.grid(row=1,column=1)

buttony= Button(root, text="button13")
buttony.grid(row=1,column=3)

button2= Button(root, text="button21")
button2.grid(row=2,column=2)

button3=Button(root, text="button33")
button3.grid(row=3,column=3)

button4=Button(root, text="button44")
button4.grid(row=4,column=4)

button5=Button(root, text="button55")
button5.grid(row=5,column=5)


button5=Button(root, text="button5")
button5.grid(row=6,column=5)

root.mainloop()