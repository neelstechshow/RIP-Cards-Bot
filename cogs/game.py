import random
import discord
from discord.ext import commands
import asyncio
import time

player1 = None


def hasWon(playersList):
    if len(playersList) == 1:
        return f'{playersList[0].name} Has Won!'
    else:
        return 'False'


def isDead(playersList):
    take_out = []
    playersList = list(playersList)
    for x in playersList:
        if int(x.health) <= 0:
            take_out.append(x)

    if len(take_out) == 0:
        return 'FALSE'

    else:
        for i in take_out:
            remPlayer = i
            playersList.remove(i)
        return remPlayer


def attack(playersList, user1, attackedPlayerChoice):
    user2 = playersList[attackedPlayerChoice]
    attack = random.choice(user1.attackList)
    attackVal = random.randint(1, 5)
    attackMulti = random.randint(1, 10)
    attackVal = attackVal * attackMulti
    user2.health -= attackVal
    return f'{user1.name} Has Attacked {user2.name}, with {attack} causing {user2.name} to lose {attackVal} health, this means that {user2.name} now has {user2.health} health'


class game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['generate', 'code', 'gen_code'])
    async def gencode(self, ctx):
        r = ''
        for i in range(15):
            r = r + str(random.randint(1, 9))

        embed = discord.Embed(title=r)
        await ctx.send(embed=embed)

    @commands.command(aliases=['newgame', 'new', 'game', 'nowgame', 'now_game', 'startgame', 'startnew'])
    async def new_game(self, ctx, code, *, seconds):

        players = []

        def check(msg):
            list1 = [msg.author.name, msg.channel]
            return list1

        alreadymade = True
        read = open("codes.txt", "r")
        for line in read:
            line1 = line.strip()
            if line1 == code:
                embed = discord.Embed(title='A game has already been made with this code! Create a new one!',
                                      color=0x00ff00)
                await ctx.send(embed=embed)
                alreadymade = False

        if alreadymade:
            file = open("codes.txt", "a")
            file.write(code)
            file.close()
            embed = discord.Embed(title=f'New game has been created enter the code: {code} to join the game!', color=0x00ff00)
            await ctx.send(embed=embed)
            start_time = time.time()
            while True:
                current_time = time.time()
                elapsed_time = current_time - start_time
                if elapsed_time > float(seconds):
                    break
                try:
                    join = await self.bot.wait_for('message', check=check, timeout=1)
                    health = random.randint(70, 100)
                    c = check(join)
                    if c[1] != ctx.channel:
                        break
                    if join.content == code:
                        user1 = player(c[0], health)
                        players.append(user1)

                except asyncio.TimeoutError:
                    pass

            x = 0
            a_file = open("codes.txt", "r")
            lines = a_file.readlines()
            a_file.close()

            new_file = open("codes.txt", "w")
            for line in lines:
                if line.strip("\n") != code:
                    new_file.write(line)
            new_file.close()

            embed = discord.Embed(title = 'LOBBY HAS ENDED MAY THE GAME BEGIN', color=discord.Color.from_rgb(255, 56, 83))
            while x <= len(players):
                dead = isDead(players)
                if dead != 'FALSE':
                    embed = discord.Embed(title='PLAYER HAS DIED!', description=f'{dead.name} Has Died! RIP ',
                                          color=0xff0000)
                    await ctx.send(embed=embed)
                    players.remove(dead)


                winner = hasWon(players)

                if winner != 'False':
                    embed = discord.Embed(title='We Have A Winner', description=winner, color=0x00ff00)
                    await ctx.send(embed=embed)
                    players = []
                    return
                try:
                    embed = discord.Embed(title=f"{players[x].name}'s Turn Please Enter Who You Would Like To Attack, You Have 20 Seconds!!", color = discord.Color.from_rgb(0, 255, 217))
                    await ctx.send(embed=embed)
                except:
                    continue
                while True:
                    try:
                        attacked = await self.bot.wait_for('message', check=check, timeout = 20)
                        c = check(attacked)
                        break
                    except:
                        continue
                if c[0] == players[x].name and c[1] == ctx.channel:
                    attack_person = attacked.content
                    if attack_person.startswith('<@!'):
                        attack_person = attack_person.replace("@", "")
                        attack_person = attack_person.replace("!", "")
                        attack_person = attack_person.replace(">", "")
                        attack_person = attack_person.replace("<", "")
                        attack_person = await self.bot.fetch_user(int(attack_person))
                        for i in range(len(players)):
                            if str(players[i].name) == str(attack_person.name):
                                attack_var = attack(players, players[x], i)
                                embed = discord.Embed(title='ATTACKED', description=attack_var, color=discord.Color.from_rgb(255, 56, 83))
                                await ctx.send(embed=embed)
                                break

                if x == len(players) - 1:
                    x = 0
                    continue
                x = x + 1


class player:
    def __init__(self, name, health):
        self.attackList = ['Pork Chop', ' Double Slap', 'Snipe', 'Roundhouse Kick', 'John Cena', 'Giggle Power',
                           'FUNNY KILL']
        self.name = name
        self.health = health


def setup(bot):
    bot.add_cog(game(bot))
