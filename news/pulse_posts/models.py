from django.db import models


class Instrument(models.Model):
    ticker = models.CharField(max_length=50, verbose_name='Тикер')
    name = models.CharField(max_length=255, verbose_name='Название бумаги')
    type = models.CharField(max_length=50, verbose_name='Тип инструмента')

    def __str__(self):
        return f'Инструмент - {self.name}'

    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'


class Investor(models.Model):
    nickname = models.CharField(max_length=255, verbose_name='Никнейм')
    profile_tinkoff = models.CharField(max_length=255, verbose_name='Профиль Тинькофф')

    def __str__(self):
        return f'Инвестор - {self.nickname}'

    class Meta:
        verbose_name = 'Инвестор'
        verbose_name_plural = 'Инвесторы'

class Post(models.Model):
    likesCount = models.PositiveIntegerField(verbose_name='Кол-во лайков')
    commentsCount = models.PositiveIntegerField(verbose_name='Кол-во комментариев')
    reactionsCount = models.PositiveIntegerField(verbose_name='Кол-во реакций')
    inserted = models.DateField(verbose_name='Дата публикации')
    text = models.TextField(verbose_name='Текст комментария')
    instrument = models.ManyToManyField(Instrument, related_name='total_posts')
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE, related_name='my_posts',verbose_name='Инвестор')

    # def __str__(self):
    #     return self.investor.nickname

    class Meta:
        verbose_name = 'Пост по бумаге'
        verbose_name_plural = 'Посты по бумаге'

