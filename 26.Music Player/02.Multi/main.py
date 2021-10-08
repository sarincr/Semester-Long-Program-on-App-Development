import multiprocessing
from playsound import playsound

from tkinter import*

root = Tk()
root.title('Music Player') 
root.geometry("500x500")

p = multiprocessing.Process(target=playsound, args=("NationalAnthem.mp3",))

def play():
    p.start()

def stop():
    p.terminate()
    
Button1 = Button(root, text="Play",command=play)
Button1.pack()

Button2 = Button(root, text="Stop",command=stop)
Button2.pack()

root.mainloop()
