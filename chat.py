#!/usr/bin/python3
import discord
#from discord import opus
from discord.ext import commands
from os import system as shell
from os import getpid as pid
from os import popen as sh
from os import chdir
import sys

try:
	with open("token.txt") as token:
		TOKEN = token.read().strip()

except FileNotFoundError:
	print("Bot Token not Detected - Error")
	sys.exit(1)

description = "Message Listener Bot"
ignore_bots = False #Change to True to get messages from bots
bot = commands.Bot(command_prefix='None', description=description)

@bot.event
async def on_ready():
    print('Listener Bot Active.\nEnter Username [Optional]: ')


#Listen for messages
@bot.event
async def on_message(message):
    if message.author.bot == ignore_bots:
        print("#" + message.channel.name + " | " + message.author.name + ": " + message.content) # Get messages in format: #channel | user: message

bot.run(TOKEN)
