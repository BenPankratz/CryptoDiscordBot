import discord
from discord.ext import commands

class MyBot(commands.Bot):
    #event handling
    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')

    #command handling
    @commands.command(name='test')
    async def test(self, ctx):
        print("Test command was called")
        await ctx.send('Bot is up and running!')

    @commands.command(name='beast')
    async def beast(self, ctx):
        await ctx.send('You sexy beast!')

    @commands.command(name='HowDoesDanLikeHisWomen')
    async def HowDoesDanLikeHisWomen(self, ctx):
        await ctx.send('Large!') 

    @commands.command(name='product')
    async def product(self, ctx):
        embed = discord.Embed(title="Product Name", description="This is a great product.", color=0x00ff00)
        embed.add_field(name="Price", value="$9.99")
        embed.set_image(url="https://upload.wikimedia.org/wikipedia/en/thumb/0/09/Skibidi_toilet_screenshot.webp/237px-Skibidi_toilet_screenshot.webp.png")
        await ctx.send(embed=embed)

#Setup the bot
intents = discord.Intents.default()
intents.messages = True 
intents.message_content = True
TOKEN = 'replace with TOKEN' #Delete token when uploading to GitHub

#Start and initialize the bot
bot = MyBot(command_prefix='!', intents=intents)
bot.run(TOKEN)
