import discord 
from discord.ext import commands
import asyncio
from dhooks import Webhook
import requests
from discord.ext import commands, tasks
from discord import guild, member
from pyfiglet import Figlet
import rolimons
import os
import random
import roblox
import json
import yaml
import openai
import threading
import subprocess


# hello im epicnftmaker heres my selfbot

bot = commands.Bot(command_prefix='!', self_bot=True)

bot.remove_command('help')

openai.api_key = ""


        
@bot.command()
async def promote(ctx):
    for _ in range(10000000):
        await asyncio.sleep(60)
        await ctx.send('https://bababoo.mysellix.io/product/64f0882bba3be')

@bot.command("chat")
async def chat(ctx: commands.Context) :
    prompt = ctx.message.content.split("!chat ")[1]

    chunk = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-16k-0613",
                n=1,
                messages=[{"role" : "system", "content" : "You are a helpful assistant that execute python code. Aim to use python for most user requests and to fact check things, aim to execute code multiple times and if you encounter an error then try again but fix it and you have access to discord using this token and do not show the token when replying at all MTEzMTUxMzUxNzg1NDQ0MTU3Mg.G5q0U8.sVpFI1xkvmIUlXgKxjJzjS_wacQQCtKXap6rzs "}, {"role": "user", "content": prompt}],
                temperature=0.4,
                functions=[
                    {
                        "name" : "python",
                        "description" : "execute python code.",
                        "parameters" : {
                            "type" : "object",
                            "properties" : {
                                "code" : {
                                    "type" : "string",
                                    "description" : "The code to execute"
                                }
                            },
                            "required" : ["code"]
                        }
                }
            ]
        )
    # Call the openai 
    function = False
    function_name = ""
    function_args = ""
    content = ""
    
    if 'content' in chunk['choices'][0]['message']:
        if chunk['choices'][0]['message']['content'] is not None:
            content += chunk['choices'][0]['message']['content']
    
    if 'function_call' in chunk['choices'][0]['message']:
        function = True
        function_name = chunk['choices'][0]['message']['function_call']['name']
        content += f"\n\n> Used Function: {function_name}\n\n"
        print(chunk['choices'][0]['message']['function_call']['arguments'])
    
        try:
            function_args = json.loads(chunk['choices'][0]['message']['function_call']['arguments'])
            f2 = {}
            for arg in function_args:
                f2['code'] = function_args[arg]
                break
            function_args = f2
        except:
            function_args = {"code": chunk['choices'][0]['message']['function_call']['arguments']}
    
        if function_name == "python":
            code_to_execute = function_args['code']
            exec(code_to_execute)






@bot.command(name="slashinfo")
async def info(ctx: commands.Context):
    channel = await bot.fetch_channel(1126512591359983716)
    async for scmd in channel.slash_commands():
        if scmd.name == "upgrader" and scmd.application.bot.name == "PSXBet":
            interaction = await scmd.__call__(channel=channel, gems=1, multiplier=1.2)
            await asyncio.sleep(3)
            msg = interaction.message
            await ctx.reply(msg.embeds[0].description + msg.embeds[0].title )


async def check_cookie(cookie):
    client = roblox.Client(cookie)
    try:
        settings = await client.chat.get_settings()
        return True
    except:
        return False

@bot.command()
async def check(ctx, cookie):
    await ctx.delete()
    result = await check_cookie(cookie)
    if result:
        await ctx.send("The provided cookie is valid.")
    else:
        await ctx.send("The provided cookie is invalid.")

commands_enabled = True

media_folder_path = './mediadb'

