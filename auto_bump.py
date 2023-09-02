import discord
from discord.ext import commands, roles
import asyncio



bot = commands.Bot(commands_prefix='!', self_bot=True)

### auto bump shi les goo



@bot.command()
async def autobump(ctx):
    channel = bot.fetch_channel()
    for _ in range(1000000000000000000000000000000):        
        async for scmd in channel.slash_commands():
            if scmd.name == "bump" and scmd.application.bot.name == "DISBOARD":
                await scmd.__call__(channel=channel)
                await asyncio.sleep(7200)
                

                
bot.run('token here wow')
