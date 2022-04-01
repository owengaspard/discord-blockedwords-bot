"""
Discord.py Blocked Words Bot
Created by Owen Gaspard under the MIT license
- Please take a look at my GitHub: https://github.com/owengaspard
- Star the repository if you found it helpful, and fork it if you make
  any changes that may be useful: https://github.com/owengaspard/discord-blockedwords-bot
    - Make sure you do NOT share your botToken file (add it to your gitignore)!

This is not the first bot I have made, but it is the first I am releasing publicly. Please
do not hesitate to content me if you find anything I missed.

This bot blocks words that you specify under the blockedWords variable.
Remember that when you add words, put them in quotes ("") and add a comma at
the end of it only if you are adding another word under it. Do not add a comma
if it is the last word in the list (Python doesn't care, but JSON files do care).
"""

import discord
from discord import Client, Intents
import os

client = discord.Client()

blockedWords = [
    "word1",
    "word2"
]

token = open("./botToken", "r").read()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for blocked words'))

@client.event
async def on_message(ctx): 
    print(f"{ctx.channel}: {ctx.author}: {ctx.author.name}: {ctx.content}")
    if any(x in ctx.content for x in blockedWords):
        await ctx.delete()

client.run(token)