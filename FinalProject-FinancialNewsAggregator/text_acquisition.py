import requests
import json

news_sources = ['bbc-news', 'cnn', 'bloomberg']
api_key = '4783852d077f4c479f392fe657e763b4'

articles_data = {
    "articles" : []
}

for source in news_sources:
    url = 'https://newsapi.org/v2/everything?sources=' + source + '&apiKey=' + api_key
    response = requests.get(url)

    articles = response.json()['articles']

    for article in articles:
        articles_data['articles'].append(article)
        print(article['content'])

with open('articles.json', 'w', encoding='utf-8') as f:
    json.dump(articles_data, f, ensure_ascii=False, indent=4)
