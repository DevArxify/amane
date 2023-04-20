import time
import datetime
from time import sleep
import json
import random
import string
import webbrowser
from os import system, name
import os
from discord.ext import commands
from discord.ui import Button, View
import colorama
import asyncio
import re
import urllib.parse 
import io
import aiohttp
import discord
import requests
from colorama import Fore
import urllib.request
from urllib import parse, request
colorama.init()





def clear():
  system("cls")

TOKEN = "YOUR_TOKEN_GOES_HERE"

token = (TOKEN)

ping = False

bot = commands.Bot(command_prefix=("x"), intents=discord.Intents.all())

def whitelist1(ctx):
    return ctx.author.id == 721806436648222829 or ctx.author.id == 934863291463913504

def whitelist2(ctx):
    return ctx.author.id == 713425475334307972 or ctx.author.id == 975954277791047752 or ctx.guild.id == 1003307808260886608 or ctx.author.id == 653564331606409239

punch_gifs = ['https://c.tenor.com/SwMgGqBirvcAAAAM/saki-saki-kanojo-mo-kanojo.gif', 'https://c.tenor.com/p_mMicg1pgUAAAAC/anya-forger-damian-spy-x-family.gif', 'https://c.tenor.com/EfhPfbG0hnMAAAAC/slap-handa-seishuu.gif', 'https://c.tenor.com/YL6r_9EEqrMAAAAM/anime.gif', 'https://c.tenor.com/SQQ4VD6igHIAAAAC/yuji-itadori-yuji.gif', 'https://c.tenor.com/XoeOOzCu6Z0AAAAM/na-parede.gif', 'https://c.tenor.com/FVMcBt8nElMAAAAd/inosuke-zenitsu.gif']
punch_msg = ['punches you!']

kiss_gifs = ['https://c.tenor.com/I8kWjuAtX-QAAAAC/anime-ano.gif', 'https://c.tenor.com/nRdyrvS3qa4AAAAC/anime-kiss.gif', 'https://c.tenor.com/4ofp_xCUBxcAAAAM/eden-of-the-east-akira-takizawa.gif', 'https://c.tenor.com/8ln6Z1e-FVYAAAAM/nagumi-koushi-hozumi-serene.gif', 'https://c.tenor.com/Fyq9izHlreQAAAAC/my-little-monster-haru-yoshida.gif', 'https://c.tenor.com/8V-2mCzxzn0AAAAM/anime-kiss-romance.gif', 'https://c.tenor.com/IvfI1mCRtRoAAAAC/anime-kiss-love.gif']
kiss_msg = ['kisses you!']

play_gifs = ['https://c.tenor.com/bcvK_rU5voEAAAAC/anime-piano.gif', 'https://c.tenor.com/dglU4dQtm-QAAAAC/anime-guitar.gif', 'https://c.tenor.com/SC800OpmNm8AAAAC/your-lie-in-april-piano.gif', 'https://c.tenor.com/rHwHPB9pSnwAAAAC/gotou-anime.gif', 'https://c.tenor.com/1Lu8gPxo8L4AAAAd/showa-genroku.gif', 'https://c.tenor.com/RfwaQU3_U1UAAAAC/show-by-rock-cyan-hijirikawa.gif', 'https://c.tenor.com/RBL4pZwCm9AAAAAM/togetsu-rei-d4dj.gif']
play_msg = ['is playing an instrument!']

kill_gifs = ["https://c.tenor.com/G4SGjQE8wCEAAAAC/mikey-tokyo.gif", "https://c.tenor.com/Ds187JeCgckAAAAC/animehit-fugirl.gif", "https://c.tenor.com/i0PG6AP1qDgAAAAC/anime-cringe.gif", "https://c.tenor.com/AGTqt-wXyiEAAAAS/nichijou-minigun.gif", "https://c.tenor.com/0veQOMPIUX8AAAAd/idleglance-amv.gif", "https://c.tenor.com/WWksHmZigK0AAAAC/akame-ga-kill-anime.gif", "https://c.tenor.com/5zfhwMPXuPwAAAAC/kill-la-kill-anime.gif"]
kill_msg = ["kills you!"]


@bot.event
async def on_message(message):
  await bot.process_commands(message)

@bot.event
async def on_guild_join(guild):
    current_guilds = len(bot.guilds)
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(f'xhelp | Serving {current_guilds} guilds'))


@bot.event
async def on_guild_remove(guild):
    current_guilds = len(bot.guilds)
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(f'xhelp | Serving {current_guilds} guilds'))

