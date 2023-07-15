#######################匯入模組########################
from moviepy.editor import *
import sys
import os
from function.function import *
#######################初始化########################
os.chdir(sys.path[0])

#######################取得影片資訊########################
u = "https://www.youtube.com/watch?v=WlfIYn8-1pI"
# u = input("請輸入網址(輸入n跳過):")
if u != "n":
    title, author, length, _, res = get_video_info(u)
    print(res)
#######################下載影片########################
r = input("根據上面的資訊, 請輸入要下載的影片的解析度(720p/480p/360p/240p/144p(n為跳過)):")
if r != "n":
    if dwonload_video(u, r):
        print("下載完成")
    else:
        print("找不到該解析度的影片")

#######################切割影片########################
r = input("要不要切割影片(n/y):")
if r != "n":
    beg = int(input("請輸入要切割的開始時間(秒):"))
    end = int(input("請輸入要切割的結束時間(秒):"))

    result = "剪輯完成" if cut_video(f"{title}.mp4", beg, end) else "剪輯失敗"
    print(result)
#######################合併影片########################
r = input("要不要合併影片(n/y):")
if r != "n":
    file_name_list = []
    for i in range(10):
        file_name_list.append("【小小兵】第三支精采可愛預告-9-10.mp4")

    # file_name_list = ["【小小兵】第三支精采可愛預告-9-10.mp4", "【小小兵】第三支精采可愛預告-9-10.mp4", "【小小兵】第三支精采可愛預告-9-10.mp4"]
    # if merge_video(file_name_list, "合併影片.mp4"):
    #     print("合併影片成功")
    # else:
    #     print("合併影片失敗")
    result = "合併影片成功" if merge_video(file_name_list, "合併影片.mp4") else "合併影片失敗"
    print(result)
#######################影片轉GIF########################
r = input("要不要影片轉GIF(y/n):")
if r != "n":
    video_path = "合併影片.mp4"
    gif_path = "【小小兵】第三支精采可愛預告.gif"

    result = "影片轉GIF成功" if video_to_gif(video_path, gif_path) else "影片轉檔失敗"
    print(result)
