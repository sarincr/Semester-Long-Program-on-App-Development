from tkinter import *

frame_name= Tk()

lab =  Label(frame_name, text = "Hello World", font=("courier, 50"))
bt = Button(frame_name ,  text = "Click") 
bt.pack()
lab.pack()
frame_name.mainloop()
