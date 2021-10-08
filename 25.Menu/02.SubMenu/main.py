from tkinter import *

import tkinter

root = Tk()

MainButton =  Menubutton ( root, text = "File", relief = RAISED )

MainButton.grid()

MainButton.SubButton =  Menu ( MainButton )
MainButton["menu"]  =  MainButton.SubButton 
    
MainButton.SubButton.add_checkbutton ( label = "New File" )
MainButton.SubButton.add_checkbutton ( label = "Open" )

MainButton.pack()
root.mainloop() 

