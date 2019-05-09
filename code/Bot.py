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

    if message.content.startswith('.mon'):
        await message.channel.send(
            "Please use 👍 to add an anime and 🚫 to delete it from your list")
        for anime in data2['anime']:
            if anime['weekday'] == 'Monday':
                embed = discord.Embed(title=anime['title'],
                                      description=anime['description'],
                                      colour=discord.Colour.blue())
                embed.set_image(url=anime['image'])

                await message.channel.send(embed=embed)

    if message.content.startswith('.tues'):
        await message.channel.send(
            "Please use 👍 to add an anime and 🚫 to delete it from your list")
        for anime in data2['anime']:
            if anime['weekday'] == 'Tuesday':
                embed = discord.Embed(title=anime['title'],
                                      description=anime['description'],
                                      colour=discord.Colour.blue())
                embed.set_image(url=anime['image'])

                await message.channel.send(embed=embed)

    if message.content.startswith('.wed'):
        await message.channel.send(
            "Please use 👍 to add an anime and 🚫 to delete it from your list")
        for anime in data2['anime']:
            if anime['weekday'] == 'Wednesday':
                embed = discord.Embed(title=anime['title'],
                                      description=anime['description'],
                                      colour=discord.Colour.blue())
                embed.set_image(url=anime['image'])

                await message.channel.send(embed=embed)

    if message.content.startswith('.thurs'):
        await message.channel.send(
            "Please use 👍 to add an anime and 🚫 to delete it from your list")
        for anime in data2['anime']:
            if anime['weekday'] == 'Thursday':
                embed = discord.Embed(title=anime['title'],
                                      description=anime['description'],
                                      colour=discord.Colour.blue())
                embed.set_image(url=anime['image'])

                await message.channel.send(embed=embed)

    if message.content.startswith('.fri'):
        await message.channel.send(
            "Please use 👍 to add an anime and 🚫 to delete it from your list")
        for anime in data2['anime']:
            if anime['weekday'] == 'Friday':
                embed = discord.Embed(title=anime['title'],
                                      description=anime['description'],
                                      colour=discord.Colour.blue())
                embed.set_image(url=anime['image'])

                await message.channel.send(embed=embed)

    if message.content.startswith('.sat'):
        await message.channel.send(
            "Please use 👍 to add an anime and 🚫 to delete it from your list")
        for anime in data2['anime']:
            if anime['weekday'] == 'Saturday':
                embed = discord.Embed(title=anime['title'],
                                      description=anime['description'],
                                      colour=discord.Colour.blue())
                embed.set_image(url=anime['image'])

                await message.channel.send(embed=embed)

    if message.content.startswith('.sun'):
        await message.channel.send(
            "Please use 👍 to add an anime and 🚫 to delete it from your list")
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

    if (reaction.emoji == '👍') and not any(
            int(userInfo.get('user', None)) == user.id
            for userInfo in userData['users']):
        for message in reaction.message.embeds:
            print(str(message.title), user)
            userData['users'].append({
                'user': user.id,
                'anime': [message.title]
            })

    elif (reaction.emoji == '👍'):
        for users in userData['users']:
            if users['user'] == user.id:
                for message in reaction.message.embeds:
                    users['anime'].append(message.title)

    elif (reaction.emoji == '🚫'):
        for users in userData['users']:
            if users['user'] == user.id:
                for message in reaction.message.embeds:
                    try:
                        for items in users['anime']:
                            if items == message.title:
                                users['anime'].remove(message.title)
                                await user.send('Anime successfully removed')
                    except:
                        await user.send("Anime not in list")
    else:
        await user.send(
            f"{reaction.emoji} is not the correct reaction for this bot")
        await user.send("Please use 👍 to add an anime and 🚫 to delete it")

    with open('userData.json', 'w') as outfile:
        json.dump(userData, outfile)


@client.command()
async def myAnime(ctx):
    currentUser = ctx.message.author.id
    sendToUser = client.get_user(currentUser)
    for user in userData['users']:
        if currentUser == user['user']:
            await sendToUser.send("Here are the animes currently in your list:"
                                  )
            for item in user['anime']:
                for anime in data2['anime']:
                    if anime['title'] == item:
                        embed = discord.Embed(title=anime['title'],
                                              description=anime['description'],
                                              colour=discord.Colour.purple())
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
                                    colour=discord.Colour.red())
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
                                    colour=discord.Colour.red())
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
                                    colour=discord.Colour.red())
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
                                    colour=discord.Colour.red())
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
                                    colour=discord.Colour.red())
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
                                    colour=discord.Colour.red())
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
                                    colour=discord.Colour.red())
                                embed.set_image(url=anime['image'])
                                embed.set_author(
                                    name='New Episode is about to be released!'
                                )
                                await user.send(embed=embed)


######Run Code#####
client.loop.create_task(counts())
client.run(token)