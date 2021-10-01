from tkinter import *
root = Tk()
root.geometry("500x500")

btn_height = Button(root, text="50px high")
btn_height.place(height=50, x=200, y=200)

btn_width = Button(root, text="60px wide")
btn_width.place(width=60, x=300, y=300)


btn_width = Button(root, text="70px wide")
btn_width.place(width=60, x=400, y=400)


btn_width = Button(root, text="80px wide")
btn_width.place(width=60, x=460, y=460)




btn_x=Button(root, text="X = 400px")
btn_x.place(x=400)

btn_y=Button(root, text="Y = 300")
btn_y.place(y=400)

root.mainloop()