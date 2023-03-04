from tkinter import *
import random as r


def hi_fun():
    display.config(text="Hi Singular", fg=color[r.randint(0, len(color) - 1)])


color = [
    "black", "red", "green", "blue", "yellow", "orange", "purple", "pink",
    "brown", "gray"
]
windows = Tk()
windows.title("My first GUI")

btn = Button(windows, text="1", command=hi_fun, fg="black", bg="#FFFFFF")
btn.pack()

display = Label(windows, text="")
display.pack()
windows.mainloop()
