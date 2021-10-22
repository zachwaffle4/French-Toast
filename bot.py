#bot.py | imports and stuff 
import discord
import os
from discord.ext import commands
from discord.commands import Option
from pycord_components import Button
from googlesearch import search
from dotenv import load_dotenv
from random import randint

#dotenv my beloved and also the iniatlizing of the bot itself
load_dotenv()
bot = discord.Bot()
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

#invicta's marlene command
@bot.slash_command(guild_ids=[866756514996158474],description="What does have the team enjoy saying?")
async def marlene(ctx):
    await ctx.respond(":skull:")

#ping command
@bot.slash_command(guild_ids=[866756514996158474,899047123415343114],description="Tells the ping of the bot.")
async def ping(ctx):
    await ctx.respond(f'Pong! {bot.latency}')

#invicta's youmom command
@bot.slash_command(name="yourmom",guild_ids=[866756514996158474,899047123415343114],description="What does Michelle say?")
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
@bot.slash_command(guild_ids=[866756514996158474], description="Calls Kevin for help.")
async def help(ctx, need: Option(str, "What you need help with.",required=False,default="with life")):
    await ctx.respond(f"<@242490141309009920> we need help {need}!")

@bot.command(guild_ids=[866756514996158474,899047123415343114])
async def button(ctx):
    message = await ctx.send("This message has a button and a reaction 💀",
    components=[Button(label="this is a button",custom_id="button1")])
    await message.add_reaction("💀")

    interaction = await bot.wait_for(
        "button_click", check=lambda inter: inter.custom_id == "button1"
    )
    await interaction.respond(content="Button Clicked")
bot.run(TOKEN)
