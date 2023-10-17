import discord
from discord.ext import commands
from apikeys import BOTTOKEN
from srcs import Commands
import asyncio
import os

intents = discord.Intents().all()

intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="GitHub/MVPee")
    )
    print("""
        _________                             __________        __   
        \_   ___ \  ____  __ ________  ______ \______   \ _____/  |_ 
        /    \  \/ /  _ \|  |  \____ \/  ___/  |    /  _//  _ \   __\\
        \     \___(  <_> )  |  /  |_> >___ \   |____\   (  <_> )  |  
        \______  /\____/|____/|   __/____  >  |______  /\____/|__|  
                \/             |__|       \/          \/             
    """)

async def load():
    for filename in os.listdir("./srcs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"srcs.{filename[:-3]}")

async def main():
    await load()
    await bot.start(BOTTOKEN)

asyncio.run(main())