import os
import discord

from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='!')


@client.command(aliases=['who'])
async def add(ctx,*,question):
    response = f'added {question}'

    
    await ctx.send(f'{response}')


client.run(TOKEN)