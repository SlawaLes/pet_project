# Generated by Django 3.2.16 on 2024-01-16 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_news', '0012_alter_topnews_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topnewsimages',
            name='url',
            field=models.URLField(max_length=1700, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='topnewstranslated',
            name='url',
            field=models.URLField(max_length=1700, verbose_name='Ссылка'),
        ),
    ]