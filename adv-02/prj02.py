from tkinter import *
import sys
import os


def exit_fun():
    win.destroy()


os.chdir(sys.path[0])

win = Tk()
win.title("My first GUI")
quit_btn = Button(win, command=exit_fun)
quit_btn.pack()
canvas = Canvas(win, width=400, height=600, bg="white")
canvas.pack()

win.iconbitmap("2586511.ico")
# 載入圖片
img = PhotoImage(file="2586511.png")
# 在畫布上顯示圖片
my_img = canvas.create_image(200, 300, image=img)
rec = canvas.create_rectangle(100, 100, 300, 300, fill="red")
msg = canvas.create_text(200, 200, text="中指", fill="black", font=('Arial', 30))


def move_canvas(event):
    key = event.keysym
    if key == "Right":
        canvas.move(rec, 10, 0)
    elif key == "Left":
        canvas.move(rec, -10, 0)
    elif key == "Up":
        canvas.move(rec, 0, -10)
    elif key == "Down":
        canvas.move(rec, 0, 10)


canvas.bind_all('<Key>', move_canvas)

win.mainloop()
