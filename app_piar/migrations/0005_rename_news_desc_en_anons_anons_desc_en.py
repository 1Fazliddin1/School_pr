# Generated by Django 4.2.7 on 2023-12-09 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_piar', '0004_anons'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anons',
            old_name='news_desc_en',
            new_name='anons_desc_en',
        ),
    ]