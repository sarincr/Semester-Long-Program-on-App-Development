from tkinter import *  
      
def selection():
    selection = "You selected " + str(X.get())
    label.config(text = selection)  
      
root = Tk()  
root.geometry("500x500")  

X = IntVar()  
lbl = Label(text = "Select an Option")  
lbl.pack()  


R1 = Radiobutton(root, text="Yes", variable=X, value=1, command=selection)  
R1.pack( )  

R2 = Radiobutton(root, text="No", variable=X, value=2,  command=selection)  
R2.pack( )  

R3 = Radiobutton(root, text="May be", variable=X, value=3, command=selection)  
R3.pack( )  
  
label = Label(root)  
label.pack()  
root.mainloop()  