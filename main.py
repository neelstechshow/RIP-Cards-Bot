import discord
from discord.ext import commands
from webserver import webserver
import os

bot = commands.Bot(command_prefix=':')
bot.remove_command('help')


for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

webserver()
token = os.environ.get('Token')
bot.run(token)
