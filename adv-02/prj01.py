# 匯入 tkinter 模組和 random 模組
from tkinter import *
import random


# 定義 hi_fun 函數，當按鈕被按下時，將標籤的文字設為 "Hi Singular"，前景顏色隨機選擇 COLORS 中的一種。
def hi_fun():
    display.config(text="Hi Singular", fg=random.choice(COLORS))


# 定義 COLORS，為一個包含了多種顏色的列表
COLORS = [
    "black",
    "red",
    "green",
    "blue",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "gray",
    "cyan",
    "magenta",
    "gold",
    "silver",
    "lime",
    "maroon",
    "navy",
    "olive",
    "teal",
    "violet",
    "indigo",
    "coral",
    "crimson",
    "hotpink",
    "khaki",
    "lavender",
    "lavenderblush",
    "lemonchiffon",
    "lightblue",
    "lightcoral",
    "lightcyan",
    "lightgoldenrodyellow",
    "lightgreen",
    "lightgrey",
    "lightpink",
    "lightsalmon",
    "lightseagreen",
    "lightskyblue",
    "lightslategray",
    "lightsteelblue",
    "lightyellow",
]

# 創建主視窗
windows = Tk()

# 設定主視窗標題
windows.title("My first GUI")

# 創建一個按鈕，當被按下時，執行 hi_fun 函數
btn1 = Button(windows, text="Show Screen", command=hi_fun)

# 將按鈕加入主視窗中
btn1.pack()

# 創建一個標籤，顯示 "Hi Singular"
display = Label(windows, text="Hi Singular")

# 將標籤加入主視窗中
display.pack()

# 開始執行主迴圈，等待用戶操作
windows.mainloop()