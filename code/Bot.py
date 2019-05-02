from accounts import token
import discord
import json
import datetime
data2 = json.load(open('data.json', 'r'))
userData = json.load(open('userData.json', 'r'))


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('.'):
            await message.channel.send('pong')
            for anime in data2['anime'][:5]:
                embed = discord.Embed(title=anime['title'],
                                      description=anime['description'],
                                      colour=discord.Colour.blue())
                embed.set_image(url=anime['image'])

                await message.channel.send(embed=embed)


######Run Code#####
client = MyClient()
client.run(token)