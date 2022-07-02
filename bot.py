#bot.py | imports and stuff 
import discord
import os
from discord import channel
from discord.ext import commands
from discord.commands import Option
from googlesearch import search
from dotenv import load_dotenv
from random import randint, choice
from datetime import datetime


from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Your Bot Is Ready"

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()
  
#dotenv my beloved and also the iniatlizing of the bot itself
load_dotenv()
bot = discord.Bot(debug_guilds=[866756514996158474,899047123415343114,992568762840653897])
TOKEN = os.getenv("TOKEN")

#readying and installation
#tells me the bot is online in the terminal
@bot.event
async def on_ready():
    print("Lucky Charm is online!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you."))

@bot.command(description="Sends the bot's latency.")
async def ping(ctx):
    await ctx.respond(f"Pong! Latency is {bot.latency}")

@bot.command(description="Asks an anonymous question to staff.")
async def ask(ctx,question: Option(str, "Enter your question.")):
    await ctx.respond(f"Your question ({question}) has been sent to staff.",ephemeral=True)
    channel = bot.get_channel(992569868509520002)
    await channel.send(f"{ctx.author} has sent a question reading {question}.")

bot.run(TOKEN)