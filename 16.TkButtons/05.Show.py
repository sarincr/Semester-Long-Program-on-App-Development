from tkinter import *

frame_name= Tk()
def ClickHere():
    print("Hello Tkinter")
    lab.pack()

lab =  Label(frame_name, text = "Terms and Conidtions", font=("courier, 10"))
bt1 = Button(frame_name ,  text = "Ok",command=ClickHere)
bt2 = Button(frame_name ,  text = "Close",command=quit) 
bt1.pack()
bt2.pack()
frame_name.mainloop()
