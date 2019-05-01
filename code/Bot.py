from accounts import token
import discord
import json
data2 = json.load(open('data.json', 'r'))


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('.'):
            await message.channel.send('pong')
            await message.channel.send(data2['anime'][:5])


######Run Code#####
client = MyClient()
client.run(token)