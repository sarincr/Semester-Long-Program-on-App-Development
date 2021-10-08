from ttkbootstrap import Style, ttk

style = Style()
style.theme_use('flatly')
root = style.master

# create widget with primary colors
ttk.Label(root, text='Hello world').pack()

# create widget with other colors
ttk.Label(root, text='Hello world', style='danger.TLabel').pack()
ttk.Label(root, text='Hello World', style='info.TLabel').pack()
ttk.Button(root, text='Hello World', style='info.TButton').pack()
ttk.Button(root, text='Hello World', style='warning.Outline.TButton').pack()
ttk.Radiobutton(root, text='Hello World', style='danger.TRadiobutton').pack()

# run the window
root.mainloop()
