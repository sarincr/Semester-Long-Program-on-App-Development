import tkinter as tk
 
 
root = tk.Tk()
 
tk.Label(root, text="Label 1").grid(row=0, column=0)
tk.Label(root, text="Label 2").grid(row=1, column=0)
 
e1 = tk.Entry(root)
e2 = tk.Entry(root)
 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
 
tk.mainloop()