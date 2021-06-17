from tkinter import *

frame_name= Tk()
def ClickHere():
    print("Hello Tkinter")

lab =  Label(frame_name, text = "Hello World", font=("courier, 50"))
bt = Button(frame_name ,  text = "Click",command=ClickHere) 
bt.pack()
lab.pack()
frame_name.mainloop()
