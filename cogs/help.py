import discord
from discord.ext import commands
 
class help(commands.Cog):
   def __init__(self, bot):
       self.bot = bot
 
   @commands.command()
   async def help(self, ctx):
       embed = discord.Embed(title='HELP!', description='Command Prefix Is :', color = discord.Color.from_rgb(0, 191, 178))
       embed.add_field(name = '\u200b', value = '\u200b', inline=False)
       embed.add_field(name='How To Play', value = "If you want to join an already created game type the game code in the channel where it was started, if you want to create a new game refer to How To Start A New Game. After the lobby time set for the game is over, the game will start. When your name is called, you have to choose a player to attack and the person will get damage accordingly the last person standing wins.", inline=False)
       embed.add_field(name = '\u200b', value = '\u200b', inline=False)
       embed.add_field(name='How To Create A New Game', value=':newgame code lobby_time. you have to choose a Unique Code That Members Can Join With And A Time Limit Of How Long The Lobby Will Last. If you cannot think of a code that has not already been taken. use our :gencode command', inline=False)
       embed.add_field(name = '\u200b', value = '\u200b', inline=False)
       embed.add_field(name='If you cannot think of a code that has not already been taken.', value='use our :gencode command', inline=False)
       embed.add_field(name = '\u200b', value = '\u200b', inline=False)
       embed.add_field(name = "Invite Me: https://ripcards.netlify.app/", value='\u200b', inline=True)
       embed.add_field(name = 'Check out my YouTube channel: https://www.youtube.com/c/programmingdoneright', value='\u200b', inline=True)
       embed.add_field(name='Join our discord server: https://discord.com/invite/UbWFK4je7B', value='\u200b', inline=True)
 
       await ctx.send(embed=embed)
 
 
def setup(bot):
   bot.add_cog(help(bot))

