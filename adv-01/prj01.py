from tkinter import *

win = Tk()
win.title("My first GUI")


def hi_fun():
    display.config(text="HI", fg="red", bg="black")


btn = Button(win, text="1", command=hi_fun, fg="black", bg="#FFFFFF")
btn.pack()

display = Label(win, text="hi", fg="#FFFFFF", bg="#00E2C6")
display.pack()

win.mainloop()
