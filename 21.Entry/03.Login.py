from tkinter import *

root=Tk()


root.geometry("500x500")


X_name=StringVar()
X_password=StringVar()



def submit():
	name=X_name.get()
	password=X_password.get()
	
	print("The name is : " + name)
	print("The password is : " + password)
	
	X_name.set("")
	X_password.set("")
	

    
lab1 = Label(root, text = 'Username', font=('calibre',10, 'bold'))
 
entr = Entry(root,textvariable = X_name, font=('calibre',10,'normal'))

 
lab2 = Label(root, text = 'Password', font = ('calibre',10,'bold'))

 
entr2=Entry(root, textvariable = X_password, font = ('calibre',10,'normal'), show = '*')
 
sub_btn=Button(root,text = 'Submit', command = submit)
 
lab1.grid(row=0,column=0)
entr.grid(row=0,column=1)
lab2.grid(row=1,column=0)
entr2.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
 
root.mainloop()
