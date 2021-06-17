from tkinter import *

frame_name= Tk()

lab =  Label(frame_name, text = "Hello World", font=("courier, 50"))
bt = Button(frame_name ,  text = "Click",bg ="red", fg = "black",activebackground="blue" , activeforeground= "yellow",highlightcolor="black") 
bt.pack()
lab.pack()
frame_name.mainloop()
