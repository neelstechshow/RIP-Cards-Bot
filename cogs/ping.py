import discord
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if str(message.content) == '<@!844066483982172200>':
            embed = discord.Embed(title='My Prefix Is :', color = discord.Color.from_rgb(0, 191, 178))
            await message.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(ping(bot))
