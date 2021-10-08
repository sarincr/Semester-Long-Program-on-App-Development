from tkinter import *
from functools import partial  

def addit(label_result, n1, n2): 
    num1 = (n1.get())  
    num2 = (n2.get())  
    result = int(num1)+int(num2)  
    label_result.config(text="Result = %d" % result)  
    return  

root = Tk()  
root.geometry('500x500')  
root.title('Calculator') 

X1 = StringVar()  
X2 = StringVar()  
      
lab1 = Label(root, text="Enter first Number").grid(row=1, column=0) 
lab2 = Label(root, text="Enter second Number").grid(row=2, column=0)  
      
labelResult = Label(root)  
labelResult.grid(row=7, column=2)  
      
entr1 = Entry(root, textvariable=X1).grid(row=1, column=2)  
entr2 = Entry(root, textvariable=X2).grid(row=2, column=2)


addit = partial(addit, labelResult, X1, X2)  


buttonCal = Button(root, text="Calculate", command=addit).grid(row=3, column=0)  
root.mainloop()  