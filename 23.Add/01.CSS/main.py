from tkinter_expansion import GuiStyle as Tks
import tkinter as tk

root = tk.Tk()
root.configure(width=700, height=700)

style = Tks.StyleManager(css_file="style.css") # initializing StyleManager
json_data = style.load_css() # load css data
style.css_to_theme("css") # convert css to theme

window = tk.Button(root, bg=json_data["window"]["color"],
                   activebackground=json_data["window"]["activebackground"],
                   highlightbackground=json_data["window"]["bordercolor"],
                   highlightthickness=json_data["window"]["bordercolorwidth"])
window.place(x=0, y=0, relwidth=0.5, relheight=1)

label = tk.Label(root, bg=json_data["label"]["background"])
label.place(relx=0.5, y=0, relwidth=0.5, relheight=1)
root.mainloop()
