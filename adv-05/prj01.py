import requests
import os
import sys

os.chdir(sys.path[0])
api_key = "892da2f13edf3c7f382637760e72d224"

base_url = "https://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name :")
units = "metric"
lang = "zh_tw"

send_url = base_url
send_url += "appid=" + api_key
send_url += "&q=" + city_name
send_url += "&units=" + units
send_url += "&lang=" + lang
print(send_url)

response = requests.get(send_url)
info = response.json()

if "main" in info.keys():
    icon_code = info["weather"][0]["icon"]
    icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
    response = requests.get(icon_url)
    with open(f"{icon_code}.png", "wb") as icon_file:
        icon_file.write(response.content)
else:
    print(" City Not Found ")