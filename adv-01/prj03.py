import tkinter.messagebox
from tkinter import *

win = Tk()


def hi_fun():
    while True:
        tkinter.messagebox.showerror('Windows 错误', '你的电脑正在被攻击！')


btn = Button(win, text="領取獎金", command=hi_fun, fg="black", bg="#FFFFFF")
btn.pack()

win.mainloop()