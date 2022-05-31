"""
Github: Plushhh
Website: plushhhh.carrd.co

Please read the readme.md before you do anything.

Also plz dont leach
"""
from discord.ext import commands
import discord
import time
import datetime

print("Starting, please wait.")

token = "defo my token bruh" # Put your ALT'S TOKEN ***NOT YOUR MAIN***
discord_id = "689744458761371648" # Put your main discord accounts id here, the account has to be in the server you're sending the commmand in.
bot = commands.Bot("/--/", self_bot=True)
now = datetime.datetime.now()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="plushhh's yt GO SUB")) # You can delete this line or change ducchub to your server name, its just a custom status
    print("""
                    Sub to me, link on website                       
                    Type '/--/farm' to start                                    
                            Credits:
                        Github: Plushhh
                    Website: plushhh.carrd.co
                                                                     """)

@bot.command()
async def farm(ctx):
    print("Starting farm.")
    while True:
        await ctx.send('pls beg')
        print("sent 'pls beg' " + str(now))
        time.sleep(4)
        await ctx.send('pls fish')
        print("sent 'pls fish' " + str(now))
        time.sleep(5)
        await ctx.send("pls hunt")
        print("sent 'pls hunt' " + str(now))
        time.sleep(5)
        await ctx.send("pls sell fish all")
        print("sent 'pls sell fish all' " + str(now))
        time.sleep(5)
        await ctx.send("pls sell seawead all")
        print("sent 'pls sell seawead all' " + str(now))
        time.sleep(3)
        await ctx.send("pls sell boar all")
        print("sent 'pls sell boar all' " + str(now))
        time.sleep(2)
        await ctx.send("pls sell skunk all")
        print("sent 'pls sell skunk all' " + str(now))
        time.sleep(4)
        await ctx.send("pls sell rabbit all")
        print("sent 'pls sell rabbit all' " + str(now))
        time.sleep(4)
        await ctx.send("pls sell duck all")
        print("sent 'pls sell duck all' " + str(now))
        time.sleep(3)
        await ctx.send("pls sell trash all")
        print("sent 'pls sell trash all' " + str(now))
        time.sleep(4)
        await ctx.send("pls dep all")
        print("sent 'pls dep all " + "Deposits all your money" + str(now))
        time.sleep(5)



bot.run(token, bot=False)