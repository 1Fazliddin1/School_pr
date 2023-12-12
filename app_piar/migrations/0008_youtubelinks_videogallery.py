# Generated by Django 4.2.7 on 2023-12-12 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_piar', '0007_image_photogallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField()),
            ],
            options={
                'db_table': 'gallery_videos_links',
            },
        ),
        migrations.CreateModel(
            name='VideoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_title_uz', models.CharField(max_length=255, verbose_name='Videogallariya sahifasi')),
                ('gallery_title_ru', models.CharField(max_length=255, verbose_name='Название videoгалереи')),
                ('gallery_title_en', models.CharField(max_length=255, verbose_name='Videogallery title')),
                ('gallery_desc_uz', models.CharField(max_length=255, verbose_name='Videogallariya qisqacha tavsif')),
                ('gallery_desc_ru', models.CharField(max_length=255, verbose_name='Oписание videoгалереи')),
                ('gallery_desc_en', models.CharField(max_length=255, verbose_name='Videogallery description')),
                ('gallery_datetime', models.DateTimeField(auto_now_add=True)),
                ('gallery_view_count', models.IntegerField(default=0, verbose_name='Ko`rishlar soni')),
                ('gallery_video_links', models.ManyToManyField(to='app_piar.youtubelinks')),
            ],
        ),
    ]