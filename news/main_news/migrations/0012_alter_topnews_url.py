# Generated by Django 3.2.16 on 2024-01-16 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_news', '0011_alter_countries_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topnews',
            name='url',
            field=models.URLField(max_length=1700, verbose_name='Ссылка'),
        ),
    ]
