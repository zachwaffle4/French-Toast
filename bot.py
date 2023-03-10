#bot.py | imports and stuff 
import discord
import os
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
print(TOKEN)
openai.api_key = os.getenv("API_KEY")

#readying and installation
#tells me the bot is online in the terminal
@bot.event
async def on_ready():
    print("French Toast is online!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you."))

@bot.slash_command(description="Sends the bot's latency.")
async def ping(ctx):
    await ctx.respond(f"Pong! Latency is {bot.latency}")

message = [{"role": "system", "content": "talk like you're a human, not an AI language model"}]

@bot.slash_command(description="Generates a result based on the prompt.")
async def prompt(ctx,promptai: Option(str,"Your prompt for the AI"),temp: Option(float,"The risk level of your query from 0 to 1.",required=False,default=.5)):
    try:
        if temp > 1:
            temp = 1
        elif temp < 0:
            temp = 0
        message.append({"role": "user", "content": promptai})
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=message,
          temperature=temp,
          max_tokens=100
         )
        message.append(response.choices[0].message)
        await ctx.respond(response.choices[0].message['content'])  
    except Exception as e:
        print(e)
        await ctx.respond("I am currently unavailable.")
  
bot.run(TOKEN)