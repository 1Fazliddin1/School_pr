from django.contrib import admin

from .models import News, Anons, Vacancy, PhotoGallery, Image, YoutubeLinks, VideoGallery


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ['news_title_uz', 'news_title_ru', 'news_title_en', 'news_image', 'news_desc_uz', 'news_desc_ru',
              'news_desc_en', 'news_text_uz', 'news_text_ru', 'news_text_en', 'news_source']
    list_display = ['id', 'news_title_uz', 'news_desc_uz', 'news_date', 'news_views_count']
    search_fields = ['news_title_uz', 'news_desc_uz', 'news_text_uz']


@admin.register(Anons)
class AnonsAdmin(admin.ModelAdmin):
    fields = ['anons_title_uz', 'anons_title_ru', 'anons_title_en', 'anons_desc_uz', 'anons_desc_ru',
              'anons_desc_en', 'anons_dateline']
    list_display = ['id', 'anons_title_uz', 'anons_desc_uz', 'anons_datetime', 'anons_dateline']
    search_fields = ['anons_title_uz', 'anons_desc_uz']


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    fields = ['vacancy_name_uz', 'vacancy_name_ru', 'vacancy_name_en', 'vacancy_desc_uz', 'vacancy_desc_ru',
              'vacancy_desc_en', 'vacancy_text_uz', 'vacancy_text_ru', 'vacancy_text_en', 'vacancy_status']
    list_display = ['id', 'vacancy_name_uz', 'vacancy_desc_uz', 'vacancy_datetime', 'vacancy_status']
    search_fields = ['vacancy_name_uz', 'vacancy_desc_uz', 'vacancy_text_uz']


admin.site.register(Image)
admin.site.register(YoutubeLinks)


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    fields = ['gallery_title_uz', 'gallery_title_ru', 'gallery_title_en', 'gallery_desc_uz', 'gallery_desc_ru',
              'gallery_desc_en', 'gallery_images']
    list_display = ['id', 'gallery_title_uz', 'gallery_desc_uz', 'gallery_datetime']
    search_fields = ['gallery_title_uz', 'gallery_desc_uz']


@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    fields = ['gallery_title_uz', 'gallery_title_ru', 'gallery_title_en', 'gallery_desc_uz', 'gallery_desc_ru',
              'gallery_desc_en', 'gallery_video_links']
    list_display = ['id', 'gallery_title_uz', 'gallery_desc_uz', 'gallery_datetime']
    search_fields = ['gallery_title_uz', 'gallery_desc_uz']
