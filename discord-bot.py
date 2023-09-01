import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions
from discord.ext import tasks
import discord.utils
import datetime
import time
import random

intents = discord.Intents().all()
Client = commands.Bot(command_prefix='wd!', intents=intents)

@Client.event
async def on_ready():
    activity = discord.Game(name="with ambatakum")
    await Client.change_presence(status=discord.Status.idle, activity=activity)
    print("its ready for testing")
    
#moderation commands 
@Client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None): 
    await member.ban(reason = reason)
    await ctx.send('GET BANNED')
    await ctx.send('HE WAS BANNED FOR ' + reason)
    await ctx.delete()
    await ctx.delete_after(5)
    
@Client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send('GET KICKED HE WAS KICKED FOR ' + reason)
    await ctx.delete()
    await ctx.delete_after(5)
    
@Client.command()
@commands.bot_has_guild_permissions(mute_members = True)
async def mute(ctx, member : discord.Member, timelimit):
    if "s" in timelimit:
        gettime = timelimit.strip("s")
        if int(gettime) > 2419000:
            await ctx.send('to much time sorry')
            await ctx.delete_after(5)
        else:
            newtime = datetime.timedelta(seconds=int(gettime))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
            await ctx.send(member + 'was muted')
            await ctx.delete_after(5)
    elif "m" in timelimit:
        gettime = timelimit.strip("m")
        if int(gettime) > 40320:
            await ctx.send('to much time sorry')
            await ctx.delete_after(5)
        else:
            newtime = datetime.timedelta(minutes=int(gettime))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
            await ctx.send(member + 'was muted')
            await ctx.delete_after(5)
    elif "h" in timelimit:
        gettime = timelimit.strip("h")
        if int(gettime) > 672:
            await ctx.send('to much time sorry')
            await ctx.delete_after(5)
        else:
            newtime = datetime.timedelta(hours=int(gettime))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
            await ctx.send(member + 'was muted')
            await ctx.delete_after(5)
    elif "d" in timelimit:
        gettime = timelimit.strip("d")
        if int(gettime) > 28:
            await ctx.send('to much time sorry')
            await ctx.delete_after(5)
        else:
            newtime = datetime.timedelta(days=int(gettime))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
            await ctx.send(member + 'was muted')
            await ctx.delete_after(5)    
    elif "S" in timelimit:
        if "S" in timelimit:
            gettime = timelimit.strip("s")
        if int(gettime) > 2419000:
            await ctx.send('to much time sorry')
            await ctx.delete_after(5)    
        else:
            newtime = datetime.timedelta(seconds=int(gettime))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
            await ctx.send(member + 'was muted')
            await ctx.delete_after(5)    
    elif "M" in timelimit:
        gettime = timelimit.strip("M")
        if int(gettime) > 40320:
            await ctx.send('to much time sorry')
            await ctx.delete_after(5)
        else:
            newtime = datetime.timedelta(minutes=int(gettime))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
            await ctx.send(member + 'was muted')
            await ctx.delete_after(5)
    elif "H" in timelimit:
        gettime = timelimit.strip("H")
        if int(gettime) > 672:
            await ctx.send('to much time sorry')
            await ctx.delete_after(5)
    
        else:
            newtime = datetime.timedelta(hours=int(gettime))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
            await ctx.send(member + 'was muted')
            await ctx.delete_after(5)

    elif "D" in timelimit:
        gettime = timelimit.strip("D")
        if int(gettime) > 28:
            await ctx.send('to much time sorry')
        else:
            newtime = datetime.timedelta(days=int(gettime))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
            await ctx.send(member + 'was muted')
            await ctx.delete()    
            await ctx.delete_after(5)
@Client.command()
@commands.bot_has_guild_permissions(ban_members = True)
async def unban(ctx, userId: discord.User):
  await ctx.guild.unban(userId)
  await ctx.delete()
  await ctx.delete_after(5)




@Client.command()
@commands.bot_has_guild_permissions(manage_roles = True)
async def addrole(ctx, role: discord.Role, user: discord.Member):
    await user.add_roles(role)
    await ctx.send('success')






@Client.command()
@commands.bot_has_guild_permissions(manage_roles = True)
async def removerole(ctx, role: discord.Role, user: discord.Member):
    await user.remove_roles(role)
    await ctx.send('success')

##################fun commands
@Client.command()
async def hack(ctx):
    await ctx.send('hacking starting')
    await ctx.send('█▒▒▒▒▒▒▒▒▒ 10%. hacking project wd stealing the source')
    time.sleep(2)
    await ctx.send('██▒▒▒▒▒▒▒▒ 20%. hacking walker')
    time.sleep(2)
    await ctx.send('███▒▒▒▒▒▒▒ 30%. sending bombs to walkers location')
    time.sleep(2)
    await ctx.send('████▒▒▒▒▒▒ 40%. hacking zenci ')
    time.sleep(2)
    await ctx.send('█████▒▒▒▒▒ 50%. banning zenci')
    time.sleep(2)
    await ctx.send('██████▒▒▒▒ 60%. override override unbanning zenci ')
    time.sleep(2)
    await ctx.send('███████▒▒▒ 70%. found zenci address')
    time.sleep(2)
    await ctx.send('████████▒▒ 80%. he lives at 12 pakistan road')
    time.sleep(2)
    await ctx.send('█████████▒ 90%. hacking ambatakum')
    time.sleep(2)
    await ctx.send('██████████ 100%. giving zenci ballz ')
    time.sleep(2)
    await ctx.send('success zenci has mod :cool:')




@Client.command()
async def hop(ctx):
    await ctx.send('.skip', delete_after=1)
    


@Client.command()
async def zenci(ctx):
    await ctx.send('zenci is the hottest man in the world is daddy best coder made this bot easy')
TOKEN = "put the token here dawg"
Client.run(TOKEN)
