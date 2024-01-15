import requests

base_url_th = 'https://newsapi.org/v2/top-headlines'

def headlines_url(**kwargs):
        result = base_url_th + '?'
        for i,j in kwargs.items():
                result += f'{i}={j}&'
        result += 'apiKey=25e5bde914644c75bfd59d97c616cef0'
        return result


def news_load(country='ru', category='sports', pageSize=20):
        url = headlines_url(country=country, category=category, pageSize=pageSize)
        data = requests.get(url).json()
        data['country'] = country
        data['category'] = category
        return data
