import requests
import matplotlib.pyplot as plt
import io

url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/usd/1'

response = requests.get(url)

if response.status_code == 200:
         data = response.json()
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

         print(buf)
else:
         print('Failed to retrieve data from the API')