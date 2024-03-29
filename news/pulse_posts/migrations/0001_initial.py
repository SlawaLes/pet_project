# Generated by Django 3.2.16 on 2024-01-29 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostsTicker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200, verbose_name='Никнейм автора')),
                ('ticker', models.CharField(max_length=20, verbose_name='Тикер бумаги')),
                ('likesCount', models.PositiveIntegerField(verbose_name='Кол-во лайков')),
                ('commentsCount', models.PositiveIntegerField(verbose_name='Кол-во комментариев')),
                ('inserted', models.DateField(verbose_name='Дата публикации')),
                ('text', models.TextField(verbose_name='Текст комментария')),
            ],
            options={
                'verbose_name': 'Пост по бумаге',
                'verbose_name_plural': 'Посты по бумаге',
            },
        ),
    ]
