# Generated by Django 4.2.7 on 2023-12-09 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_piar', '0002_alter_news_news_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_title_en',
            field=models.CharField(max_length=300, unique=True, verbose_name='News title'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_title_ru',
            field=models.CharField(max_length=300, unique=True, verbose_name='заголовок новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_title_uz',
            field=models.CharField(max_length=300, unique=True, verbose_name='Yangiliklar sarlavhasi'),
        ),
    ]
