#bot.py | imports and stuff 
import discord
import os
from discord import channel
from discord.ext import commands
from googlesearch import search
from discord.commands import Option
from dotenv import load_dotenv
from random import randint, choice
from datetime import datetime

#dotenv my beloved and also the iniatlizing of the bot itself
load_dotenv()
bot = discord.Bot(command_prefix='&')
TOKEN = os.getenv("TOKEN")

quoteList = ["''It will get worse'' - Arash", "''Be yourself; everyone else is already taken. ''- Oscar Wilde", "''You've gotta dance like there's nobody watching, Love like you'll never be hurt, Sing like there's nobody listening, And live like it's heaven on earth' - William W. Purkey", "''Be the change you wish to see in this world'' - Ghandi", "''You are stupid' - Rich Chen", "''Live as if you were to die tomorrow. Learn as if you were to life forever'' - Ghandi", "''Darkness cannot drive out darkness; only light can. Hate cannot drive out hate; only love can'' -  Martin Luther King Jr.", "''Without music life would be a mistake'' ―  Friedrich", "''We accept the love we think we should deserve'' - Stephen Chbosky", "''Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.'' - Marilyn Monroe", "''There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.'' - Alber Einstein", "''We are all in the gutter, but some of us are looking at the stars.'' - Oscar Wilde", "''Fairy tales are more than true: not because they tell us that dragons exist, but because they tell us that dragons can be beaten.'' - Neil Gaiman", "''Yesterday is history, tomorrow is a mystery, today is a gift of God, which is why we call it the present.'' - Bill Keine", "''I have not failed. I've just found 10,000 ways that won't work.'' - Thomas Edison", "''Out of the mountain of despair, a stone of hope.'' - Martin Luther King Jr.", "''When you've got a dream you've got to grab it and never let it go.'' - Audrey Hepburn", "''The bad news is time flies. The good news is you’re the pilot.'' - Michael Altshuler", "''This life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good part is you get to decide how you're going to mess it up. Girls will be your friends - they'll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything - they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn't mean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.'' - Marilyn Monroe", "''There is no greater agony than bearing an untold story inside you.'' - Maya Angelou", "''Everything you can imagine is real.'' - Pable Picasso", "''You can never get a cup of tea large enough or a book long enough to suit me.'' - C.S. Lewis", "''Life isn't about finding yourself. Life is about creating yourself.'' - George Bernard Shaw", "''To the well-organized mind, death is but the next great adventure.'' - J.K. Rowling"]

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
@bot.slash_command(guild_ids=[866756514996158474,899047123415343114],description="Searches Google.")
async def google(ctx,*,Search: Option(str, "What you want to search for.",required=True,default='test'),amount: Option(int, "The amount of results you want.", required=False,default=5)):
    query = Search
    author = ctx.author.mention
    await ctx.respond(f"Here are the links related to your question!") 
    async with ctx.typing(): 
        for j in search(query, tld="co.in", num=amount, stop=amount, pause=2):
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
    )
    interaction = await bot.wait_for("button_click",check=lambda i: i.component.label.startswith("Click"))
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

@bot.command()
async def inspire(ctx, amount: int):
    for x in range(amount):
        await ctx.respond(choice(quoteList))


        
bot.run(TOKEN)