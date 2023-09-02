import discord
import aiohttp
import asyncio
from discord.ext import commands
import random
import string
from dhooks import Webhook


bot1 = commands.Bot(command_prefix='!', self_bot=True)


# psxbet auto rain joiner 


@bot1.event
async def on_message(message: discord.Message):    
    ch = await bot1.fetch_channel(1126511960545046659)
    async for message in ch.history(limit=1):
        for comp in message.components:
            for child in comp.children:
                await child.click()
                



bot1.run('')
