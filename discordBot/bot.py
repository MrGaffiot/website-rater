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
        await ctx.message.channel.send(f"Yes master {ctx.message.author.name}!")
        await ctx.message.channel.send(f"Package  with length {message.content.split(' ')[1]}generated")
        await ctx.message.channel.send(file=discord.File('discordBot/packageGenerator/package.zip'))
    except Exception as e:
        await ctx.message.channel.send(str(e))

@bot.command()
async def kys(ctx):
    if ctx.message.author.name == "walper":
        await ctx.message.channel.send(f"Yes master {ctx.message.author.name}!")
    else:
        await ctx.message.channel.send(f"Nah fuck you")
    quit()
    
with open("discordBot/token", 'r') as f:
    token = f.read()

bot.run(token)
