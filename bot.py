#bot.py | imports and stuff 
import discord
import os
from discord.ext import commands
from discord.commands import Option
from pycord_components import Button
from googlesearch import search
from dotenv import load_dotenv
from random import *
from PyDictionary import PyDictionary
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint

#initializes the bot, the token, the dictionary, giphy, 
load_dotenv()
bot = discord.Bot()
TOKEN = os.getenv("TOKEN")
GIPHY = os.getenv("GIPHY")
dictionary=PyDictionary()
api_instance = giphy_client.DefaultApi()
config = {
    'api_key': GIPHY,  # Giphy API Key,
    'limit': 1,
    'rating': 'g'
}


#tells me the bot is online in the terminal
@bot.event
async def on_ready():
    print("InvictaBot is online!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for / commands."))



#find command
@bot.slash_command(guild_ids=[866756514996158474,899047123415343114],description="Searches Google.",alias=["search","google"])
async def find(ctx,*,query: Option(str, "What you want to search for.",required=True,default='test'),amount: Option(int, "The amount of results you want.", required=False,default=2)):
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
@bot.slash_command(guild_ids=[866756514996158474],description="What does have the team enjoy saying?")
async def marlene(ctx):
    await ctx.respond(":skull:")

#invicta's youmom command
'''@bot.slash_command(guild_ids=[866756514996158474,899047123415343114],description="What does Marlene say?")
async def yourmom(ctx):
    choiceyourmom = ["Your mother.","ur mum","haha L","https://tenor.com/bID8C.gif"]
    responseyourmom = randint(0,len(choiceyourmom))
    resultyourmom=choiceyourmom(responseyourmom)
    ctx.respond(resultyourmom)'''

#help command
@bot.slash_command(guild_ids=[866756514996158474], description="Calls Kevin for help.")
async def help(ctx, need: Option(str, "What you need help with.",required=False,default="with life")):
    await ctx.respond(f"<@242490141309009920> we need help {need}!")

@bot.command(guild_ids=[866756514996158474,899047123415343114])
async def button(ctx):
    message = await ctx.send("This message has a button and a reaction 💀",
    components=[Button(label="this is a button",custom_id="button1")])

    interaction = await bot.wait_for(
        "button_click", check=lambda inter: inter.custom_id == "button1"
    )
    await interaction.respond(content="Button Clicked")
    await message.add_reaction("💀")
#ping command
@bot.slash_command(guild_ids=[866756514996158474,899047123415343114],description="Tells the ping of the bot.")
async def ping(ctx,bot):
    await ctx.respond(f'Pong! The bot is currently running {bot.latency} behind.')

#yeetsleep
@bot.slash_command(guild_ids=[866756514996158474,899047123415343114],description="Makes the person go to bed.")
async def yeetsleep(ctx,name: Option(str, "The person who needs to go to sleep.",required=True)):
    await ctx.respond(f"Sleep is good and important, {name}.")

#thesaurus series
word = bot.command_group("word","Commands related to words.")
@bot.command(guild_ids=[866756514996158474,899047123415343114],description="Defines the word.")
async def define(ctx,word: Option(str,"The word you want to define.",required=True)):
    await ctx.respond(dictionary.meaning(word))

@bot.command(guild_ids=[866756514996158474,899047123415343114],description="Defines the word.")
async def synonym(ctx,word: Option(str,"The word you want the synonym.",required=True)):
    await ctx.respond(dictionary.synonym(word))

@bot.command(guild_ids=[866756514996158474,899047123415343114],description="Defines the word.")
async def antonym(ctx,word: Option(str,"The word you want the opposite of.",required=True)):
    await ctx.respond(dictionary.antonym(word))

bot.load_extension("cogs.utility")  # <--- This single line of code to be precise
print(dictionary.antonym("test"))

@bot.command(name='8ball',guild_ids=[866756514996158474,899047123415343114],description="Asks the Magic 8 Ball a question.")
async def eightBall(ctx,question: Option(str,"What you want to ask the 8ball.")):
    response8ball =['Without a doubt.','Outlook good.','Better not tell you now.','Cannot predict now.','My reply is no.','Outlook not so good.']
    choice=randint(0,len(response8ball))
    result=response8ball(choice)
    await ctx.respond(result)

bot.run(TOKEN)
