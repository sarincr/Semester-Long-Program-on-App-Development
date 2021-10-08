 
from ttkbootstrap import Style
from tkinter import ttk

style = Style()

window = style.master
ttk.Button(window, text="Submit", style='success.TButton').pack(side='left', padx=5, pady=10)
ttk.Button(window, text="Submit", style='success.Outline.TButton').pack(side='left', padx=5, pady=10)
ttk.Button(window, text="Submit", style='warning.TButton').pack(side='left', padx=5, pady=10)
ttk.Button(window, text="Submit", style='danger.TButton').pack(side='left', padx=5, pady=10)
window.mainloop()
