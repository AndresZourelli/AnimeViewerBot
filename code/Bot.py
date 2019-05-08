from accounts import token
import discord
import json
from datetime import datetime
from discord.ext import commands
import asyncio
from pytz import timezone

data2 = json.load(open('data.json', 'r'))
userData = json.load(open('userData.json', 'r'))
if not userData['users']:
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
    elif str(reaction.emoji == '👍'):
        for users in userData['users']:
            if users['user'] == user.id:
                for message in reaction.message.embeds:
                    users['anime'].append(message.title)
    elif str(reaction.emoji == ':no_entry_sign:'):
        for users in userData['users']:
            if users['user'] == user.id:
                for message in reaction.message.embeds:
                    try:
                        for items in users['anime']:
                            if items == message.title:
                                items.remove(message.title)
                            await user.send('Anime successfully removed')
                    except:
                        await user.send("Anime not in list")
    else:
        print(reaction.emoji)
        return

    with open('userData.json', 'w') as outfile:
        json.dump(userData, outfile)


@client.command()
async def dm(ctx):
    user = client.get_user(138423304183611392)
    print(ctx.author)
    await user.send('ehllo')


@client.command()
async def myAnime(ctx):
    currentUser = ctx.message.author.id
    sendToUser = client.get_user(currentUser)
    for user in userData['users']:
        if currentUser == user['user']:
            await sendToUser.send(
                "Here are your the animes you are currently watching:")
            for item in user['anime']:
                for anime in data2['anime']:
                    if anime['title'] == item:
                        embed = discord.Embed(title=anime['title'],
                                              description=anime['description'],
                                              colour=discord.Colour.blue())
                        embed.set_image(url=anime['image'])
                        await sendToUser.send(embed=embed)


