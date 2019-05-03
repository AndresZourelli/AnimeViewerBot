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

    if message.content.startswith('.monday'):
        for anime in data2['anime']:
            if anime['weekday'] == 'Monday':
                embed = discord.Embed(title=anime['title'],
                                      description=anime['description'],
                                      colour=discord.Colour.blue())
                embed.set_image(url=anime['image'])

                await message.channel.send(embed=embed)

    if message.content.startswith('.tuesday'):
        for anime in data2['anime']:
            if anime['weekday'] == 'Tuesday':
                embed = discord.Embed(title=anime['title'],
                                      description=anime['description'],
                                      colour=discord.Colour.blue())
                embed.set_image(url=anime['image'])

                await message.channel.send(embed=embed)

    if message.content.startswith('.wednesday'):
        for anime in data2['anime']:
            if anime['weekday'] == 'Wednesday':
                embed = discord.Embed(title=anime['title'],
                                      description=anime['description'],
                                      colour=discord.Colour.blue())
                embed.set_image(url=anime['image'])

                await message.channel.send(embed=embed)

    if message.content.startswith('.thursday'):
        for anime in data2['anime']:
            if anime['weekday'] == 'Thursday':
                embed = discord.Embed(title=anime['title'],
                                      description=anime['description'],
                                      colour=discord.Colour.blue())
                embed.set_image(url=anime['image'])

                await message.channel.send(embed=embed)

    if message.content.startswith('.friday'):
        for anime in data2['anime']:
            if anime['weekday'] == 'Friday':
                embed = discord.Embed(title=anime['title'],
                                      description=anime['description'],
                                      colour=discord.Colour.blue())
                embed.set_image(url=anime['image'])

                await message.channel.send(embed=embed)

    if message.content.startswith('.saturday'):
        for anime in data2['anime']:
            if anime['weekday'] == 'Saturday':
                embed = discord.Embed(title=anime['title'],
                                      description=anime['description'],
                                      colour=discord.Colour.blue())
                embed.set_image(url=anime['image'])

                await message.channel.send(embed=embed)

    if message.content.startswith('.sunday'):
        for anime in data2['anime']:
            if anime['weekday'] == 'Sunday':
                embed = discord.Embed(title=anime['title'],
                                      description=anime['description'],
                                      colour=discord.Colour.blue())
                embed.set_image(url=anime['image'])

                await message.channel.send(embed=embed)


@client.event
async def on_reaction_add(reaction, user):
    print(reaction, user, reaction.message.author)


######Run Code#####

client.run(token)