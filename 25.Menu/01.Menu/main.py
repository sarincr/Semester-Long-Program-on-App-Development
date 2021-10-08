from tkinter import *

root = Tk()  
  
def base():  
    print("Menu is clicked")  

    
Mn = Menu(root)  

Mn.add_command(labe= "New_File", command =  base)
Mn.add_command(labe= "Open", command =  base)
Mn.add_command(label="Quit!", command=root.quit)  
  

root.config(menu=Mn)  
  
root.mainloop()  