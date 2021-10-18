#bot.py | imports and stuff 
import discord
import os
from discord.ext import commands
from discord.app import Option
from googlesearch import search
from dotenv import load_dotenv

#dotenv my beloved and also the iniatlizing of the bot itself
load_dotenv()
bot = commands.Bot(command_prefix=["i","I","eye","Eye","EYE"])
TOKEN = os.getenv("TOKEN")

#tells me the bot is online in the terminal
@bot.event
async def on_ready():
    print("InvictaBot is online!")

#hello command
@bot.slash_command(guild_ids=[866756514996158474])
async def hello(ctx, name: Option(str, "The person you want to say hello to.", required=False,default=None)):
    await ctx.respond(f"Hello, {name}!")

#ping command
@bot.slash_command(guild_ids=[866756514996158474])
async def ping(ctx):
    await ctx.respond("pong")

#find command
'''@bot.slash_command(guild_ids=[866756514996158474])
async def find(ctx,search: Option(str, "What you want to search for.",required=True,default='test'),amount: Option(int, "The amount of results you want.", required=False,default=5)):
    author = ctx.author.mention
    await ctx.respond(f"Here are the links related to your question!") 
    async with ctx.typing(): 
        for j in search(search, tld="co.in", num=amount, stop=amount, pause=2):
            await ctx.send(f"\n:point_right: {j}")'''

@bot.slash_command(guild_ids=[866756514996158474])
async def eye(ctx):
    await ctx.respond(":eye:")

@bot.command(name="-")
async def i(ctx):
    await ctx.send(':eye:-')

@bot.slash_command(guild_ids=[866756514996158474])
async def marlene(ctx):
    await ctx.respond(":skull:")

bot.run(TOKEN)