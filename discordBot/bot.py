import discord
from dbHanderl import databaseHandler

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        content = message.content
        if message.author == self.user:
            return
        if message.content.startswith('!'):
            await message.channel.send("User added")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
with open("discordBot\\token", 'r') as f:
    token = f.read()
client.run(token)
