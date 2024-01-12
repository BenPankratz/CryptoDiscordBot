import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

TOKEN = '' #Delete token when uploading to GitHub

API_KEY = 'CG-6Jo2ZVRrgQBFywfd3BVoEWKZ'

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

def get_crypto_info(ticker):
    COIN_IDS = {
    'btc': 'bitcoin',
    'eth': 'ethereum',
    'xrp': 'ripple',
    # Add more mappings as needed
}

    coin_id = COIN_IDS.get(ticker.lower(),ticker) #returns the ticker as a default if not found

    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': coin_id,
        'vs_currencies': 'usd',
        'include_market_cap': 'true',
        'include_24hr_vol' : 'true',
        'include_24hr_change' : 'true',
        'include_last_updated_at' : 'true'
    }
    response = requests.get(url, params = params)
    data = response.json()

    if coin_id in data:
        coin_data = data[coin_id]
        return [
            coin_data.get('usd', None),
            coin_data.get('usd_market_cap', None),
            coin_data.get('usd_24h_vol', None),
            coin_data.get('usd_24h_change', None),
            coin_data.get('last_updated_at', None)
        ]
    else:
        return None

@bot.command(name='crypto')
async def crypto(ctx, coin):
    info = get_crypto_info(coin)
    if info is not None:
        await ctx.send(
            f"""
            Crypto Data:\n
            Price: ${info[0]}USD\nMarket Cap: ${info[1]}USD\n24 Hour Volume: ${info[2]}USD\n
            24 Hour Change: {info[3]}%\nLast Updated: {info[4]}
            """
            )
    else:
        await ctx.send("Data not available for this ticker.")

@bot.command(name='beast')
async def beast(ctx):
    await ctx.send('You sexy beast!')

@bot.command(name='HowDoesDanLikeHisWomen')
async def HowDoesDanLikeHisWomen(ctx):
    await ctx.send('Large!')

# Start the bot
bot.run(TOKEN)
