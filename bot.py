#bot.py | imports and stuff 
import discord
import os
from discord.ext import commands
from googlesearch import search
from dotenv import load_dotenv

#dotenv my beloved and also the iniatlizing of the bot itself
load_dotenv()
bot = commands.Bot(command_prefix=';')
TOKEN = os.getenv("TOKEN")

#tells me the bot is online in the terminal
@bot.event
async def on_ready():
    print("InvictaBot is online!")

#hello command and hello slash command
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.slash_command(guild_ids=[866756514996158474])
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

#ping command
@bot.command()
async def ping(ctx):
    await ctx.send("pong")

#find command
@bot.command()
async def find(ctx,arg:int,*, query):
    author = ctx.author.mention
    await ctx.channel.send(f"Here are the links related to your question {author} !") 
    async with ctx.typing(): 
        for j in search(query, tld="co.in", num=arg, stop=arg, pause=2):
            await ctx.send(f"\n:point_right: {j}") 
        for j in search(query, tld="co.in", num=5, stop=5, pause=2):
            await ctx.send(f"\n:point_right: {j}") 

bot.run(TOKEN)