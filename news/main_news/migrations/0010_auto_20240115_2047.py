# Generated by Django 3.2.16 on 2024-01-15 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_news', '0009_testimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimage',
            name='test',
            field=models.ImageField(upload_to='test_folder', verbose_name='Изображение'),
        ),
        migrations.CreateModel(
            name='TopNewsImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='http://127.0.0.1:8000/test_folder/harsh-taggar-asset.jpg', upload_to='test_folder', verbose_name='Изображение')),
                ('titleRus', models.CharField(default='Нет перевода', max_length=1000, verbose_name='Новость на русском')),
                ('titleOrig', models.CharField(max_length=1000, verbose_name='Новость в оригинале')),
                ('source', models.CharField(max_length=200, verbose_name='Источник')),
                ('author', models.CharField(default='Неизветный автор', max_length=200, verbose_name='Автор')),
                ('description', models.CharField(default='Нет описания', max_length=2000, verbose_name='Описание')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_news.countries', verbose_name='Страна')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_news.categories', verbose_name='Тема')),
            ],
            options={
                'verbose_name': 'Новость c картинкой',
                'verbose_name_plural': 'Новости с картинками',
            },
        ),
    ]
