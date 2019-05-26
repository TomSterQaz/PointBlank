import discord
import random
import json
from discord.ext import commands

client = commands.Bot(command_prefix = '>')

@client.event
async def on_ready():
    print('Ready for action!')

@client.command()
async def ping(ctx):
    await ctx.send('Ping: {:0.2f} ms'.format(client.latency * 1000))

@client.command()
async def coinflip(ctx):
    choice = random.choice(['Heads', 'Tails'])
    await ctx.send("It's {}!".format(choice))

@client.command()
async def clear(ctx, amount = 3):
    await ctx.channel.purge(limit = amount)


client.run('NTIxODYyMTI2NzQzMDYwNDkx.XMc4Dw.KRT39YgXQlXbB2Pd8FsAJrqwHKU')
