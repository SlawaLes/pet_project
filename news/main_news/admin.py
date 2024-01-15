from django.contrib import admin
from .models import Countries, Categories, RequestParamsTopLines, TopNews, TopNewsTranslated
from main_news.api_news.loader import news_load
from main_news.api_news.parser import pars
from main_news.api_news.translator_yan import translation

class CountryAdmin(admin.ModelAdmin):
    search_fields = ['Name']
    class Meta:
        fields = '__all__'

class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'

class RequestParamsTopLinesAdmin(admin.ModelAdmin):
    @admin.action(description='Загрузить новости')
    def make_requests(self, request, queryset):
        for params in queryset:
            country = params.Country.ShortName
            category = params.Category.NameEng
            num_news = params.NumberLines
            news = news_load(country=country, category=category, pageSize=num_news)
            pars(news)
    actions = ['make_requests', ]
    class Meta:
        fields = '__all__'


class TopNewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'topic', 'url_short']
    list_filter = ['topic', 'country__Name']

    def url_short(self, object):
        return object.url[:50]

    url_short.short_description = 'Ссылка'
    @admin.action(description='Перевести новость')
    def make_translation(self, request, queryset):
        for new in queryset:
            TopNewsTranslated.objects.create(
                titleRus=translation(new.title) if new.country.ShortName != 'ru' else new.title,
                titleOrig=new.title,
                source=new.source,
                author=new.author,
                description=new.description,
                url=new.url,
                country=new.country,
                topic=new.topic)
    actions = ['make_translation', ]
    class Meta:
        fields = '__all__'

class TopNewsTransAdmin(admin.ModelAdmin):
    list_display = ['titleRus', 'titleOrig', 'author', 'topic']
    list_filter = ['topic', 'country']
    class Meta:
        fields = '__all__'


admin.site.register(TopNewsTranslated, TopNewsTransAdmin)
admin.site.register(TopNews, TopNewsAdmin)
admin.site.register(Countries, CountryAdmin)
admin.site.register(Categories, CategoryAdmin)
admin.site.register(RequestParamsTopLines, RequestParamsTopLinesAdmin)

# Register your models here.
