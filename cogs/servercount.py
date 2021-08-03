import discord
from discord.ext import commands

class servercount(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def servercount(self, ctx):
        embed = discord.Embed(title = f"I'm in {str(len(self.bot.guilds))} servers!", color = discord.Color.from_rgb(255, 255, 255))
        await ctx.send(embed=embed)
 
def setup(bot):
    bot.add_cog(servercount(bot))
