# Generated by Django 4.2.7 on 2023-12-11 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_piar', '0006_vacancy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/gallery')),
            ],
            options={
                'db_table': 'gallery_images',
            },
        ),
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_title_uz', models.CharField(max_length=255, verbose_name='Fotogallariya sahifasi')),
                ('gallery_title_ru', models.CharField(max_length=255, verbose_name='Название фотогалереи')),
                ('gallery_title_en', models.CharField(max_length=255, verbose_name='Photogallery title')),
                ('gallery_desc_uz', models.CharField(max_length=255, verbose_name='Fotogallariya qisqacha tavsif')),
                ('gallery_desc_ru', models.CharField(max_length=255, verbose_name='Oписание фотогалереи')),
                ('gallery_desc_en', models.CharField(max_length=255, verbose_name='Photogallery description')),
                ('gallery_datetime', models.DateTimeField(auto_now_add=True)),
                ('gallery_view_count', models.IntegerField(default=0, verbose_name='Ko`rishlar soni')),
                ('gallery_images', models.ManyToManyField(to='app_piar.image')),
            ],
        ),
    ]