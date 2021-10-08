from tkPDFViewer import tkPDFViewer 
from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfile


root = Tk()

X = tkPDFViewer.ShowPdf()

Y = X.pdf_view(root,pdf_location=askopenfile(filetypes = [('PDF Files', '*.pdf')]))
Y.pack()
root.mainloop()
