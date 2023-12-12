# Generated by Django 4.2.7 on 2023-12-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pages', '0005_alter_documents_doc_type_alter_documents_org_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='doc_type',
            field=models.CharField(choices=[('5', 'Farmon'), ('3', 'Farmoish'), ('2', 'Qaror'), ('4', 'Buyruq'), ('1', 'Qonun')], max_length=15, verbose_name='Toifasi/type'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='org_type',
            field=models.CharField(choices=[('1', 'Parlamen'), ('2', 'Prezident'), ('5', 'Boshqarma'), ('4', 'Xalq talim vazirligi'), ('3', 'Vazirlar mahkamasi')], max_length=25, verbose_name='Tashkilot/Organisation'),
        ),
    ]