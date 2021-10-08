# importing required module
from playsound import playsound
from tkinter import*

root = Tk()
root.title('Music Player') 
root.geometry("500x500")

# making function
def play():
	playsound('NationalAnthem.mp3')


Button = Button(root, text="Play",command=play)
Button.pack()

root.mainloop()
