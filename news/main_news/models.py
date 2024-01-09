from django.db import models


class Countries(models.Model):
    Name = models.CharField(max_length=20, verbose_name='Страна')
    ShortName = models.CharField(max_length=2, verbose_name='Краткое название')
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
class Categories(models.Model):
    NameRus = models.CharField(max_length=20, verbose_name='Категория')
    NameEng = models.CharField(max_length=20, verbose_name='Category')

    def __str__(self):
        return self.NameRus
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class RequestParamsTopLines(models.Model):
    Country = models.ForeignKey(Countries, on_delete=models.CASCADE, verbose_name='Страна')
    Category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')
    NumberLines = models.PositiveIntegerField(help_text='Макс кол-во: 100', verbose_name='Количество новостей')

    def __str__(self):
        return f'Страна - {self.Country.Name}, категория - {self.Category.NameRus}, число новстей - {self.NumberLines}'
    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры топ новостей'
# Create your models here.

class TopNews(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Наименование')
    source = models.CharField(max_length=200, verbose_name='Источник')
    author = models.CharField(max_length=200, default='Неизветный автор', verbose_name='Автор')
    topic = models.CharField(max_length=50, verbose_name='Тема')
    country = models.CharField(max_length=100, verbose_name='Страна')
    description = models.CharField(max_length=2000, default='Нет описания', verbose_name='Описание')
    url = models.CharField(max_length=2000, verbose_name='Ссылка')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