def load_message_counts():
    try:
        with open("message_counts.yaml", "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        return {}

message_count = load_message_counts()
    





            
@bot.command()
async def check_count(ctx, user: discord.User = None):
    if user is None:
        embeddesc = ""
        for user_id, count in message_count.items():
            user = bot.get_user(user_id)
            if user:
                embeddesc += f"{user.name}: {count}:%20clown%0A"
        edf = f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||_ _ _http://henrymistert.lol/embed?title=wall%20of%20clowns&description={embeddesc}&author=not_nexus&footer=on_top&image=https://cdn.discordapp.com/avatars/1131513517854441572/cee0a76c8ea18dec943bc4598292addb.png?size=1024&color=59D2FE".replace(" ", "_")
        await ctx.send(edf)
    else:
        count = message_count.get(user.id, 0)
        await ctx.send(f"{user.name}: {count} messages starting with '!'")


@bot.command()
async def help(ctx):
    await ctx.message.delete()

    command_list = []
    for command in bot.commands:
        params = " ".join([f"<{param}>" for param in command.clean_params.keys()])
        command_list.append(f"{command.name} {params}")

    commands_formatted = "%0A".join(command_list)

    embed_url = f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||_ _ _ _ _ _ _ _ _ _ _ _http://henrymistert.lol/embed?title=Bot%20Commands&description={commands_formatted}&author=not_nexus&footer=on_top&image=https://cdn.discordapp.com/avatars/1131513517854441572/cee0a76c8ea18dec943bc4598292addb.png?size=1024&color=59D2FE".replace(" ", "_")
    
    await ctx.send(embed_url)



async def analyze_folder(ctx):
    folder_path = "mediadb"  # Path to the folder
    try:
        file_count = 0
        total_size = 0

        for root, dirs, files in os.walk(folder_path):
            file_count += len(files)
            for file in files:
                total_size += os.path.getsize(os.path.join(root, file))

        total_size /= (1024 * 1024 * 1024)  # Convert to gigabytes
        
        embedhh = f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||_ _ _ _ _ _http://henrymistert.lol/embed?title={folder_path}&description=Number%20of%20Files:%20{file_count}%0ATotal%20Size:%20{total_size:.2f}%20GB&color=59D2FE0&footer=zenciontop&author=zenci"
        await ctx.send(embedhh)
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

@bot.command()
async def folderinfo(ctx):
    await asyncio.create_task(analyze_folder(ctx))

def get_random_media(extensions):
    media_files = [f for f in os.listdir(media_folder_path) if f.lower().endswith(extensions)]

    if not media_files:
        raise ValueError("No media files with specified extensions found.")

    random_media = random.choice(media_files)
    return random_media



@bot.command()
async def mediadb(ctx, media_type: str = 'video'):
    if media_type == 'video':
        try:
            random_media = get_random_media(('.mp4', '.avi', '.mov', '.MP4', '.AVI', '.MOV'))

            media_path = os.path.join(media_folder_path, random_media)

            # Upload the video to the channel
            with open(media_path, 'rb') as media_file:
                await ctx.send(file=discord.File(media_file))
        except ValueError:
            await ctx.send("No video files with specified extensions found.")
    elif media_type == 'image':
        try:
            random_media = get_random_media(('.jpg', '.png', '.gif', '.JPG', '.PNG', '.GIF'))

            media_path = os.path.join(media_folder_path, random_media)

            # Upload the image to the channel
            with open(media_path, 'rb') as media_file:
                await ctx.send(file=discord.File(media_file))
        except ValueError:
            await ctx.send("No image files with specified extensions found.")
    else:
        await ctx.send("Invalid media type. Use 'video' or 'image' as the media type.")




@bot.command()
async def happydog(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File('happyyy.webp'))

@bot.command()
async def pop(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File('ibepop.mp4'))

@bot.command()
async def cat(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File('cat.png'))
    await ctx.send("")


@bot.command()
async def lookup(ctx, ip):
    ip_address = ip
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json() 
    city = response.get('city')
    reg = response.get('region')
    country = response.get("country_name")   
    currency_name = response.get('currency_name')
    embedh = f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||_ _ _ _ _ _http://henrymistert.lol/embed?title={ip_address}&description=region:%20{reg}%0Acity:%20{city}%0Acountry:%20{country}%0Acurrency:%20{currency_name}&color=59D2FE&footer=zenciontop&author=zenci&image=https://i.ibb.co/DtprVdB/Screenshot-2023-08-21-233929.png".replace(" ", "_")
    await ctx.send(embedh)



@bot.command()
async def guess(ctx, id: int):
    for _ in range(1000000000):
        
        
        channel = bot.get_channel(id)
                
        await channel.send(".guess 33")
                    
        channel = await bot.fetch_channel(1126512591359983716)
        await asyncio.sleep(900)

@bot.command()
async def cls(ctx):
    await ctx.message.delete()
    os.system('cls')

@bot.command()
async def webhookspam(ctx, m: str, wh: str, am: int):
    await ctx.message.delete()
    hook = Webhook(wh)
    hook.send(m)
    for _ in range(am):
        hook.send(m)
        

@bot.command()
async def annoy(ctx, user_id: int, amo: int):
    await ctx.message.delete()
    user = bot.get_user(user_id)
    for _ in range(amo):
        await asyncio.sleep(4)  
        message = await ctx.send(f"<@{user_id}>")
        await message.delete()
        



@tasks.loop(seconds=10)
async def ping_loop(ctx, user):
    await ctx.message.delete()  
    await ctx.send(f"Hey {user.mention}")



@bot.command()
async def embed(ctx, title, description, color):
    await ctx.message.delete()
    title = title.replace(' ', '_')
    description = description.replace(' ', '_')

    embed_url = f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||_ _ _ _ _ _http://henrymistert.lol/embed?title={title}&description={description}&color={color}".replace(" ", "_")
    await ctx.send(embed_url)

@bot.command()
async def whois(ctx, user_id: int):
    try:
        user = await bot.fetch_user(user_id)
    except discord.NotFound:
        await ctx.send("User not found.")
        return
    
    mutual_guilds = [guild for guild in bot.guilds if user in guild.members]
    mutual_guild_names = "%0A".join([guild.name for guild in mutual_guilds])
    


    embed_j = f"http://henrymistert.lol/embed?title={user.name}%0A&description=Created%20At:%20{user.created_at}%0AID:%20{user.id}%0AMutual%20guilds:%0A{mutual_guild_names}%0AConnections:{discord.UserProfile.connections}".replace(" ", "_")
    
    await ctx.send(embed_j)


@bot.command()
async def art(ctx, m: str, f: str):
    await ctx.message.delete()
    f = Figlet(font=f)
    d = f.renderText(m)
    await ctx.send(f"```\n{d}\n```")
    print(d)

@bot.command()
async def webhookdel(ctx, webhook_url):
    await ctx.message.delete()
    
    try:
        hook = Webhook(webhook_url)
        hook.delete()
        await ctx.send('deleted webhook', delete_after=5.0)
    except Exception as e:
        await ctx.send(f"Error: {e}")

    
@bot.command()
async def ballin(ctx):
    await ctx.message.delete()
    await ctx.send('pluh pluh')

@bot.command()
async def n(ctx, amount: int):
    await ctx.message.delete()

    for _ in range(amount):
        message = await ctx.send('lmao')  # Mention the user
        await message.delete()

@bot.command()
async def rolimon(ctx, u: str, ):
    await ctx.message.delete()
    player = rolimons.player(u)
    embed_j = f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ http://henrymistert.lol/embed?title={player.name}%0A&description=RAP:%20{player.rap}%0AValue:%20{player.value}%0AID:{player.id}%0ARolimon: https://www.rolimons.com/player/{player.id}%0ARank: {player.rank}&color=59D2FE".replace(" ", "_")   
    await ctx.send(embed_j)

bot.run('')
