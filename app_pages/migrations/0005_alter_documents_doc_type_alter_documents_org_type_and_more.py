# Generated by Django 4.2.7 on 2023-12-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pages', '0004_alter_documents_doc_type_alter_documents_org_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='doc_type',
            field=models.CharField(choices=[('5', 'Farmon'), ('1', 'Qonun'), ('4', 'Buyruq'), ('3', 'Farmoish'), ('2', 'Qaror')], max_length=15, verbose_name='Toifasi/type'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='org_type',
            field=models.CharField(choices=[('5', 'Boshqarma'), ('3', 'Vazirlar mahkamasi'), ('4', 'Xalq talim vazirligi'), ('2', 'Prezident'), ('1', 'Parlamen')], max_length=25, verbose_name='Tashkilot/Organisation'),
        ),
        migrations.AlterField(
            model_name='internaldocs',
            name='doc_type',
            field=models.CharField(choices=[('1', 'Qaror'), ('2', 'Buyruq')], max_length=15, verbose_name='Toifasi/type'),
        ),
    ]