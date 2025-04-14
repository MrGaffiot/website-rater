import discord
from dbHanderl import databaseHandler
import packageGenerator.generate as generate
#await message.channel.send("User added")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        content = message.content
        if message.author == self.user:
            return
        if message.content.startswith('!'):
            if message.content.startswith('!generate'):
                try:
                    generate.makePackage(generate.makePackageInfo(int(message.content.split(' ')[1])))
                    await message.channel.send(f"Package  with length {message.content.split(' ')[1]}generated")
                    await message.channel.send(file=discord.File('discordBot\\packageGenerator\\package.zip'))
                except Exception as e:
                    await message.channel.send(str(e))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
with open("discordBot\\token", 'r') as f:
    token = f.read()
client.run(token)
