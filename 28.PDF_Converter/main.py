import tkinter as tk
from docx2pdf import convert
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfile


root = tk.Tk()
root.title("word to PDF converter")

def openfile():
    file = askopenfile(filetypes = [('Word Files', '*.docx')])
    convert(file.name,'/convert.pdf')
    showinfo("Done","File Succesfully Converted")

label = tk.Label(root, text= "Choose File:- ")
label.grid(row=0, column=0)

button = ttk.Button(root, text="Select", width=30, command=openfile)
button.grid(row=0, column=1)

root.mainloop()