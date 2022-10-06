#bot.py | imports and stuff 
import discord
import os
from discord import channel
from discord.ext import commands
from discord.commands import Option
from discord.ui import *
from googlesearch import search
from dotenv import load_dotenv
from random import randint, choice
from datetime import datetime
import openai
  
#dotenv my beloved and also the iniatlizing of the bot itself
load_dotenv()
bot = discord.Bot(debug_guilds=[866756514996158474,899047123415343114,992568762840653897,787120261437718539])
TOKEN = os.getenv("TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")

#readying and installation
#tells me the bot is online in the terminal
@bot.event
async def on_ready():
    print("Lucky Charm is online!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you."))

@bot.command(description="Sends the bot's latency.")
async def ping(ctx):
    await ctx.respond(f"Pong! Latency is {bot.latency}")

@bot.command(description="Generates a result based on the prompt.")
async def prompt(ctx,promptai: Option(str,"Your prompt for the AI"),temp: Option(float,"The risk level of your query from 0 to 1.",required=False,default=.5)):
    try:
        if temp > 1:
            temp = 1
        elif temp < 0:
            temp = 0
        response = openai.Completion.create(
          model="text-davinci-002",
          prompt=promptai,
          temperature=temp,
          max_tokens=100
         )
        await ctx.respond(response.choices[0].text)  
    except:
          await ctx.respond("I am currently unavailable.")
  
bot.run(TOKEN)