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

#place the cog files into the bot
bot.load_extension("cogs.utility")
bot.load_extension("cogs.fun")

#run the bot
bot.run(TOKEN)
