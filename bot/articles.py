import requests
from bs4 import BeautifulSoup

def get_crypto_news(crypto_name):
    # CoinDesk search URL (you might need to adjust this based on how their search works)
    url = f'https://www.coindesk.com/search/?s={crypto_name}'
    
    try:
        # Fetch the content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for unsuccessful status codes

        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the news articles - the selectors need to be adjusted based on CoinDesk's HTML structure
        articles = soup.find_all('div', class_='article', limit=3)
        print(articles)
        # Extracting the top 3 news titles and links
        news_list = []
        for article in articles:
            title = article.find('h4').get_text().strip()  # Adjust the tag and class based on actual structure
            link = article.find('a')['href']
            news_list.append({'title': title, 'link': link})
        return news_list
    
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'An error occurred: {err}')

# Example usage
crypto_news = get_crypto_news('Bitcoin')
for news in crypto_news:
    print(f"Title: {news['title']}, Link: {news['link']}")
