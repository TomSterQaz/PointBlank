import discord
import json
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '>')

print(discord.__version__)

@client.event
async def on_ready():
    print('Ready for action!')

@client.command()
async def ping(ctx):
    await ctx.send('Ping: {:0.2f} ms'.format(client.latency * 1000))

@client.command()
async def get_msg(ctx, num):
    with open('DataFiles/Test.JSON', 'r') as messages:
        for item in messages[0:int(num)]:
            await ctx.send(item)

@client.command()
async def coinflip(ctx):
    choice = random.choice(['Heads', 'Tails'])
    await ctx.send("It's {}!".format(choice))

@client.command()
async def quit(ctx):
    pass



client.run('NTIxODYyMTI2NzQzMDYwNDkx.XMc4Dw.KRT39YgXQlXbB2Pd8FsAJrqwHKU')
