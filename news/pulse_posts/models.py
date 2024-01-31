from django.db import models

class PostsTicker(models.Model):
    nickname = models.CharField(max_length=200, verbose_name='Никнейм автора')
    ticker = models.CharField(max_length=20, verbose_name='Тикер бумаги')
    likesCount = models.PositiveIntegerField(verbose_name='Кол-во лайков')
    commentsCount = models.PositiveIntegerField(verbose_name='Кол-во комментариев')
    inserted =  models.DateField(verbose_name='Дата публикации')
    text = models.TextField(verbose_name='Текст комментария')

    def __str__(self):
        return f'Пост автора - {self.nickname} по бумаге - {self.ticker}'

    class Meta:
        verbose_name = 'Пост по бумаге'
        verbose_name_plural = 'Посты по бумаге'


