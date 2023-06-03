from ttkbootstrap import *
import sys
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from function.function import *

os.chdir(sys.path[0])  # 設定工作目錄


def get_weather_info():
    global current_temperature
    # 使用OpenWeatherMap API獲取天氣資訊
    info = call_weather_api(lon_entry.get(), lat_entry.get())

    if "daily" in info.keys():  # 如果有main這個key，代表有天氣資訊
        current_temperature = info["current"]["temp"]
        weather_description = info["current"]["weather"][0]["description"]
        icon_code = info["current"]["weather"][0]["icon"]

        # 下載並保存天氣圖標
        save_weather_icon(icon_code)

        # 更新GUI
        image = Image.open(f"{icon_code}.png")  # 打開圖片
        tk_image = ImageTk.PhotoImage(image)  # 將圖片轉換為tkinter可以使用的格式
        icon_label.config(image=tk_image)  # 更新圖片 # type: ignore
        icon_label.image = tk_image  # type: ignore # 避免被記憶體回收機制回收圖片

        temperature_label.config(text=f"溫度: {current_temperature}°C")
        description_label.config(text=f"描述: {weather_description}")
        city_name_label.config(text=f"目前搜尋的地區: {info['timezone']}")

        # 獲取七天天氣資訊, 建立日期和溫度的list
        dates, temps = get_7_Days_weather(info)

        # 建立圖表
        fig = get_plot_fig(dates, temps, "七日天氣預報", "日期", "溫度(°C)")
        # 將圖表添加到 tkinter GUI
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas = canvas.get_tk_widget()
        canvas.grid(row=4, column=0, columnspan=3)

    else:  # 如果沒有main這個key，代表沒有天氣資訊
        city_name_label.config(text=f"目前搜尋的地區: City Not Found")


def on_switch_change():
    global units, current_temperature
    if check_type.get():
        units = "metric"

    else:
        units = "imperial"

    if temperature_label.cget("text") != "溫度: ?°C":
        if units == "metric":
            current_temperature = round((current_temperature - 32) * 5 / 9, 2)
            temperature_label.config(text=f"溫度: {current_temperature}°C")
        elif units == "imperial":
            current_temperature = round(current_temperature * 9 / 5 + 32, 2)
            temperature_label.config(text=f"溫度: {current_temperature}°F")


def on_closing():
    window.destroy()
    plt.close('all')


lon = "121.5319"  # Taipei  的經度
lat = "25.0478"  # Taipei  的緯度

font_size = 20
window = tk.Tk()
window.title("Weather App")
window.protocol("WM_DELETE_WINDOW", on_closing)
window.option_add("*font", ("Helvetica", font_size))

style = Style(theme="minty")
style.configure('my.TButton', font=('Helvetica', font_size))
style.configure('my.TCheckbutton', font=('Helvetica', font_size))

# 城市名稱輸入框
city_name_label = Label(window, text="目前搜尋的地區:?")
city_name_label.grid(row=0, column=0, rowspan=2, padx=10, pady=10)

# 查詢按鈕
search_button = Button(window,
                       text="獲得天氣資訊",
                       command=get_weather_info,
                       style='my.TButton')
search_button.grid(row=0, column=2, rowspan=2, padx=10, pady=10)

# 經度輸入框, 預設顯示lon
lon_var = tk.StringVar()
lon_var.set(lon)
lon_entry = Entry(window, width=20, textvariable=lon_var)
lon_entry.grid(row=0, column=1, padx=10, pady=10)

# 緯度輸入框, 預設顯示lat
lat_var = tk.StringVar()
lat_var.set(lat)
lat_entry = Entry(window, width=20, textvariable=lat_var)
lat_entry.grid(row=1, column=1, padx=10, pady=10)

# 天氣圖標
icon_label = Label(window, text="天氣圖標")
icon_label.grid(row=2, column=0)

# 溫度標籤
temperature_label = Label(window, text="溫度: ?°C")
temperature_label.grid(row=2, column=1)

# 描述標籤
description_label = Label(window, text="描述: ?")
description_label.grid(row=2, column=2)

check_type = BooleanVar()
check_type.set(True)

check = Checkbutton(window,
                    variable=check_type,
                    onvalue=True,
                    offvalue=False,
                    command=on_switch_change,
                    text="溫度單位(°C/°F)",
                    style='my.TCheckbutton')
check.grid(row=3, column=1)

# 運行應用程式
window.mainloop()