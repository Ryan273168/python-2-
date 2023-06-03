from ttkbootstrap import *
import sys
import os
from tkinter import filedialog
from PIL import ImageTk

os.chdir(sys.path[0])

front_size = 20
window = tk.Tk()
window.title("My GUI")
window.option_add("*font", ("Helvetica", front_size))

style = Style(theme="flatly")
style.configure('my.TButton', font=("Helvetica", front_size))

check_type = BooleanVar()
check_type.set(True)

check_label = Label(window, text="True")
check_label.grid(row=1, column=2)


def on_switch_change():
    check_label.config(text=str(check_type.get()))


check = Checkbutton(window,
                    variable=check_type,
                    onvalue=True,
                    offvalue=False,
                    command=on_switch_change)
check.grid(row=1, column=1)

window.mainloop()