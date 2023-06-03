#######################模組#######################
import discord
import os
from dotenv import load_dotenv
from function import function as mf

#######################初始化#######################

# 載入環境變數
load_dotenv()

# 建立機器人
bot = discord.Bot()


#######################事件#######################
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


#######################指令#######################
@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
    """輸入hello, 會回傳Hey!"""
    await ctx.respond("SB!")


@bot.slash_command(name="weather",
                   description="Get the weather of the next 7 days")
async def weather(ctx):
    """輸入weather, 會回傳未來七天溫度的圖表"""
    info = mf.call_weather_api()
    dates, temps = mf.get_7_Days_weather(info)
    icon_code = info["current"]["weather"][0]["icon"]
    mf.save_weather_icon(icon_code)
    fig = mf.get_plot_fig(dates, temps, f"{info['timezone']}未來七天溫度", "日期",
                          "溫度")
    fig.savefig("weather.png")
    await ctx.respond(file=discord.File("weather.png"))
    await ctx.respond(file=discord.File(f"{icon_code}.png"))


#######################啟動#######################
def main():
    # 讀取環境變數, 並啟動機器人
    bot.run(os.getenv('TOKEN'))


# 主程式, 這樣寫是為了讓程式碼更有模組化, 同時可以當作模組使用
if __name__ == "__main__":
    main()