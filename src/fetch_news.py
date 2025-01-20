import requests
import pandas as pd

def fetch_news(api_key, query='stocks', pages=1):
    """Fetch financial news articles using NewsAPI."""
    articles = []
    for page in range(1, pages + 1):
        url = f'https://newsapi.org/v2/everything?q={query}&page={page}&apiKey={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for article in data['articles']:
                articles.append({
                    'source': article['source']['name'],
                    'headline': article['title'],
                    'content': article['content'],
                    'date': article['publishedAt']
                })
    return pd.DataFrame(articles)

if __name__ == '__main__':
    api_key = 'your_newsapi_key_here'  # Replace with your API key
    df = fetch_news(api_key)
    df.to_csv('../data/raw_articles.csv', index=False)
