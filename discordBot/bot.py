import discord
from discord.ext import commands
import packageGenerator.generate as generate
from packageGenerator.zipper import unzip_file
import packageHalnder.readInput as readInput
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

@bot.command()
async def download(ctx):
    # Check if message has attachments
    if not ctx.message.attachments:
        await ctx.message.channel.send("No attachments found in your message!")
        return
    
    # Download each attachment
    for attachment in ctx.message.attachments:
        try:
            # Get the filename from the attachment
            filename = attachment.filename
            
            # Create full path for saving
            filepath = f'discordBot/packageHalnder/{filename}'
            
            # Download the file
            await attachment.save(filepath)
            readInput.writeInput()
            # Send confirmation
            await ctx.message.channel.send(f"Downloaded '{filename}' successfully!")
            
        except Exception as e:
            await ctx.message.channel.send(f"Failed to download {filename}: {str(e)}")

@bot.command()
async def readDB(ctx):
    await ctx.message.channel.send(str(readInput.dbHanderl.readData()))
    
with open("discordBot/token", 'r') as f:
    token = f.read()

bot.run(token)
