from django.db import models


class AboutSchool(models.Model):
    school_name_uz = models.CharField(max_length=255, verbose_name='Maktab nomi')
    school_name_ru = models.CharField(max_length=255, verbose_name='Hазвание школы', blank=True, null=True)
    school_name_en = models.CharField(max_length=255, verbose_name='School name', blank=True, null=True)

    school_logo = models.ImageField(upload_to='school/', blank=True, null=True)

    school_address_uz = models.CharField(max_length=255, verbose_name='Maktab manzili')
    school_address_ru = models.CharField(max_length=255, verbose_name='Aдрес школы', blank=True, null=True)
    school_address_en = models.CharField(max_length=255, verbose_name='School address', blank=True, null=True)

    school_email = models.EmailField(verbose_name='Email', blank=True, null=True)
    school_phone = models.CharField(verbose_name='Telefon', blank=True, null=True)
    school_prime_time = models.CharField(max_length=50, verbose_name='Qabul vaqlari', blank=True, null=True)

    school_location_lat = models.CharField(max_length=50, verbose_name='Latitude', blank=True, null=True)
    school_location_lon = models.CharField(max_length=50, verbose_name='Longitude', blank=True, null=True)

    school_smm_tg = models.CharField(max_length=50, verbose_name='Telegram', blank=True, null=True)
    school_smm_ig = models.CharField(max_length=50, verbose_name='Instagram', blank=True, null=True)
    school_smm_fb = models.CharField(max_length=50, verbose_name='Facebook', blank=True, null=True)
    school_smm_yt = models.CharField(max_length=50, verbose_name='Youtube', blank=True, null=True)

    def __str__(self):
        return self.school_name_uz

    class Meta:
        db_table = 'school_info'


class Documents(models.Model):
    doc_title_uz = models.CharField(max_length=255, verbose_name='Hujjatlar nomi')
    doc_title_ru = models.CharField(max_length=255, verbose_name='название документа')
    doc_title_en = models.CharField(max_length=255, verbose_name='Documents name')

    doc_types = {
        ('1', 'Qonun'),
        ('2', 'Qaror'),
        ('3', 'Farmoish'),
        ('4', 'Buyruq'),
        ('5', 'Farmon'),
    }

    doc_type = models.CharField(max_length=15, choices=doc_types, verbose_name='Toifasi/type')
    org_types = {
        ('1', 'Parlamen'),
        ('2', 'Prezident'),
        ('3', 'Vazirlar mahkamasi'),
        ('4', 'Xalq talim vazirligi'),
        ('5', 'Boshqarma'),
    }
    org_type = models.CharField(max_length=25, choices=org_types, verbose_name='Tashkilot/Organisation')
    doc_code = models.CharField(max_length=50, verbose_name='N˚')
    doc_date = models.DateField(verbose_name='Hujjat qabul qilingan vaqt')
    doc_link = models.URLField(verbose_name='Hujjat havolasi', blank=True, null=True)

    def __str__(self):
        return self.doc_title_uz

    class Meta:
        db_table = 'Documents'


class InternalDocs(models.Model):
    doc_title_uz = models.CharField(max_length=255, verbose_name='Ichik hujjatlar nomi')
    doc_title_ru = models.CharField(max_length=255, verbose_name='Название внутренних документов', blank=True, null=True)
    doc_title_en = models.CharField(max_length=255, verbose_name='Inernal documents name', blank=True, null=True)

    doc_types = {
        ('1', 'Qaror'),
        ('2', 'Buyruq'),
    }

    doc_type = models.CharField(max_length=15, choices=doc_types, verbose_name='Toifasi/type')
    inter_text = models.TextField(verbose_name='Hujjatlarning to\'liq tavsifi')
    doc_code = models.CharField(max_length=50, verbose_name='N˚')
    doc_date = models.DateField(verbose_name='Hujjat qabul qilingan vaqt')
    doc_pdf = models.FileField(upload_to='media/docs_pdf', blank=True, null=True)

    def __str__(self):
        return self.doc_title_uz

    class Meta:
        db_table = 'Interlan_documents'