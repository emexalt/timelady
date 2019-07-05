#timelady.py
#discord bot who returns local time of whatever server it runs on
#6.3.2019, emexalt

import discord, datetime, logging
from discord.ext import commands

TOKEN = ""

logging.basicConfig(level=logging.DEBUG)

timelady = commands.Bot(command_prefix="$")

#sets status of bot when server is running
@timelady.event
async def on_ready():
    print("The bot is ready!")
    await timelady.change_presence(activity=discord.Game(name="Making a bot!"))

#$test to test whether bot can send msg
@timelady.command()
async def test(ctx):
    await ctx.send("hello, world!")

#display time on $time cmd
@timelady.command()
async def time(ctx):
    time = str(datetime.datetime.now().time())
    await ctx.send("The time from your Telephone Company is: " + time, tts=True)

timelady.run(TOKEN)

