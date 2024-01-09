import requests

base_url_th = 'https://newsapi.org/v2/top-headlines'

def headlines_url(**kwargs):
        result = base_url_th + '?'
        for i,j in kwargs.items():
                result += f'{i}={j}&'
        result += 'apiKey=25e5bde914644c75bfd59d97c616cef0'
        return result

url = headlines_url(country='us', category='sports', pageSize=100)

data = requests.get(url).json()
data['country'] = 'us'
data['category'] = 'sports'

if __name__=='__main__':
        print(data)