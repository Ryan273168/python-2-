from ttkbootstrap import *
import sys
import os
from function import function as fun

os.chdir(sys.path[0])


def get_video_info_gui():
    _, _, _, _, res = fun.get_video_info(entry.get())

    res_option['menu'].delete(0, 'end')
    for r in res:
        res_option['menu'].add_command(label=r, command=tk._setit(res_var, r))
    res_var.set(res[0])


def download_video_gui():
    if fun.dwonload_video(entry.get(), res_var.get(), show_progress):
        label3.config(text="下載完成")
    else:
        label3.config(text="解析錯誤")


def show_progress(stream, chunk, bytes_remaining):
    percent = (100 * (stream.filesize - bytes_remaining)) / stream.filesize
    percent_label.config(text=f"{percent:.2f}%")
    progress['value'] = percent
    window.update()


front_size = 20
window = tk.Tk()
window.title("My GUI")
window.option_add("*font", ("Helvetica", front_size))

style = Style(theme="flatly")
style.configure('my.TButton', font=("Helvetica", front_size))

label1 = Label(window, text="請輸入YouTube影片網址:")
label1.grid(row=0, column=0)

lable2 = Label(window, text="請選擇影片解析度")
lable2.grid(row=1, column=0)

label3 = Label(window, text="下載完成")
label3.grid(row=2, column=0)

entry = Entry(window, width=20)
entry.grid(row=0, column=1, padx=10, pady=10)

button = Button(window,
                text="搜尋影片資訊",
                command=get_video_info_gui,
                style="my.TButton")
button.grid(row=0, column=2)

button = Button(window,
                text="下載影片",
                command=download_video_gui,
                style="my.TButton")
button.grid(row=1, column=2)

progress = Progressbar(window,
                       orient=HORIZONTAL,
                       length=200,
                       mode='determinate')
progress.grid(row=2, column=1, padx=10, pady=10)

percent_label = Label(window, text="")
percent_label.grid(row=2, column=2, padx=10, pady=10)

res_var = tk.StringVar()
res_option = OptionMenu(window, res_var, ())
res_option.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()
