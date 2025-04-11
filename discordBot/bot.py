import discord
from savesF.dbHanderl import databaseHandler

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
with open("files\\token", 'r') as f:
    token = f.read()
client.run(token)
