import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ttkbootstrap import *
import os
import sys

os.chdir(sys.path[0])


def on_closing():
    window.destroy()
    plt.close('all')


def draw_graph():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3], 'o')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas = canvas.get_tk_widget()
    canvas.grid(row=0, column=0, padx=10, pady=10)


window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", on_closing)
style = Style(theme="minty")

draw_button = Button(window, text="Draw Graph", command=draw_graph)
draw_button.grid(row=1, column=0, padx=10, pady=10)

window.mainloop()