from django.contrib import admin
from .models import Countries, Categories, RequestParamsTopLines, TopNews, TopNewsTranslated, testImage, TopNewsImages
from main_news.api_news.loader import news_load
from main_news.api_news.parser import pars
from main_news.api_news.translator_yan import translation
from main_news.api_news.image_generation import generator

from news.settings import MEDIA_ROOT


class CountryAdmin(admin.ModelAdmin):
    list_display = ['Name', 'ShortName']
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
    @admin.action(description='Сгенерировать картинку')
    def make_picture(self, request, queryset):
        for new in queryset:
            TopNewsImages.objects.create(
                image=generator(new.titleRus),
                titleRus=new.titleRus,
                titleOrig=new.titleOrig,
                source=new.source,
                author=new.author,
                description=new.description,
                url=new.url,
                country=new.country,
                topic=new.topic)

    actions = ['make_picture', ]
    class Meta:
        fields = '__all__'
class TestImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'test', 'image_tag']
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        from django.utils.html import mark_safe
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(url="{0}{1}".format('http://127.0.0.1:8000/', obj.test.url),
                                                                                      width=64*2,
                                                                                      height=64*2))

    image_tag.short_description = 'Изображение'
    class Meta:
        fields = '__all__'

class TopNewsImagesAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'titleRus', 'titleOrig', 'topic', 'country']
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        from django.utils.html import mark_safe
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(url="{0}{1}".format('http://127.0.0.1:8000/', obj.image.url),
                                                                                      width=64*2,
                                                                                      height=64*2))

    image_tag.short_description = 'Изображение'
    class Meta:
        fields = '__all__'


admin.site.register(TopNewsImages, TopNewsImagesAdmin)
admin.site.register(testImage, TestImageAdmin)
admin.site.register(TopNewsTranslated, TopNewsTransAdmin)
admin.site.register(TopNews, TopNewsAdmin)
admin.site.register(Countries, CountryAdmin)
admin.site.register(Categories, CategoryAdmin)
admin.site.register(RequestParamsTopLines, RequestParamsTopLinesAdmin)

# Register your models here.
