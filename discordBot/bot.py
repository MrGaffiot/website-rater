import discord
from discord.ext import commands
from dbHanderl import databaseHandler
import packageGenerator.generate as generate
#await message.channel.send("User added")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def generate(ctx, arg):
    try:
        generate.makePackage(generate.makePackageInfo(int(arg)))
        await message.channel.send(f"Package  with length {message.content.split(' ')[1]}generated")
        await message.channel.send(file=discord.File('discordBot/packageGenerator/package.zip'))
    except Exception as e:
        await message.channel.send(str(e))

@bot.command()
async def work(ctx):
    await message.channel.send(f"Yes master {message.author.name}!")
    
with open("discordBot/token", 'r') as f:
    token = f.read()

bot.run(token)
