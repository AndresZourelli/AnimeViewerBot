from accounts import token
import discord
import json
import datetime
from discord.ext import commands
import asyncio
data2 = json.load(open('data.json', 'r'))
userData = json.load(open('userData.json', 'r'))
userData['users'] = []

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
    await client.process_commands(message)


@client.event
async def on_reaction_add(reaction, user):

    if str(reaction.emoji == '👍') and not any(
            int(userInfo.get('user', None)) == user.id
            for userInfo in userData['users']):

        for message in reaction.message.embeds:
            print(str(message.title), user)
            userData['users'].append({
                'user': user.id,
                'anime': [message.title]
            })
        print(userData)
    else:
        for users in userData['users']:
            if users['user'] == user.id:
                for message in reaction.message.embeds:
                    users['anime'].append(message.title)
        print(userData)

    with open('userData.json', 'w') as outfile:
        json.dump(userData, outfile)


@client.command()
async def dm(ctx):
    user = client.get_user(138423304183611392)
    print(ctx.author)
    await user.send('ehllo')


async def counts():
    while True:
        x = datetime.datetime.now()
        print(x.strftime("%A"), x.strftime("%H"), x.strftime("%M"),
              x.strftime("%S"))
        await asyncio.sleep(1)


######Run Code#####
client.loop.create_task(counts())
client.run(token)