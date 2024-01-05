import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True 
intents.message_content = True


TOKEN = 'replace with TOKEN'

# Prefix for commands
bot = commands.Bot(command_prefix='!', intents=intents)

# Intitialize bot
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Bot Commands
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

# Test Images
@bot.command(name='product')
async def product(ctx):
    embed = discord.Embed(title="Product Name", description="This is a great product.", color=0x00ff00)
    embed.add_field(name="Price", value="$9.99")
    embed.set_image(url="https://upload.wikimedia.org/wikipedia/en/thumb/0/09/Skibidi_toilet_screenshot.webp/237px-Skibidi_toilet_screenshot.webp.png")
    await ctx.send(embed=embed)


# Start the bot
bot.run(TOKEN)
