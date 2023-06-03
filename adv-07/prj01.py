import requests
from ttkbootstrap import *
import sys
import os
from PIL import Image, ImageTk

os.chdir(sys.path[0])

api_key = "892da2f13edf3c7f382637760e72d224"

base_url = "https://api.openweathermap.org/data/2.5/weather?"
units = "metric"
lang = "zh_tw"


def get_weather_info():
    city_name = entry.get()
    send_url = base_url
    send_url += "appid=" + api_key
    send_url += "&q=" + city_name
    send_url += "&units=" + units
    send_url += "&lang=" + lang

    response = requests.get(send_url)
    info = response.json()

    if "main" in info.keys():
        global current_temperature
        temp_info = info["main"]
        current_temperature = temp_info["temp"]
        weather_info = info["weather"][0]
        weather_description = weather_info["description"]
        icon_code = weather_info["icon"]

        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
        response = requests.get(icon_url)
        with open(f"{icon_code}.png", "wb") as icon_file:
            icon_file.write(response.content)

        image = Image.open(f"{icon_code}.png")
        tk_image = ImageTk.PhotoImage(image)
        lable2.config(image=tk_image)
        lable2.image = tk_image
        lable3.config(text=f'溫度:{current_temperature}')
        lable4.config(text=f'描述:{weather_description}')


front_size = 20
window = tk.Tk()
window.title("My GUI")
window.option_add("*font", ("Helvetica", front_size))

style = Style(theme="flatly")
style.configure('my.TButton', font=("Helvetica", front_size))
style.configure('my.TCheckbutton', font=("Helvetica", front_size))

lable = Label(window, text="請輸入想搜尋的城市:")
lable.grid(row=0, column=0, sticky="W")

button = Button(window,
                text="獲得天氣資訊",
                command=get_weather_info,
                style="my.TButton")
button.grid(row=0, column=2, sticky="E")

lable2 = Label(window, text="天氣圖標")
lable2.grid(row=1, column=0)

entry = Entry(window)
entry.grid(row=0, column=1)

lable3 = Label(window, text="溫度:")
lable3.grid(row=1, column=1)

lable4 = Label(window, text="描述:")
lable4.grid(row=1, column=2)

check_type = BooleanVar()
check_type.set(True)


def on_switch_change():
    global units, current_temperature
    if check_type.get():
        units = "metric"

    else:
        units = "imperial"

    if lable3.cget("text") != "溫度: ?℃":
        if units == "metric":
            current_temperature = round((current_temperature - 32) * 5 / 9, 2)
        elif units == "imperial":
            current_temperature = round(current_temperature * 9 / 5 + 32, 2)
        lable3.config(text=f"溫度:{current_temperature}")


check = Checkbutton(window,
                    text="溫度單位(℃/℉)",
                    variable=check_type,
                    onvalue=True,
                    offvalue=False,
                    command=on_switch_change,
                    style='my.TCheckbutton')
check.grid(row=2, column=1)

window.mainloop()
