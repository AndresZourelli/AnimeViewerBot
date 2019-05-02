from accounts import token
import discord
import json
import datetime
from discord.ext import commands
data2 = json.load(open('data.json', 'r'))
userData = json.load(open('userData.json', 'r'))

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Logged on as', client.user)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.'):
        await message.channel.send('pong')
        for anime in data2['anime'][:5]:
            embed = discord.Embed(title=anime['title'],
                                  description=anime['description'],
                                  colour=discord.Colour.blue())
            embed.set_image(url=anime['image'])

            await message.channel.send(embed=embed)


@client.event
async def on_reaction_add(reaction, user):
    print(reaction, user, reaction.message)


######Run Code#####

client.run(token)