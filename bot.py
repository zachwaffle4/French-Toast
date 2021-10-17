import discord
from discord.ext import commands
from googlesearch import search

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    print("InvictaBot is online!")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def find(ctx,arg:int,*, query):
    author = ctx.author.mention
    await ctx.channel.send(f"Here are the links related to your question {author} !") 
    async with ctx.typing(): 
        for j in search(query, tld="co.in", num=arg, stop=arg, pause=2):
            await ctx.send(f"\n:point_right: {j}") 
        for j in search(query, tld="co.in", num=5, stop=5, pause=2):
            await ctx.send(f"\n:point_right: {j}") 

bot.run("ODk0MDMxMTQ2NDI4NTM4OTAw.YVkFYw.lzXubZjNH2g9ZJ2YGLSpuE_68rk")