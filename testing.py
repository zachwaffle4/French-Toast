#bot.py | imports and stuff 
import discord
import os
from discord import channel
from discord.ext import commands
from discord.app import Option
from googlesearch import search
from pycord_components import Button
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
@bot.slash_command(guild_ids=[866756514996158474,899047123415343114],description="Searches Google.",aliases=["search","google"])
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
@bot.slash_command(guild_ids=[866756514996158474],description="What does Marlene say?")
async def marlene(ctx):
    await ctx.respond(":skull:")

#ping command
@bot.slash_command(guild_ids=[866756514996158474,899047123415343114],description="Tells the ping of the bot.")
async def ping(ctx):
    await ctx.respond(f'Pong! {bot.latency}')

#invicta's youmom command
@bot.slash_command(aliases=["urmum","urmom"],guild_ids=[866756514996158474,899047123415343114],description="What does Marlene say?")
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

#EVENT COMMAND GROUP

#define the command group
event = bot.command_group(
    "event","Commands related to events."
)

@event.command(guild_ids=[866756514996158474,899047123415343114],description="Creates an event!")
async def create(ctx, name: Option(str,"The name of the event.", required=True, default="Test"), channel: Option(channel,"The channel you want the event to be posted in.")):
    await channel.send(
        f"Would you like to be part of the {name} event? Click the button below if you are interested.", 
        components=[Button(label="I can join!",custom_id="joinButton")])

@bot.event
async def on_button_click(interaction):
    await interaction.respond(content="Button Clicked")

bot.run(TOKEN)