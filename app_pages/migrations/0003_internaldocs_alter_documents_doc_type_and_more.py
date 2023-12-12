# Generated by Django 4.2.7 on 2023-12-08 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pages', '0002_documents'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternalDocs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_title_uz', models.CharField(max_length=255, verbose_name='Ichik hujjatlar nomi')),
                ('doc_title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название внутренних документов')),
                ('doc_title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Inernal documents name')),
                ('doc_type', models.CharField(choices=[('2', 'Qaror'), ('1', 'Qonun')], max_length=15, verbose_name='Toifasi/type')),
                ('inter_text', models.TextField(verbose_name="Hujjatlarning to'liq tavsifi")),
                ('doc_code', models.CharField(max_length=50, verbose_name='N˚')),
                ('doc_date', models.DateField(verbose_name='Hujjat qabul qilingan vaqt')),
                ('doc_pdf', models.FileField(blank=True, null=True, upload_to='media/docs_pdf')),
            ],
            options={
                'db_table': 'Interlan_documents',
            },
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_type',
            field=models.CharField(choices=[('2', 'Qaror'), ('1', 'Qonun'), ('3', 'Farmoish'), ('5', 'Farmon'), ('4', 'Buyruq')], max_length=15, verbose_name='Toifasi/type'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='org_type',
            field=models.CharField(choices=[('5', 'Boshqarma'), ('3', 'Vazirlar mahkamasi'), ('4', 'Xalq talim vazirligi'), ('1', 'Parlamen'), ('2', 'Prezident')], max_length=25, verbose_name='Tashkilot/Organisation'),
        ),
    ]