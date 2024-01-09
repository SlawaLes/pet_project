from .loader import data
import pandas as pd


for article in data['articles']:
    source = article['source'][0]['name']
    author = article['author']
    title = article['title']
    description = article['description']
    url = article['url']
    topic = data['topic']
    country = data['country']



