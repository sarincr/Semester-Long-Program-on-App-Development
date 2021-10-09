import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Visual TK")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_267=tk.Button(root)
        GButton_267["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_267["font"] = ft
        GButton_267["fg"] = "#000000"
        GButton_267["justify"] = "center"
        GButton_267["text"] = "Button"
        GButton_267.place(x=220,y=200,width=100,height=62)
        GButton_267["command"] = self.GButton_267_command

        GLabel_614=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_614["font"] = ft
        GLabel_614["fg"] = "#333333"
        GLabel_614["justify"] = "center"
        GLabel_614["text"] = "label"
        GLabel_614.place(x=230,y=140,width=70,height=25)

    def GButton_267_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