@bot.event
async def on_ready():
    current_guilds = len(bot.guilds)
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(f'xhelp | Serving {current_guilds} guilds'))
    print("Made with <3 by Arxify and Polaris")

bot.remove_command("help")

@bot.command()
async def help(ctx):
  button = Button(label='Invite me!', url='https://discord.com/api/oauth2/authorize?client_id=972631150302470145&permissions=8&scope=bot', style=discord.ButtonStyle.blurple, emoji="<:amane_cropped:1010672648256229477>")
  button1 = Button(label='Support Server', url='https://discord.gg/y7AbGYY2uc', style=discord.ButtonStyle.blurple, emoji='<:DiscordSpin:1010673908975931392>')
  view = View()
  view.add_item(button)
  view.add_item(button1)
  embed = discord.Embed(title='Help', description='`help` - It shows you this message\n`credits` - Arxify & Polaris made this\n`kick` - Kicks a user\n`ban` - Bans a user\n`unban` - Unbans a user\n`minesweeper` - You can play this masterpiece\n`8ball` - You can play with the classic 8 Ball\n`cat` - You can see a cool cat\n`panda` - You can see a panda dude, what else do you want?\n`meme` - You get a meme that is not always funny\n`spoiler` - It sends a message like a spoiler\n`avatar` - You can see someones avatar\n`duck` - You can see a gorgeous duck\n`dog` - You can see a fabulous dog\n`punch` - You can punch somebody\n`kiss` - You can kiss someone\n`play` - You can play an instrument\n`kill` - You can kill somebody', color=0x1C1C1C)
  embed.set_footer(text='© Darkside Development')
  embed.set_thumbnail(url='https://media.discordapp.net/attachments/972640633078575114/972800968360091678/amane_cropped.png')
  await ctx.send(embed=embed, view=view)





@bot.command()
async def credits(ctx):
  embed = discord.Embed(title='Credits', description='-- Coded by [lucidry#3019](https://discord.com/users/975954277791047752) for [Darkside Development](https://discord.gg/XTpTVWftCK) --', color=0x1C1C1C)
  embed.set_image(url='https://cdn.discordapp.com/attachments/937327510130155543/937331397268475915/45e88b9d8b773017bc0110d511880a1dd7b2fdb6eb87a9f9c4d23f2c8d555bc7.png')
  embed.set_footer(text='© 2022 Darkside Development')
  await ctx.send(embed=embed)


@bot.command()
async def minesweeper(ctx, size: int = 5):
    m_offets = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1)
    ]
    m_numbers = [
        ":one:",
        ":two:",
        ":three:",
        ":four:",
        ":five:",
        ":six:"
    ]
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = ""
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    embed = discord.Embed(title=f"Click to play:",
                            description=message, color=0x206694)
    await ctx.send(embed=embed)

@bot.command(name='8ball')
async def _ball(ctx, *, question):
    responses = [
        'From my point of view, yes',
        'Ask again later.',
        'It is better if I do not tell it to you now.',
        'I cannot predict right now.',
        'Concentrate and ask again.',
        'Do not count on it.',
        'It is definitely so.',
        'It is the most probable.',
        'My answer is no.',
        'My sources say no.',
        'From my point of view, maybe not.',
        'I am not sure.',
        'The sign is pointing to yes.',
        'I really doubt it.',
        'Undoubtedly.',
        'Yes.',
        'Yes – definitely.',
        'You can trust it.'
    ]
    answer = random.choice(responses)
    embed = discord.Embed(color=0x000000)
    embed.add_field(name="**Question:**", value=f"```{question}```", inline=False)
    embed.add_field(name="**Answer:**", value=f"```{answer}```", inline=False)
    embed.set_author(name="8 Ball", icon_url="https://media.discordapp.net/attachments/910296097656815649/912066570073833512/8ball_moshed.gif") 
    await ctx.send(embed=embed)

@bot.command()
async def cat(ctx):
    r = requests.get("https://some-random-api.ml/img/cat").json()
    embed = discord.Embed(color=0x5c5c8a)
    embed.set_author(name="Here's the cat that you requested, it's pretty!", icon_url="https://i.stack.imgur.com/DTCra.png") 
    embed.set_image(url=str(r["link"]))
    await ctx.send(embed=embed)

