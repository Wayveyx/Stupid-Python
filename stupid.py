import discord
import os
import time
from discord.ext import commands

bot = commands.Bot(description="Stupid bot rewritten in Python", command_prefix="sp;")
bot.remove_command('help')
@bot.event
async def on_ready():
    print('c:')
    game = discord.Game("with knives")
    await bot.change_presence(status=discord.Status.online, activity=game)

#Couldn't figure out how to put this in a cog lol
@bot.command(pass_context = True) 
async def ping(ctx):
    ''' 
    Pong! See the bot's latency.
    '''
    await ctx.send(f"Pong! Latency: {bot.latency}")

#Bot Owner only commands
def isme(ctx):
    return ctx.message.author.id == 363474941523263518

@bot.command()
@commands.check(isme)
async def load(ctx, ext):
    '''
    Load a Category.
    '''
    bot.load_extension(f'cogs.{ext}')
    await ctx.send(f"Extension `{ext}` has been loaded.")

@bot.command()
@commands.check(isme)
async def unload(ctx, ext):
    '''
    Unload a Category.
    '''
    bot.unload_extension(f'cogs.{ext}')
    await ctx.send(f"Extension `{ext}` has been unloaded.")

@bot.command()
@commands.check(isme)
async def reload(ctx, ext):
    bot.unload_extension(f"cogs.{ext}")
    time.sleep(2)
    bot.load_extension(f"cogs.{ext}")
    await ctx.send(f"Extension `{ext}` has been reloaded.")

for filename in os.listdir('./cogs'):
    if filename.endswith('py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run("token")