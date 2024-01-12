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

COIN_IDS = {
    'btc': 'bitcoin',
    'eth': 'ethereum',
    'xrp': 'ripple',
    # Add more mappings as needed
}

def get_crypto_price(ticker):
    coin_id = COIN_IDS.get(ticker.lower())
    if not coin_id:
        coin_id = ticker
    
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {  
        'ids': coin_id,
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params = params)
    data = response.json()
    return data[coin_id]['usd'] if coin_id in data else None

def get_crypto_market_cap(ticker):
    coin_id = COIN_IDS.get(ticker.lower())
    if not coin_id:
        coin_id = ticker
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': coin_id,
        'vs_currencies': 'usd',
        'include_market_cap': 'true'
    }
    response = requests.get(url, params = params)
    data = response.json()
    market_cap_key = f'{coin_id}_usd_market_cap'
    return data[coin_id]['usd_market_cap'] if market_cap_key in data[coin_id] else None

@bot.command(name='crypto')
async def crypto(ctx, coin):
    price = get_crypto_price(coin.lower())
    cap = get_crypto_market_cap(coin.lower())
    if price is not None:
        await ctx.send(f"The current price of {coin.upper()} is: ${price}")
    else:
        await ctx.send(f"Couldn't fetch price for {coin.upper()}. Please check the coin symbol.")
    if cap is not None:
        await ctx.send(f"The market cap of {coin.upper()} is: ${cap}")
    else:
        await ctx.send(f"Couldn't fetch market cap for {coin.upper()}. Please check the coin symbol.")


@bot.command(name='beast')
async def beast(ctx):
    await ctx.send('You sexy beast!')

@bot.command(name='HowDoesDanLikeHisWomen')
async def HowDoesDanLikeHisWomen(ctx):
    await ctx.send('Large!')

# Start the bot
bot.run(TOKEN)