@bot.command()
async def duck(ctx):
    r = requests.get("https://random-d.uk/api/random").json()
    embed = discord.Embed(color=0x5c5c8a)
    embed.set_author(name="Here's the duck that you asked for. It's super cute!", icon_url="https://media.istockphoto.com/vectors/duckling-simple-vector-icon-vector-id1045035708?k=20&m=1045035708&s=612x612&w=0&h=eUv26Njg6R9lGiDl4fLZccV2altzVDksirrftyrxYuo=") 
    embed.set_image(url=str(r["url"]))
    await ctx.send(embed=embed)

@bot.command()
async def dog(ctx):
    r = requests.get("https://some-random-api.ml/animal/dog").json()
    embed = discord.Embed(color=0xe0af4c)
    embed.set_author(name="Here's the dog you requested. It's really cute!", icon_url="https://www.publicdomainpictures.net/pictures/250000/velka/dog-puppy-illustration-cartoon.jpg") 
    embed.set_image(url=str(r["image"]))
    await ctx.send(embed=embed)

@bot.command()
async def panda(ctx):
    r = requests.get("https://some-random-api.ml/img/panda").json()
    embed = discord.Embed(color=0xffffff)
    embed.set_author(name="Here's the panda that you asked for, what a handsome one!", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
    embed.set_image(url=str(r["link"]))
    await ctx.send(embed=embed)

@bot.command()
async def meme(ctx):
    r = requests.get("https://some-random-api.ml/meme").json()
    embed = discord.Embed(color=0x006600)
    embed.set_author(name="Here's the meme that you requested XD", icon_url="https://freepngimg.com/thumb/internet_meme/3-2-troll-face-meme-png-thumb.png") 
    embed.set_image(url=str(r["image"]))
    await ctx.send(embed=embed)

@bot.command()
async def spoiler(ctx, *, mensaje):
  if mensaje == '@everyone' or mensaje == '@here':
      await ctx.send(f"||you can't do that little kid||")
  else:
    await ctx.send(f"||{mensaje}||")

@bot.command()
async def avatar(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author 
    embed = discord.Embed(color=0x13d420)
    embed.set_author(name=str(user), icon_url=user.avatar_url)     
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason="No reason provided."
    await ctx.guild.kick(member)
    await ctx.send(f'{member.mention} has been kicked for: {reason}')

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
  if reason==None:
    reason="No reason provided."
    await member.ban(reason = reason)
    await ctx.send(f'{member.mention} has been succesfully banned.')

@bot.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}.')
            return
        
@bot.command()
async def punch(ctx):
    embed = discord.Embed(
        colour=(discord.Colour.random()),
        description=f"{ctx.author.mention} {(random.choice(punch_msg))}"
        
        
    )
    embed.set_image(url=(random.choice(punch_gifs)))

    await ctx.send(embed=embed)
    
@bot.command()
async def kiss(ctx):
    embed = discord.Embed(
        colour=(discord.Colour.random()),
        description=f"{ctx.author.mention} {(random.choice(kiss_msg))}"
        
        
    )
    embed.set_image(url=(random.choice(kiss_gifs)))

    await ctx.send(embed=embed)
    

@bot.command()
async def play(ctx):
    embed = discord.Embed(
        colour=(discord.Colour.random()),
        description=f"{ctx.author.mention} {(random.choice(play_msg))}"
        
        
    )
    embed.set_image(url=(random.choice(play_gifs)))

    await ctx.send(embed=embed)
    
@bot.command()
@commands.check(whitelist2)
async def invite(ctx, *, messageContents):
    link = await ctx.channel.create_invite(max_age = 300)
    message = link
    msg = "I've sent you an invite link to this server to your DMs."
    await ctx.message.author.send(message)
    
    await ctx.send(msg)
    
@bot.command()
@commands.check(whitelist2)
async def sname(ctx):
    message = ctx.guild.name
    msg = "I've sent you this server's name to your DMs."
    await ctx.message.author.send(message)
    
    await ctx.send(msg)
    
@bot.command()
async def kill(ctx):
    embed = discord.Embed(
        colour=(discord.Colour.random()),
        description=f"{ctx.author.mention} {(random.choice(kill_msg))}"
        
        
    )
    embed.set_image(url=(random.choice(kill_gifs)))

    await ctx.send(embed=embed)
    
@bot.command(pass_context=True)
@commands.check(whitelist2)
async def broadcast(ctx, *, msg):
    for server in bot.guilds:
        for channel in server.text_channels:
            try:
                await channel.send(msg)
            except Exception:
                continue
            else:
                break


  



bot.run(token)
