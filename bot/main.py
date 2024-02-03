import discord
from database import initialize_database, insert_user, insert_coin, get_user_coins, query_data
from discord.ext import commands
import requests
import datetime 
import matplotlib.pyplot as plt
import io
from COIN_IDS import COIN_IDS

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

TOKEN = ''
#test
bot = commands.Bot(command_prefix='!', intents=intents)#Prefix for commands
initialize_database()

#test test 
#test test
#test test
#test test

@bot.event  #Intitialize bot
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='test')
async def test(ctx):
    print("Test command was called")
    await ctx.send('Bot is up and running!')

def get_crypto_info(ticker):
    coin_id = COIN_IDS.get(ticker.lower(), ticker)  # returns the ticker as a default if not found
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = { #what information do we need from coingecko api?
        'ids': coin_id,
        'vs_currencies': 'usd',
        'include_market_cap': 'true',
        'include_24hr_vol': 'true',
        'include_24hr_change': 'true',
        'include_last_updated_at': 'true'
    }
    response = requests.get(url, params=params)
    data = response.json()

    if coin_id in data:
        coin_data = data[coin_id]
        last_updated = datetime.datetime.fromtimestamp(coin_data.get('last_updated_at')).strftime('%Y-%m-%d %H:%M:%S')
        return [
            coin_data.get('usd', None),
            coin_data.get('usd_market_cap', None),
            coin_data.get('usd_24h_vol', None),
            coin_data.get('usd_24h_change', None),
            last_updated
        ]
    else:
        return None


@bot.command(name='crypto')
async def crypto(ctx, coin):
    info = get_crypto_info(coin) #Calls get_crypto_info, which returns a list of information
    if info is not None:
        coin_name = coin.capitalize()  # Capitalize the first letter

        price = f"${info[0]:,.2f}" #Format specifiers
        market_cap = f"${int(info[1]):,}"
        volume_24h = f"${int(info[2]):,}"
        change_24h = f"{info[3]:.2f}%"

        await ctx.send(
            f"{coin_name} Data:\n\n"
            f"Price: {price}\n"
            f"Market Cap: {market_cap}\n"
            f"24 Hour Volume: {volume_24h}\n"
            f"24 Hour Change: {change_24h}\n"
            f"Last Updated: {info[4]}"
        )
    else: #Data was not found for this ticker
        await ctx.send("Data not available for this ticker.")


def get_crypto_chart(coin_id):
    # Fetch historical data from an API
    response = requests.get(f'https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart')
    data = response.json()

    # Example data processing (this will vary based on your data source)
    timestamps = [point['timestamp'] for point in data]
    prices = [point['price'] for point in data]

    # Creating a plot
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, prices, label=f'Price of {coin_id} over the last 24 hours')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title(f'{coin_id} Price Chart')
    plt.legend()

    # Saving plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return buf

# In your Discord command
@bot.command(name='chart')
async def chart(ctx, coin):
    coin_id = COIN_IDS.get(coin.lower(), coin)  # Convert to coin ID
    chart_image = get_crypto_chart(coin_id)
    await ctx.send(file=discord.File(chart_image, f'{coin_id}_chart.png'))

@bot.command(name='add')
async def add(ctx, coin):
    username = ctx.author.name
    insert_coin(username, coin)
    await ctx.send(f"Added {coin} for {username}")
    query_data()


@bot.command(name='report')
async def report(ctx):
    coins = get_user_coins(ctx.author.name)
    if(len(coins) == 0):
        await ctx.send("you have no coins saved. Use '!add *coin name*' to add a coin.")
        return 
    await ctx.send("Here's a report on your current crypo coins")
    message = ""
    for coin in coins:
        info = get_crypto_info(coin) #Calls get_crypto_info, which returns a list of information
        if info is not None:
            coin_name = coin.capitalize()  # Capitalize the first letter

            price = f"${info[0]:,.2f}" #Format specifiers
            market_cap = f"${int(info[1]):,}"
            volume_24h = f"${int(info[2]):,}"
            change_24h = f"{info[3]:.2f}%"

            await ctx.send(
                f"{coin_name} Data:\n\n"
                f"Price: {price}\n"
                f"Market Cap: {market_cap}\n"
                f"24 Hour Volume: {volume_24h}\n"
                f"24 Hour Change: {change_24h}\n"
                f"Last Updated: {info[4]}\n\n"
            )
        else: #Data was not found for this ticker
            await ctx.send("Data not available for this ticker.")

        
@bot.command(name='beast')
async def beast(ctx):
    await ctx.send('You sexy beast!')

@bot.command(name='HowDoesDanLikeHisWomen')
async def HowDoesDanLikeHisWomen(ctx):
    await ctx.send('Large!')


# Start the bot
bot.run(TOKEN)
