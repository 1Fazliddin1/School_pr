from django.db import models


class News(models.Model):
    news_title_uz = models.CharField(max_length=300, verbose_name='Yangiliklar sarlavhasi', unique=True)
    news_title_ru = models.CharField(max_length=300, verbose_name='заголовок новости', unique=True)
    news_title_en = models.CharField(max_length=300, verbose_name='News title', unique=True)

    news_image = models.ImageField(upload_to='image/news', verbose_name='Image', null=True, blank=True)

    news_desc_uz = models.CharField(max_length=500, verbose_name='Yangiliklar qisqacha tavsifi')
    news_desc_ru = models.CharField(max_length=500, verbose_name='описание новости')
    news_desc_en = models.CharField(max_length=500, verbose_name='News description')

    news_text_uz = models.TextField(verbose_name='Yangiliklar to\'liq tavsifi')
    news_text_ru = models.TextField(verbose_name='Tekct новости')
    news_text_en = models.TextField(verbose_name='News text')

    news_date = models.DateTimeField(auto_now_add=True)
    news_views_count = models.IntegerField(verbose_name='Ko`rishlar soni', default=0)
    news_source = models.URLField(verbose_name='Manba (agar mavjud bo`lsa)', null=True, blank=True )

    class Mete:
        db_table = 'pr_news'
        ordering = ('-news_date', )

    def __str__(self):
        return f"{self.id}. {self.news_title_uz}"


class Anons(models.Model):
    anons_title_uz = models.CharField(max_length=300, verbose_name='E\'lon sarlavhasi')
    anons_title_ru = models.CharField(max_length=300, verbose_name='заголовок obyavleniyae')
    anons_title_en = models.CharField(max_length=300, verbose_name='Announcement title')

    anons_desc_uz = models.CharField(max_length=500, verbose_name='E\'lon qisqacha tavsifi')
    anons_desc_ru = models.CharField(max_length=500, verbose_name='описание obyavleniyae')
    anons_desc_en = models.CharField(max_length=500, verbose_name='Announcement description')

    anons_datetime = models.DateTimeField(auto_now_add=True)
    anons_dateline = models.DateTimeField()

    class Mete:
        db_table = 'pr_anons'
        ordering = ('-anons_datetime', )

    def __str__(self):
        return f"{self.id}. {self.anons_title_uz}"


class Vacancy(models.Model):
    vacancy_name_uz = models.CharField(max_length=100, verbose_name='Vakansiya nomi')
    vacancy_name_ru = models.CharField(max_length=100, verbose_name='Название вакансии')
    vacancy_name_en = models.CharField(max_length=100, verbose_name='Vacancy name')

    vacancy_desc_uz = models.CharField(max_length=500, verbose_name='Vakansiya qisqacha tavsifi')
    vacancy_desc_ru = models.CharField(max_length=500, verbose_name='Описание вакансии')
    vacancy_desc_en = models.CharField(max_length=500, verbose_name='Vacancy description')

    vacancy_text_uz = models.TextField(verbose_name='Vakansiya to\'liq tavsifi')
    vacancy_text_ru = models.TextField(verbose_name='вакансии новости', null=True, blank=True)
    vacancy_text_en = models.TextField(verbose_name='Vacancy text', null=True, blank=True)

    vacancy_datetime = models.DateTimeField(auto_now_add=True)
    vacancy_views_count = models.IntegerField(verbose_name='Ko`rishlar soni', default=0)
    vacancy_status = models.BooleanField(verbose_name='Vacancy holati', default=True)

    class Mete:
        db_table = 'pr_vacancy'
        ordering = ('-vacancy_datetime', )

    def __str__(self):
        return f"{self.id}. {self.vacancy_name_uz}"


class Image(models.Model):
    image = models.ImageField(upload_to='images/gallery')

    class Meta:
        db_table = 'gallery_images'


class PhotoGallery(models.Model):
    gallery_title_uz = models.CharField(max_length=255, verbose_name='Fotogallariya sahifasi')
    gallery_title_ru = models.CharField(max_length=255, verbose_name='Название фотогалереи')
    gallery_title_en = models.CharField(max_length=255, verbose_name='Photogallery title')

    gallery_desc_uz = models.CharField(max_length=255, verbose_name='Fotogallariya qisqacha tavsif')
    gallery_desc_ru = models.CharField(max_length=255, verbose_name='Oписание фотогалереи')
    gallery_desc_en = models.CharField(max_length=255, verbose_name='Photogallery description')

    gallery_datetime = models.DateTimeField(auto_now_add=True)
    gallery_view_count = models.IntegerField(verbose_name='Ko`rishlar soni', default=0)
    gallery_images = models.ManyToManyField(Image)

    class Mete:
        dt_table = 'pr_photogallery'
        ordering = ('-gallery_datetime', )


class YoutubeLinks(models.Model):
    video = models.URLField()

    class Meta:
        db_table = 'gallery_videos_links'


class VideoGallery(models.Model):
    gallery_title_uz = models.CharField(max_length=255, verbose_name='Videogallariya sahifasi')
    gallery_title_ru = models.CharField(max_length=255, verbose_name='Название videoгалереи')
    gallery_title_en = models.CharField(max_length=255, verbose_name='Videogallery title')

    gallery_desc_uz = models.CharField(max_length=255, verbose_name='Videogallariya qisqacha tavsif')
    gallery_desc_ru = models.CharField(max_length=255, verbose_name='Oписание videoгалереи')
    gallery_desc_en = models.CharField(max_length=255, verbose_name='Videogallery description')

    gallery_datetime = models.DateTimeField(auto_now_add=True)
    gallery_view_count = models.IntegerField(verbose_name='Ko`rishlar soni', default=0)
    gallery_video_links = models.ManyToManyField(YoutubeLinks)

    class Mete:
        dt_table = 'pr_videogallery'
        ordering = ('-gallery_datetime', )


