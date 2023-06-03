import requests  # 載入 requests 套件 (用來發送請求) 內建json模組
import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
import sys

os.chdir(sys.path[0])

api_key = "892da2f13edf3c7f382637760e72d224"  # API Key
base_url = "https://api.openweathermap.org/data/2.5/onecall?"  # API URL
lon = "121.5319"
lat = "25.0478"
exclude = "minutely,hourly"
units = "metric"  # 單位 (公制)
lang = "zh_tw"  # 語言 (繁體中文)

send_url = base_url
send_url += "lat=" + lat
send_url += "&lon=" + lon
send_url += "&exclude=" + exclude
send_url += "&appid=" + api_key
send_url += "&units=" + units
send_url += "&lang=" + lang

print(send_url)  # 印出發送的 URL
response = requests.get(send_url)  # 發送請求
info = response.json()

xlist = []
ylist = []

if "daily" in info.keys():
    for i in range(7):
        temp = info["daily"][i]["temp"]["day"]
        time = datetime.datetime.fromtimestamp(
            info["daily"][i]["dt"]).strftime("%m/%d")
        xlist.append(time)
        ylist.append(temp)
        print(f"{time}的溫度是{temp}度")

else:
    print(" Request Fail ")

font = FontProperties(fname='NotoSansHK-Regular.otf', size=14)
fig, ax = plt.subplots()
ax.plot(xlist, ylist)
ax.set_xlabel('日期', fontproperties=font)
ax.set_ylabel('時間', fontproperties=font)
ax.set_title('7天氣溫預測', fontproperties=font)
plt.show()
