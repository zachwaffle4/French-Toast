#bot.py | imports and stuff 
import discord
import os
from discord import channel
from discord.ext import commands
from discord.commands import Option
from googlesearch import search
from pycord_components import Button
from dotenv import load_dotenv
from random import randint
from datetime import datetime

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

#EVENT COMMAND GROUP

#define the command group
event = bot.command_group(
    "event","Commands related to events."
)

@bot.command(guild_ids=[866756514996158474,899047123415343114],description="Creates an event!")
async def event(ctx, name: Option(str,"The name of the event.", required=True, default="Test"), channel: Option(discord.TextChannel,"The channel you want the event to be posted in.",required=True,default=None), date: Option(str, "The date of the event.",required=True,default=None),time: Option(str, "The time of the event.",required=True)):
    now = datetime.now()
    await ctx.respond(f"The event has been started in {channel}.")
    await channel.send(
        f"Would you like to be part of the {name} event? Click the button below if you are interested. The event will be hosted on {date} at {time}.", 
        components=[Button(label="I can join!")])

    interaction = await bot.wait_for("button_click",check=lambda i: i.component.label.startswith("Click"))
    await interaction.respond(content="Button Clicked")
    
@bot.command(guild_ids=[899047123415343114])
async def button(ctx):
    await ctx.send("This message has a button",
    components=[Button(label="this is a button",custom_id="button1")])

    interaction = await bot.wait_for(
        "button_click", check=lambda inter: inter.custom_id == "button1"
    )
    await interaction.respond(content="Button Clicked")

#embed testing
@bot.command(guild_ids=[866756514996158474,899047123415343114],description="Creates an embed!")
async def create(ctx, title: Option(str, "The title of the embed.",required=True),description: Option(str, "The description of the embed.",required=True)):
    embed = discord.Embed(title=title,description=description,color=000000)
    await ctx.respond(embed)


#help command
@bot.slash_command(guild_ids=[866756514996158474], description="Calls Kevin for help.")
async def help(ctx, need: Option(str, "What you need help with.",required=True,default="with life")):
    await ctx.respond(f"<@242490141309009920> we need help {need}!")

bot.run(TOKEN)