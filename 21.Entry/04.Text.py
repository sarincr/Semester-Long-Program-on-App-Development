from tkinter import *

root = Tk()
root.geometry("500x500")
root.title(" In and Out ")

def Take_input():
	INPUT = inputtxt.get("1.0", "end-1c")
	print(INPUT)
	if(INPUT == "500"):
		Output.insert(END, 'Right')
	else:
		Output.insert(END, "Wrong")
	
l1 = Label(text = "What is 100*5 ? ")
inputtxt = Text(root)

Output = Text(root)

Display = Button(root,command = lambda:Take_input())

l1.pack()
inputtxt.pack()
Display.pack()
Output.pack()

mainloop()
