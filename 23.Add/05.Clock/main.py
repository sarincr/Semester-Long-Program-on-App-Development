 
from tkinter import *
from tkinter.ttk import *
from time import strftime




root = Tk()

root.title('Digital Clock')




    
    
label = Label(root, font = ('times', 50, 'bold'),background = 'grey',foreground = 'white')
label.pack(anchor = 'center')



def time():
    X = strftime('%H:%M:%S %p')
    label.config(text = X)
    label.after(1000, time)

time()


mainloop()
