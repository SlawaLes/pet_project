# Generated by Django 3.2.16 on 2024-01-14 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_news', '0005_alter_topnews_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topnews',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_news.countries', verbose_name='Страна'),
        ),
    ]