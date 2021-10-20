#bot.py | imports and stuff 
import discord
import os
from discord.ext import commands
from discord.app import Option
from googlesearch import search
from dotenv import load_dotenv
from random import randint

#dotenv my beloved and also the iniatlizing of the bot itself
load_dotenv()
bot = commands.Bot(command_prefix=["i","I","eye","Eye","EYE"])
TOKEN = os.getenv("TOKEN")

#tells me the bot is online in the terminal
@bot.event
async def on_ready():
    print("InvictaBot is online!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you."))

#hello command
@bot.slash_command(guild_ids=[866756514996158474,899047123415343114],description="Says hi to you or someone else!")
async def hello(ctx, name: Option(str, "The person you want to say hello to.", required=False,default="friend")):
    await ctx.respond(f"Hello, {name}!")

#find command
@bot.slash_command(guild_ids=[866756514996158474,899047123415343114],description="Searches Google.",alias=["search","google"])
async def find(ctx,*,search: Option(str, "What you want to search for.",required=True,default='test'),amount: Option(int, "The amount of results you want.", required=False,default=5)):
    author = ctx.author.mention
    await ctx.respond(f"Here are the links related to your question!") 
    async with ctx.typing(): 
        for j in search(search, tld="co.in", num=amount, stop=amount, pause=2):
            await ctx.send(f"\n:point_right: {j}")

#eye command
@bot.slash_command(guild_ids=[866756514996158474,899047123415343114],description="Replies with the Eye emoji!")
async def eye(ctx):
    await ctx.respond(":eye:")

#invicta's i- finder
@bot.command(name="-",guild_ids=866756514996158474)
async def i(ctx):
    await ctx.send(':eye:')

#invicta's marlene command
@bot.slash_command(guild_ids=[866756514996158474],description="What does Marlene say?")
async def marlene(ctx):
    await ctx.respond(":skull:")

#ping command
@bot.slash_command(guild_ids=[866756514996158474,899047123415343114],description="Tells the ping of the bot.")
async def ping(ctx):
    await ctx.respond(f'Pong! {bot.latency}')

#invicta's youmom command
@bot.slash_command(guild_ids=[866756514996158474,899047123415343114],description="What does Marlene say?")
async def yourmom(ctx):
    x = randint(0,4)
    if x == 0:
        await ctx.respond("Your mother.")
    if x == 1:
        await ctx.respond("ur mum")
    if x == 2: 
        await ctx.respond("haha L")
    if x == 3:
        await ctx.respond("https://tenor.com/bID8C.gif")

 #help command
@bot.slash_command(guild_ids=866756514996158474, description="Calls Kevin for help.")
async def help(ctx):
    await ctx.respond(<@242490141309009920> we need help!")

bot.run(TOKEN)
