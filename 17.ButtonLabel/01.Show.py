from tkinter import *

frame_name= Tk()
def ClickHere():
    print("Hello World")

lab =  Label(frame_name, text = "Old Label text", font=("courier, 10"))
bt1 = Button(frame_name ,  text = "Ok",command=ClickHere)
bt2 = Button(frame_name ,  text = "Close",command=quit)
lab.pack()
bt1.pack()
bt2.pack()
frame_name.mainloop()
