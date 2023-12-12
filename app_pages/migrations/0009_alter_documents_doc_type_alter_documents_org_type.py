# Generated by Django 4.2.7 on 2023-12-08 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pages', '0008_alter_documents_doc_type_alter_documents_org_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='doc_type',
            field=models.CharField(choices=[('2', 'Qaror'), ('5', 'Farmon'), ('4', 'Buyruq'), ('1', 'Qonun'), ('3', 'Farmoish')], max_length=15, verbose_name='Toifasi/type'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='org_type',
            field=models.CharField(choices=[('4', 'Xalq talim vazirligi'), ('5', 'Boshqarma'), ('3', 'Vazirlar mahkamasi'), ('2', 'Prezident'), ('1', 'Parlamen')], max_length=25, verbose_name='Tashkilot/Organisation'),
        ),
    ]
