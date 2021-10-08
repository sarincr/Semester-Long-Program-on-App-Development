 
import tkinter as tk

def increase():
    value = int(X["text"])
    X["text"] = f"{value + 1}"


def decrease():
    value = int(X["text"])
    X["text"] = f"{value - 1}"

root = tk.Tk()

root.rowconfigure(0, minsize=50, weight=1)
root.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease = tk.Button(master=root, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

X = tk.Label(master=root, text="0")
X.grid(row=0, column=1)

btn_increase = tk.Button(master=root, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")


root.mainloop()