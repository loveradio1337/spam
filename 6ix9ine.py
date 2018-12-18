import discord
from discord.ext.commands import bot
from discord.ext import commands
import random
import asyncio
import time
print("Bot Is Online! And Ready To Spam")

@bot.event
async def on_ready():
    print("Bot Is Online! And Ready To Spam")
	
	
##SPAM COMMAND##
	@bot.command(pass_context=True)
	async def spam(ctx):
	    while True:
	        await bot.say("mv!ping")
	        await bot.say("fuck")
	        await bot.say("fuck")
	        await bot.say("fuck")
	        await bot.say("mv!ping")
	        await bot.say("fuck")
	        await bot.say("fuck")
	        await bot.say("fuck")
	        await bot.say("mv!ping")
	        await bot.say("fuck")
	        await bot.say("fuck")
	        await bot.say("fuck")
	        await bot.say("mv!ping")
	
	
	bot.run(os.environ['Token'])
