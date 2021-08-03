import discord
from discord.ext import commands

class Startup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self.bot))
        await self.bot.change_presence(status=discord.Status.dnd, activity = discord.Game(name = 'Command Prefix :'))

def setup(bot):
    bot.add_cog(Startup(bot))
