# Generated by Django 4.0 on 2024-03-03 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_news', '0013_auto_20240116_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topnews',
            name='source',
            field=models.CharField(default='Робот', max_length=200, verbose_name='Источник'),
        ),
    ]
