import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True 
intents.message_content = True

# Replace 'your_bot_token' with the token you got from the Discord Developer Portal
TOKEN = 'MTE5Mjg4OTc0MDQ1ODk5NTc2NA.GWBCSm.KvdD_qaVkrn3Yy0sI-a0m2Vjb5T5rYpelPaAPw'

# Prefix for commands
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='test')
async def test(ctx):
    print("Test command was called")
    await ctx.send('Bot is up and running!')

@bot.command(name='beast')
async def beast(ctx):
    await ctx.send('You sexy beast!')

@bot.command(name='HowDoesDanLikeHisWomen')
async def HowDoesDanLikeHisWomen(ctx):
    await ctx.send('Large!') 

# Start the bot
bot.run(TOKEN)
