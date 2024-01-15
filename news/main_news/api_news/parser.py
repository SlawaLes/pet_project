from main_news.models import TopNews
from main_news.models import Countries, Categories
def pars(dict):
    for article in dict['articles']:
        country = Countries.objects.get(ShortName=dict['country'])
        category = Categories.objects.get(NameEng=dict['category'])
        TopNews.objects.create(
            source=article['source']['name'],
            author=article['author'] if article['author'] else '',
            title=article['title'],
            description=article['description'] if article['description'] else '',
            url=article['url'],
            country=country,
            topic=category
            )


