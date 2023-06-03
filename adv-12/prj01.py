#######################匯入模組########################
from pytube import YouTube  # pip install -U pytube
import os
import sys
from function import function as fun

#######################初始化########################
os.chdir(sys.path[0])  # 將工作目錄設置為目前檔案所在的目錄

#######################主程式########################

u = "https://www.youtube.com/watch?v=WlfIYn8-1pI"
_, _, _, _, res = fun.get_video_info(u)
print(res)

r = input("根據上面的資訊, 請輸入要下載的影片的解析度(720p/480p/360p/240p/144p):")

if fun.dwonload_video(u, r):
    print("下載完成")
else:
    print("找不到該解析度的影片")