#######################匯入模組########################
from moviepy.editor import *
import sys
import os
from function import function
#######################初始化########################
os.chdir(sys.path[0])

#######################取得影片資訊########################
u = "https://www.youtube.com/watch?v=WlfIYn8-1pI"
title, author, length, _, res = function.get_video_info(u)
print(res)
#######################下載影片########################
r = input("根據上面的資訊, 請輸入要下載的影片的解析度(720p/480p/360p/240p/144p):")

if function.dwonload_video(u, r):
    print("下載完成")
else:
    print("找不到該解析度的影片")

#######################切割影片########################
beg = int(input("請輸入要切割的開始時間(秒):"))
end = int(input("請輸入要切割的結束時間(秒):"))

result = "剪輯完成" if function.cut_video(f"{title}.mp4", beg, end) else "剪輯失敗"
print(result)