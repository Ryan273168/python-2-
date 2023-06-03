from tkinter import *
import sys
import os

# 設定工作目錄
os.chdir(sys.path[0])


# 定義移動物件的函式，接受一個事件、物件、水平位移和垂直位移
# event: 事件物件為canvas.bind_all要求傳入的參數
def move_object(event, object, dx, dy):
    canvas.move(object, dx, dy)


# 定義關閉程式的函式
def exit_fun():
    windows.destroy()


# 建立一個 GUI 視窗
windows = Tk()
windows.title("My first GUI")

# 設定視窗圖示
windows.iconbitmap("2586511.ico")

# 建立一個畫布
canvas = Canvas(windows, width=400, height=450)
canvas.pack()

# 載入圖片並顯示在畫布上
img = PhotoImage(file="2586511.png")
my_img = canvas.create_image(200, 300, image=img)

# 在畫布上建立圓形、矩形和文字
rec = canvas.create_rectangle(100, 100, 300, 300, fill="red")
msg = canvas.create_text(200, 200, text="中指", fill="black", font=('Arial', 30))

# 將按鍵事件綁定到畫布上，當按下指定的按鍵時，移動對應的物件
canvas.bind_all('<Right>', lambda event: move_object(event, msg, 10, 0))
canvas.bind_all('<Left>', lambda event: move_object(event, msg, -10, 0))
canvas.bind_all('<Up>', lambda event: move_object(event, msg, 0, -10))
canvas.bind_all('<Down>', lambda event: move_object(event, msg, 0, 10))
canvas.bind_all('<d>', lambda event: move_object(event, rec, 10, 0))
canvas.bind_all('<a>', lambda event: move_object(event, rec, -10, 0))
canvas.bind_all('<w>', lambda event: move_object(event, rec, 0, -10))
canvas.bind_all('<s>', lambda event: move_object(event, rec, 0, 10))

# 建立一個按鈕，用來關閉程式
quit_btn = Button(windows, text="Quit", command=exit_fun)
quit_btn.pack()

# 開始執行 GUI 程式
windows.mainloop()