async def counts():
    while True:
        x = datetime.now()
        print(x.strftime("%A"), x.strftime("%H"), x.strftime("%M"),
              x.strftime("%S"))
        await asyncio.sleep(60)

        if x.strftime("%A") == 'Monday':
            for anime in data2['anime']:
                if anime['weekday'] == 'Monday':
                    time = anime['airTime'].split(',')
                    animeShow = time[2].split()[0]
                    tz = timezone('Asia/Kolkata')
                    asiaTime = datetime.now().replace(tzinfo=tz)
                    getTime = datetime.strptime(
                        str(asiaTime.hour) + ':' + str(asiaTime.minute),
                        '%H:%M').time()
                    showtime = datetime.strptime(animeShow, '%H:%M').time()
                    # demoTime = datetime.strptime('21:54', '%H:%M').time()

                    if getTime == showtime:
                        for user in userData['users']:
                            if anime['title'] in user['anime']:
                                user = client.get_user(int(user['user']))
                                embed = discord.Embed(
                                    title=anime['title'],
                                    description=anime['description'],
                                    colour=discord.Colour.blue())
                                embed.set_image(url=anime['image'])
                                embed.set_author(
                                    name='New Episode is about to be released!'
                                )
                                await user.send(embed=embed)

        if x.strftime("%A") == 'Tuesday':
            for anime in data2['anime']:
                if anime['weekday'] == 'Tuesday':
                    time = anime['airTime'].split(',')
                    animeShow = time[2].split()[0]
                    tz = timezone('Asia/Kolkata')
                    asiaTime = datetime.now().replace(tzinfo=tz)
                    getTime = datetime.strptime(
                        str(asiaTime.hour) + ':' + str(asiaTime.minute),
                        '%H:%M').time()
                    showtime = datetime.strptime(animeShow, '%H:%M').time()
                    # demoTime = datetime.strptime('21:54', '%H:%M').time()

                    if getTime == showtime:
                        for user in userData['users']:
                            if anime['title'] in user['anime']:
                                user = client.get_user(int(user['user']))
                                embed = discord.Embed(
                                    title=anime['title'],
                                    description=anime['description'],
                                    colour=discord.Colour.blue())
                                embed.set_image(url=anime['image'])
                                embed.set_author(
                                    name='New Episode is about to be released!'
                                )
                                await user.send(embed=embed)

        if x.strftime("%A") == 'Wednesday':
            for anime in data2['anime']:
                if anime['weekday'] == 'Wednesday':
                    time = anime['airTime'].split(',')
                    animeShow = time[2].split()[0]
                    tz = timezone('Asia/Kolkata')
                    asiaTime = datetime.now().replace(tzinfo=tz)
                    getTime = datetime.strptime(
                        str(asiaTime.hour) + ':' + str(asiaTime.minute),
                        '%H:%M').time()
                    showtime = datetime.strptime(animeShow, '%H:%M').time()
                    # demoTime = datetime.strptime('21:54', '%H:%M').time()

                    if getTime == showtime:
                        for user in userData['users']:
                            if anime['title'] in user['anime']:
                                user = client.get_user(int(user['user']))
                                embed = discord.Embed(
                                    title=anime['title'],
                                    description=anime['description'],
                                    colour=discord.Colour.blue())
                                embed.set_image(url=anime['image'])
                                embed.set_author(
                                    name='New Episode is about to be released!'
                                )
                                await user.send(embed=embed)

        if x.strftime("%A") == 'Thursday':
            for anime in data2['anime']:
                if anime['weekday'] == 'Thursday':
                    time = anime['airTime'].split(',')
                    animeShow = time[2].split()[0]
                    tz = timezone('Asia/Kolkata')
                    asiaTime = datetime.now().replace(tzinfo=tz)
                    getTime = datetime.strptime(
                        str(asiaTime.hour) + ':' + str(asiaTime.minute),
                        '%H:%M').time()
                    showtime = datetime.strptime(animeShow, '%H:%M').time()
                    # demoTime = datetime.strptime('21:54', '%H:%M').time()

                    if getTime == showtime:
                        for user in userData['users']:
                            if anime['title'] in user['anime']:
                                user = client.get_user(int(user['user']))
                                embed = discord.Embed(
                                    title=anime['title'],
                                    description=anime['description'],
                                    colour=discord.Colour.blue())
                                embed.set_image(url=anime['image'])
                                embed.set_author(
                                    name='New Episode is about to be released!'
                                )
                                await user.send(embed=embed)

        if x.strftime("%A") == 'Friday':
            for anime in data2['anime']:
                if anime['weekday'] == 'Friday':
                    time = anime['airTime'].split(',')
                    animeShow = time[2].split()[0]
                    tz = timezone('Asia/Kolkata')
                    asiaTime = datetime.now().replace(tzinfo=tz)
                    getTime = datetime.strptime(
                        str(asiaTime.hour) + ':' + str(asiaTime.minute),
                        '%H:%M').time()
                    showtime = datetime.strptime(animeShow, '%H:%M').time()
                    # demoTime = datetime.strptime('21:54', '%H:%M').time()

                    if getTime == showtime:
                        for user in userData['users']:
                            if anime['title'] in user['anime']:
                                user = client.get_user(int(user['user']))
                                embed = discord.Embed(
                                    title=anime['title'],
                                    description=anime['description'],
                                    colour=discord.Colour.blue())
                                embed.set_image(url=anime['image'])
                                embed.set_author(
                                    name='New Episode is about to be released!'
                                )
                                await user.send(embed=embed)

        if x.strftime("%A") == 'Saturday':
            for anime in data2['anime']:
                if anime['weekday'] == 'Saturday':
                    time = anime['airTime'].split(',')
                    animeShow = time[2].split()[0]
                    tz = timezone('Asia/Kolkata')
                    asiaTime = datetime.now().replace(tzinfo=tz)
                    getTime = datetime.strptime(
                        str(asiaTime.hour) + ':' + str(asiaTime.minute),
                        '%H:%M').time()
                    showtime = datetime.strptime(animeShow, '%H:%M').time()
                    # demoTime = datetime.strptime('21:54', '%H:%M').time()

                    if getTime == showtime:
                        for user in userData['users']:
                            if anime['title'] in user['anime']:
                                user = client.get_user(int(user['user']))
                                embed = discord.Embed(
                                    title=anime['title'],
                                    description=anime['description'],
                                    colour=discord.Colour.blue())
                                embed.set_image(url=anime['image'])
                                embed.set_author(
                                    name='New Episode is about to be released!'
                                )
                                await user.send(embed=embed)

        if x.strftime("%A") == 'Sunday':
            for anime in data2['anime']:
                if anime['weekday'] == 'Sunday':
                    time = anime['airTime'].split(',')
                    animeShow = time[2].split()[0]
                    tz = timezone('Asia/Kolkata')
                    asiaTime = datetime.now().replace(tzinfo=tz)
                    getTime = datetime.strptime(
                        str(asiaTime.hour) + ':' + str(asiaTime.minute),
                        '%H:%M').time()
                    showtime = datetime.strptime(animeShow, '%H:%M').time()
                    # demoTime = datetime.strptime('21:54', '%H:%M').time()

                    if getTime == showtime:
                        for user in userData['users']:
                            if anime['title'] in user['anime']:
                                user = client.get_user(int(user['user']))
                                embed = discord.Embed(
                                    title=anime['title'],
                                    description=anime['description'],
                                    colour=discord.Colour.blue())
                                embed.set_image(url=anime['image'])
                                embed.set_author(
                                    name='New Episode is about to be released!'
                                )
                                await user.send(embed=embed)


######Run Code#####
client.loop.create_task(counts())
client.run(token)