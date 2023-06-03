from ttkbootstrap import *
import sys
import os

os.chdir(sys.path[0])


def test():
    print("test")


front_size = 20
window = tk.Tk()
window.title("My GUI")
window.option_add("*font", ("Helvetica", front_size))

style = Style(theme="flatly")
style.configure('my.TButton', font=("Helvetica", front_size))

lable = Label(window, text="選擇檔案:")
lable.grid(row=0, column=0, sticky="E")

lable = Label(window, text="無")
lable.grid(row=0, column=1, sticky="E")

button = Button(window, text="瀏覽", command=test, style="my.TButton")
button.grid(row=0, column=2, sticky="W")

button = Button(window, text="顯示", command=test, style="my.TButton")
button.grid(row=1, column=0, columnspan=3, sticky="EW")

canvas = Canvas(window, width=600, height=600, bg="white")
canvas.grid(row=2, column=0, columnspan=3, sticky="EW")

window.mainloop()