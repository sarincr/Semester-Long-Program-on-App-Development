from tkPDFViewer import tkPDFViewer 
from tkinter import*
root = Tk()

X = tkPDFViewer.ShowPdf()

Y = X.pdf_view(root,pdf_location=r"/home/angicia/Desktop/MultiSwarm.pdf")
Y.pack()
root.mainloop()
