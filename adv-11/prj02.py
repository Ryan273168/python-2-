#######################匯入模組########################
from pytube import YouTube  # pip install -U pytube
import os
import sys

#######################初始化########################
os.chdir(sys.path[0])  # 將工作目錄設置為目前檔案所在的目錄

#######################取得影片資訊########################
yt = YouTube("https://www.youtube.com/watch?v=WlfIYn8-1pI")  # 建立YouTube物件
print(f"影片名稱:{yt.title}")  # 取得影片的標題資訊
print(f"影片作者:{yt.author}")  # 取得影片的作者資訊
print(f"影片長度:{yt.length}秒")  # 取得影片的長度資訊
print(f"縮圖網址:{yt.thumbnail_url}")  # 取得影片的縮圖網址

streams = yt.streams  # 取得影片的所有串流

# 取得影片的所有串流的資訊
for stream in streams:
    print(stream)

print("========================================")
# 篩選progressive代表影片有音訊與影像, file_extension='mp4'代表影片格式為mp4
streams = yt.streams.filter(progressive=True, file_extension='mp4')

# 取得篩選後的影片串流的資訊
for stream in streams:
    print(stream)

res = []
for stream in streams:
    res.append(stream.resolution)

print(res)

#######################下載影片########################
# 選擇解析度
r = input("根據上面的資訊, 請輸入要下載的影片的解析度(720p/480p/360p/240p/144p):")
# 判斷解析度有沒有在目前的streams裡面
if r in res:
    # 取得該解析度的串流
    stream = streams.filter(res=r)[0]
    # 下載影片
    stream.download()
    print("下載完成")
else:
    print("找不到該解析度的影片")