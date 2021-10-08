from tkinter import*
root = Tk()
root.geometry('500x500')
root.title("Registration Form")

def Base():
    print("Completed")

lbl0 = Label(root, text="Registration form",width=20,font=("bold", 20))
lbl0.place(x=90,y=53)


lbl1 = Label(root, text="FullName",width=20,)
lbl1.place(x=80,y=130)

entr1 = Entry(root)
entr1.place(x=240,y=130)

lbl2 = Label(root, text="Email",width=20,)
lbl2.place(x=68,y=180)

entr2 = Entry(root)
entr2.place(x=240,y=180)

lbl3 = Label(root, text="Gender",width=20,)
lbl3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male", variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",variable=var, value=2).place(x=290,y=230)

lbl4 = Label(root, text="Age:",width=20,)
lbl4.place(x=70,y=280)


entr2 = Entry(root)
entr2.place(x=240,y=280)

Button(root, text='Submit',width=20,bg='brown',fg='white', command=Base).place(x=180,y=380)
 
root.mainloop()
